import re
import os.path
import json as simplejson
import jinja2

LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"(.*?)"'), r"``\1''"),
    (re.compile(r'"'), r"''"),
    (re.compile(r'-{4,}'), r'--- '),
    (re.compile(r'\.{4,}'), r'\\dots. '),
    (re.compile(r'\.{3}'), r'\\dots '),
    (re.compile(r'LaTeX'), r'\\LaTeX\\'),
)

def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval

NEWLINE_SUB = (re.compile(r'(?<!\n)\n'), r" \\\\\n")
def newline(value):
    pattern, replacement = NEWLINE_SUB
    newval = pattern.sub(replacement, value)
    return newval

with open('hashtag_hyphenation.json') as f:
    HASHTAG_HYPHENATION = simplejson.load(f)

HASH_RE = re.compile(r'#\w+')
def hyphenate_hashtags(s):
    hashtags = HASH_RE.findall(s)
    for hashtag in hashtags:
        s = s.replace(hashtag, HASHTAG_HYPHENATION[hashtag])
    return s

env = jinja2.Environment(block_start_string = '%{',
                         block_end_string = '%}',
                         variable_start_string = '%{{',
                         variable_end_string = '%}}',
                         loader = jinja2.FileSystemLoader(os.path.abspath('.')))
env.filters['escape_tex'] = escape_tex
env.filters['newline'] = newline
env.filters['hyphenate_hashtags'] = hyphenate_hashtags

def p(value):
    return '<p>\n'+'</p>\n<p>'.join(value.split('\n\n'))+'\n</p>'

SLUG_CHARS_SUB = (re.compile('[^A-Za-z0-9 ]'), '')
def slugify(value):
    pattern, replacement = SLUG_CHARS_SUB
    newval = pattern.sub(replacement, value)
    newval = newval.replace(' ', '-')
    return newval

def p_br(value):
    chunks = value.split('\n\n')
    new_chunks = []
    for chunk in chunks:
        lines = chunk.split('\n')
        new_lines = []
        for line in lines:
            if len(line) < 40:
                line += "<br />"
            new_lines.append(line)
        new_chunks.append('\n'.join(new_lines))
    return '<p>\n'+'</p>\n<p>'.join(new_chunks)+'\n</p>'

html_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('.')))
html_env.filters['p'] = p
html_env.filters['p_br'] = p_br
html_env.filters['slugify'] = slugify

fname = "MergedPosts.json"
with open(fname) as f:
    posts = simplejson.load(f)

with open("sections.json") as f:
    sections = simplejson.load(f)

prev_start = None
sections.reverse()
for i, section in enumerate(sections):
    sect_start = section['startsat']
    if prev_start:
        s_posts = filter(lambda post: int(post['timestamp']) >= sect_start and int(post['timestamp']) < prev_start, posts)
    else:
        s_posts = filter(lambda post: int(post['timestamp']) >= sect_start, posts)
    prev_start = sect_start
    section['posts'] = s_posts 
sections.reverse()

with open('preface.txt') as f:
    preface = f.read()

context = {'sections': sections, 'preface': preface}

with open("context.json", 'w') as f:
    simplejson.dump(context, f, indent=1)

t = env.get_template('template.tex')

tex = t.render(context)
with open("MakeWayForPiggies.tex", 'w') as f:
    f.write(tex.encode('utf-8'))

html_template = html_env.get_template('template.html')
html = html_template.render(context)

with open("index.html", 'w') as f:
    f.write(html.encode('utf-8'))


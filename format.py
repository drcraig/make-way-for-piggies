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
    (re.compile(r'\.\.\.+'), r'\\ldots '),
    (re.compile(r'(?<!\n)\n'), r" \\\\\n"),
)

def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval

env = jinja2.Environment(block_start_string = '%{',
                         block_end_string = '%}',
                         variable_start_string = '%{{',
                         variable_end_string = '%}}',
                         loader = jinja2.FileSystemLoader(os.path.abspath('.')))
env.filters['escape_tex'] = escape_tex


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

with open("context.json", 'w') as f:
    simplejson.dump(sections, f, indent=1)

t = env.get_template('template.tex')

tex = t.render({'sections': sections})
with open("PreggoPosts.tex", 'w') as f:
    f.write(tex.encode('utf-8'))

#print tex
#print len(posts)

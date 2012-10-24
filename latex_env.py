import os.path
import re
import jinja2
import json as simplejson

LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"(.*?)"', re.DOTALL), r"``\1''"),
    (re.compile(r'"'), r"''"),
    (re.compile(r'-{4,}'), r'--- '),
    (re.compile(r'\.{4,}'), r'\\dots. '),
    (re.compile(r'\.{3}'), r'\\dots\\ '),
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


def generate_hyphenation_function(hyphenation_file):
    with open('hashtag_hyphenation.json') as f:
        HASHTAG_HYPHENATION = simplejson.load(f)
    HASH_RE = re.compile(r'#\w+')
    def hyphenate_hashtags(s):
        hashtags = HASH_RE.findall(s)
        for hashtag in hashtags:
            s = s.replace(hashtag, HASHTAG_HYPHENATION[hashtag])
        return s
    return hyphenate_hashtags

def get_env(hyphenation_file=None):
    env = jinja2.Environment(block_start_string = '%{',
                             block_end_string = '%}',
                             variable_start_string = '%{{',
                             variable_end_string = '%}}',
                             loader = jinja2.FileSystemLoader(os.path.abspath('.')))
    env.filters['escape_tex'] = escape_tex
    env.filters['newline'] = newline
    if hyphenation_file:
        env.filters['hyphenate_hashtags'] = generate_hyphenation_function(hyphenation_file)
    return env

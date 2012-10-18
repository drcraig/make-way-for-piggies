import re
import os.path
import jinja2

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

def get_env():
    env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('.')))
    env.filters['p'] = p
    env.filters['p_br'] = p_br
    env.filters['slugify'] = slugify
    return env

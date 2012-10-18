import argparse
import os.path
import json as simplejson

import html_env
import latex_env

def render(template, context, hyphenation_file=None):
    _, ext = os.path.splitext(args.template)
    if ext == '.html':
        env = html_env.get_env()
    elif ext == '.tex':
        env = latex_env.get_env(hyphenation_file=hyphenation_file)
    else:
        raise Exception("Must be html or latex")

    t = env.get_template(args.template)
    return t.render(context)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Render the book")
    parser.add_argument("--context", required=True)
    parser.add_argument("--template", required=True)
    parser.add_argument("--hyphenation", default=None)
    parser.add_argument("--output")
    args = parser.parse_args()

    with open(args.context) as f:
        context = simplejson.load(f)

    output = render(args.template, context, hyphenation_file=args.hyphenation)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output.encode('utf-8'))
    else:
        print output

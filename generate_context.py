import argparse
import json as simplejson

def generate_context(posts, sections, preface):

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

    context = {'sections': sections, 'preface': preface}
    return context

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create the combined context.")
    parser.add_argument("--posts", required=True)
    parser.add_argument("--sections", required=True)
    parser.add_argument("--preface", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    with open(args.posts) as f:
        posts = simplejson.load(f)

    with open(args.sections) as f:
        sections = simplejson.load(f)

    with open(args.preface) as f:
        preface = f.read()

    context = generate_context(posts, sections, preface)

    print args.output
    if args.output:
        with open(args.output, 'w') as f:
            simplejson.dump(context, f, indent=1)
    else:
        print context

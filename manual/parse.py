import re
import os.path
import json as simplejson

with open('photocaptions.txt') as f:
    contents = f.read()

TIME_RE = re.compile('<abbr title="(?P<humantimestamp>.*)" data-utime="(?P<timestamp>.*)">.*</abbr>')

j = []
for chunk in contents.split('\n\n'):
    lines = chunk.splitlines()
    timeline = lines[0]
    data = TIME_RE.search(timeline).groupdict()
    data['text'] = '\n'.join(lines[1:-1])
    data['image'] = os.path.basename(lines[-1])
    j.append(data)
print simplejson.dumps(j, indent=1)

with open('photocaptions.json', 'w') as f:
    simplejson.dump(j, f, indent=1)

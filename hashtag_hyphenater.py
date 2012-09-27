import re
import simplejson

with open('MergedPosts.json') as f:
    j = simplejson.load(f)

HASHTAG_RE = re.compile('#\w+')

hashtags = []
for p in j:
    text = p['text']
    hashtags.extend(HASHTAG_RE.findall(text)
)

dictionary_files = [
    'SallyWords.txt',
    '/Users/drcraig/Downloads/ispell-enwl-3.1.20/english.0',
    '/Users/drcraig/Downloads/ispell-enwl-3.1.20/english.1',
    '/Users/drcraig/Downloads/ispell-enwl-3.1.20/english.2',
    '/Users/drcraig/Downloads/ispell-enwl-3.1.20/english.3',
   # '/Users/drcraig/Downloads/ispell-enwl-3.1.20/american.0',
   # '/Users/drcraig/Downloads/ispell-enwl-3.1.20/american.1',
   # '/Users/drcraig/Downloads/ispell-enwl-3.1.20/american.2',
]

dictionary_words = []
for df in dictionary_files:
    with open(df) as f:
        lines = f.readlines()
    dictionary_words.extend([line.rstrip().lower() for line in lines])
dictionary_words.extend(map(str,range(0,100)))

def find_longest_words(text, words=[]):
    word = ''
    remainder = text
    for i in xrange(0,len(text)+1):
        possible_word = text[0:i]
        if possible_word in dictionary_words:
            word = possible_word
            remainder = text[i:]
    if word:
        words.append(word)
        return find_longest_words(remainder, words)
    else:
        if remainder:
            words.append(remainder)
        return words

h = {}
for hashtag in hashtags:
    words = find_longest_words(hashtag.lstrip('#'), [])
    h[hashtag] = '#'+(r'\-'.join(words))
with open('hashtag_hyphenation.json', 'w') as f:
    simplejson.dump(h,f, indent=1)

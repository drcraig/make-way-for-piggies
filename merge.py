import json as simplejson

with open('PregnantSallyPosts.json') as f:
    j1 = simplejson.load(f)

with open('manual/photocaptions.json') as f:
    j2 = simplejson.load(f)

d1 = {d['text']:d for d in j1}

also_in_1 = []
not_in_1 = []
for j in j2:
    d = d1.get(j['text'])
    if d:
        also_in_1.append(j)
    else:
        not_in_1.append(j)

merged_d = d1.copy()

for j in also_in_1:
    d = merged_d[j['text']]
    d.update(j)
    print d
    print j.keys()

merged_j = merged_d.values()
merged_j.extend(not_in_1) 

merged_j.sort(key=lambda j: j['timestamp'])

with open('MergedPosts.json', 'w') as f:
    simplejson.dump(merged_j, f, indent=1)

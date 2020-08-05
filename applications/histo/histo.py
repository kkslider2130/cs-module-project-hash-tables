# Your code here

import re
d = {}
story = open('robin.txt').read()


def word_count(s):
    # Your code here
    global d
    filtered_str = re.sub(r"[^\w\d'\s]", '', s)
    for word in filtered_str.lower().split():
        if word not in d.keys():
            d[word] = '#'
        else:
            d[word] += '#'

    return d


data = word_count(story)

for k in sorted(data, key=lambda k: len(data[k]), reverse=True):
    # print(k, "         ", data[k])
    print("{0:<20} {1:>20}".format(k, data[k]))

# for k, v in data.items():

#     print(k, ':', v)

import random

# Read in all the words in one go
words = open("input.txt", encoding='utf8').read()
words = words.split()


def make_pairs(words):
    for i in range(len(words)-1):
        yield(words[i], words[i+1])


pairs = make_pairs(words)
dic = {}
for word_1, word_2 in pairs:
    if word_1 in dic.keys():
        dic[word_1].append(word_2)
    else:
        dic[word_1] = [word_2]
start = random.choice(words)

while start.islower():
    start = random.choice(words)
chain = [start]
word_count = 100

for i in range(word_count):
    chain.append(random.choice(dic[chain[-1]]))


print(' '.join(chain))

"""
ask for a word
give back the count of every letter
"""
"""
beet
[['b', 1], ['e', 2], ['t', 1]]
{'b': 1, 'e':2 ...}
"""
counts = {}
word = input('gimme a word')
for ch in word:
    counts[ch] = counts.get(ch, 0) + 1

for k in counts:
    print(k, '-', counts[k])

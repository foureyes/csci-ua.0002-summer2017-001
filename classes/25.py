word = input('give me a word')

d1 = {}
"""
d1 = {letter:count}
d1 = {'b':1, 'e':2, 'p':1}
"""
for letter in word:
    if letter not in d1:
        d1[letter] = 1
    elif letter in d1:
        d1[letter] += 1
for letter in d1:
    print("{} x {}".format(letter, d1[letter]))


"""
ask this once...


give me a word
> beep
e x 2
b x 1
p x 1


(order doesn't matter)

...only requirement... is use a dictionary somehow in this program
"""

"""
part 0

Enter a phrase
> Happy Birthday! exclaimed the sad, sad kitten
GLAD birthday exclaimed the BLEAK BLEAK kitten

remove all punctuation from input
create a new "clean" phrase

go over every character in input phrase
    use can use ord, and if it's a letter, add it to the "clean" phrase
    alternatively, use isalpha ... if it's a space, add it back as well

isolate words by splitting it up into a list


put phrase back together again
"""

thesaurus = {"happy": "glad", "sad": "bleak"}

phrase = input('enter a phrase\n>')

cleaned = ''
#go over every character in input phrase
for letter in phrase:
    if letter.isalpha() or letter == ' ':
        cleaned += letter.lower()
    #alternatively, use isalpha ... if it's a space, add it back as well

words = cleaned.split(' ')
for i in range(len(words)):
    # check if current word is in our thesaurus
    if words[i] in thesaurus:
        # words[i] is a key
        # k = words[i]
        # words[i] = thesaurus[k]
        words[i] = thesaurus[words[i]].upper()

result = ' '.join(words)
print(result)
"""
words = ['happy', 'birthday', 'exclaimed' ...]
use words in thesaurus to replace each individual word in list words
for every word in list words
    if the word is a key in the thesaurus
        replace the word with the value in the thesaurus
print(cleaned)
"""
"""
how to add a key value pair to a dictionary
... how to get every line from a file
"""
file_object = open('some_file.txt', 'r')

for line in file_object:
    print(line)

"""
# gets the whole file as string
contents = file_object.read()
# then you'd have to split on newline
"""

"""
# takes every line and puts it into a list
line_list = file_object.readlines()
for line in line_list:
    print(line))
"""
file_object.close()











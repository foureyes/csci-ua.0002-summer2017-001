"""['boot', 'bat']"""
"""
def pluralize_all(words):
    for s in words:
        s = s + "s"
    return words
"""
"""
def pluralize_all(words):
    for s in words:
        s = s + "s"
        new_words.append(plural)
    return words
    """

def pluralize_all(words):
    new_words = []
    for s in words:
        plural = s + "s"
        new_words.append(plural)
    return new_words


#assert ['boots', 'bats'] == pluralize_all(['boot', 'bat']), 'test that s is added to every word'

#print(pluralize_all(['boot', 'bat']))

def more_characters_than(words, minimum):
    """go over word
       figure out if it's greater than the minimum
       add it to an entirely new list"""
    new_words = []
    for word in words:
        if len(word) > minimum:
            new_words.append(word)
    return new_words

print(more_characters_than(["zebra", "cow", "tiger"], 4))









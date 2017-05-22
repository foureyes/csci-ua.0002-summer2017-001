"""
1. ipo
2. tests
3. psuedocode
4. actual code
5. debug

input (paramaters): 1 parameter, a string
processing: puts a space between every *character*
output (return): another string
"""
def insert_spaces(s):
    """
    create a new a string
    go over every character in original string
      add character to new string
      add space to new string


    is it the last letter? if it is, don't add a space
    somehow ignore the last space / last letter
    """
    new_s = ''
    for letter in s:
        new_s += letter + ' '
    return new_s.strip()
print(insert_spaces('aaaah!'))
assert insert_spaces('aaaah!') == 'a a a a h !', 'inserts spaces between every character'
assert insert_spaces('evolve') == 'e v o l v e', 'first and last letter are the same'
#assert insert_spaces('a') == 'a', 'single character, no spaces inserted'
#assert insert_spaces('  ') == '   ', 'spaces are counted as character'
#assert insert_spaces('') == '', 'empty returns empty'






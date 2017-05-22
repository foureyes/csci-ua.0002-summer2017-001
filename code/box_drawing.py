"""
0 ****
1 ****
2 ****
3 ****
4 ****
"""
"""
01234
12345
** **
** **
** **
** **
** **
"""


# outer loop represents rows
drawing = ""
for row_num in range(5):

    row = ''

    for col_num in range(5):
        if col_num == 2:
            row += ' '
        else:
            row += '*'

    drawing += row + "\n"

print(drawing)
print(drawing)

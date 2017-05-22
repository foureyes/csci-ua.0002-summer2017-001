words = ['foo', 'bar', 'baz']
"""
#        0       1      2
#                len of words is 3.... 0, 1, 2
"""
for i in range(len(words)):
    if i < len(words) - 1:
        print(i, words[i], words[i + 1])
    else:
        print(i, words[i])
"""
i = 0 # first index 
for element in words:
    print(i, element)
    i += 1
"""
"""
numbers = [2, 4, 6]
numbers[0] += 1
numbers[1] += 1
numbers[2] += 1
print(numbers)
"""


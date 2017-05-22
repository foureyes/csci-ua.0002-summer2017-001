"""
doubled_swapped.py (6 points)
=====

Write the following 3 functions:

1. double_with_return
2. double_in_place
3. swap_first_with

double_with_return
-----
parameters: list to process
processing: create a new list by multipling each element in the original
            list by 2
return: the new list
example:

words1 = ['foo', 'bar', 'baz']
result = double_with_return(words1)
print(result)
# return value is new list: ['foofoo', 'barbar', 'bazbaz']
print(words1)
# remains the same: ['foo', 'bar', 'baz']


double_in_place
-----
parameters: list to process
processing: multipy each element in the original list by 2 (that is, the
            original list should be modified!)
return: no return value
example:
words2 = ['qux', 'corge', 'grault' ]
result = double_in_place(words2)
print(result)
# does not return anything: None
print(words2)
# original list is modified: ['quxqux', 'corgecorge', 'graultgrault']

swap_first_with
-----
parameters: list to process, index
processing: swap the first element with the element at the index 
            specified by the second argument. the original list should be
            changed.
return: no return value
example:

numbers = [2, 4, 6, 8, 10, 12, 14]
result = swap_first_with(numbers, 3)
print(result)
# no return value: None
print(numbers)
# [8, 4, 6, 2, 10, 12, 14]

"""

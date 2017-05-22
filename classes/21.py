"""

* 14 x assertions
* 12 x lists within lists, and looping over them
* 15 x come up with practice problems on the spot?

* 1 x create a module / using a module
* 8 x general practice problems #9 (unique and filter... lists)
"""

"""
* what's the exam, topics, etc.
* sorting ... like sorting strings (without sort method)
* repeated application of list methods
* a quick overview of functions again
* most likely going to have a list of methods on the exam
"""
"""
bubble sort 
-----
do this while there are more than zero swaps:
    for every element at each position <-- at each position means that ...
    compare adjacent values
    if greater, swap

7, 3, 2
3, 7, 2
3, 2, 7
"""
"""
add items
----
append <-- parameters? the value that you're adding... return value? None
insert <-- return? None
extend <-- return? None

get rid of items
----
* remove <-- None
* pop <-- does two things... removes last element *AND* returns that value
* (not a method) .. del 

misc
----
* sort <-- None
* count <-- count returns number of occurences
* index <-- returns first index of value
"""

"""
numbers = [1, 2, 3]
result = numbers.append(4) # <-- don't do this, and if you see this in 
#... there's likely an error
print(numbers)
print(result)


numbers = [1, 2, 3]
result1 = numbers.append(4) # <-- don't do this, and if you see this in 
numbers.extend([5, 6])
result2 = numbers.pop()
numbers.append([7, 8])

print(result1) # None
print(result2) # 6
print(numbers) # [1, 2, 3, 4, 5, [7, 8]]
"""

"""
assertions... we used them for tests

not exclusively used for tests, so they have a generic syntax

        is this condition is false, stop program, print out "description"
        |
       \/
assert some_condition, "description"
       /\
        |
        |
        anything that results in a boolean value

        when we test, we're interested in:
        * does the output of the function that we wrote match what we expect
        * if not, stop the program
"""

"""
def my_abs(number):
    return number

assert my_abs(5) == 5, "positive numbers give back positive numbers"
assert my_abs(-5) == 5, "negative numbers give back positive numbers"
"""
"""     /\           |___ expected
        |
        actual output
"""
"""
(0, 100)
(100, 100)
(100, 0)
(0, 0)
"""

"""
* move every x value by 50 (change every x value so that it's whatever the current is... plus 50
* use turtle to go to every coordinate
* create a n entrely new list, that has y values that aren't 0
"""
points = [[0, 100], [100, 100], [100, 0], [0, 0]]

for i in range(len(points)):
    points[i][0] += 50 
    points[i][1] += 50 
print(points)



























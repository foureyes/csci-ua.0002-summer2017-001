"""
Write a function called swappy:
* it has one parameter, a list
* it'll create an entirely new list (how?) that's copied from the list passed in
* it'll swap the first and second element of the new list
* if the list is less than two elements, it'll just give back the original list
* finally, its return value is the new list with the first and second element swapped
"""

"""
def swappy(my_list):
    # make a copy!
    new_list = my_list[:]
    # swap elements by using multiple assignment
    new_list[0], new_list[1] = new_list[1], new_list[0]
    return new_list 
print( swappy(['a', 'b', 'c']))
"""

"""
copying a list
(using slicing)
# slicing gives back an entirely new list (a sub list)
# some_list[0:len(some_list)]
# some_list[:] # <--- this makes a copy
(use an accumulator)
new_list = []
for element in some_list:
    new_list.append(element)

"""
"""
Write a function called average_point:

* it has one parameter, a list of lists
* each sub list represents a point on the coordinate plain, so each will be composed of two elements
* for example: [[0, 0], [5, 10]] … is a list of two points (0, 0) and (5, 10)
* it's going to create a new points (that is a list with two elements)... where x is the average of all of the x values, and y is the average of all y values
"""
def average_point(points):
    """
    keep track of total points
    sum of all x
    sum of all y
    ???
    go through every point in points
        index into 0 to get x
        index into 1 to get y
        accumulate into the sums
    ... divide sum x / total
    ... divide sum y / total
    use those values to create a new point (a single list of 2 elements)
    """
    total = len(points)
    sum_x = 0
    sum_y = 0
    for point in points:
        sum_x += point[0]
        sum_y += point[1]
    average_x = sum_x / total
    average_y = sum_y / total
    return [average_x, average_y]
    #return [sum_x / total, sum_y / total]
print(average_point([[2, 3], [3, 4], [5, 6]]))

"""

Using the same list of points (a list of lists) as the previous example, write a function called all_y:

    it should take a list of points as one parameter
    it should return a new list with only points where the y value is greater than the x value

"""
def all_y(points):
    new_points = []
    for point in points:
        if point[1] > point[0]:
            new_points.append(point)

    # TODO: this is wrong ... change
    return new_points

print(all_y([[2, 200], [3, 1], [4, 9]]))

"""
1. name
2. the kind of animal
3. how urgent is the problem

[['franz catka', 'cat', 1], ['jane pawston', 'dog', 99]]
"""






































































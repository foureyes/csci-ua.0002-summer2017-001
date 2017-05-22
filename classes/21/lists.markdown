---
layout: slides
title: Lists 
---
<section markdown="block" class="title-slide">
# Lists
{% include title-slide-footer.html %}
</section>


<section markdown="block">

### Sequences

We've seen __numeric__ types, like int, float and complex.  Another kind/classification of type is a __sequence__. A __sequence__:

* consists of an ordered collection of elements
* with each element identified by an index

Sequences support operations like:

* indexing to retrieve an element
* slicing to retrieve a subset of elements
* concatenation
* multiplication

</section>

<section markdown="block">
### Strings are Sequences

A __string__ is an ordered sequence of characters.  It is a __sequence__ type.  It supports:

{% highlight pycon %}
"blubbins?"[0] #index, first element -> "b" 
"blubbins?"[-1] #index, last element -> "?"
"blubbins?"[1:4] #slices -> "lub"
"blubbins?"[4:] #slices -> "bins?"
"what the " + "blubbins?" # concatenates -> "what the blubbins?"
"blubbins?" * 2 # repeats -> "blubbins?blubbins?"
{% endhighlight %}
</section>

<section markdown="block">
### Lists

A __list__ is another sequence type.  

* instead of characters, it's an ordered collection of __values__
* _any_ values!
* an example of a list of ints and strings

{% highlight python %}
# a list of ints
stuff = [1, "one", 2, "two"]
{% endhighlight %}
</section>

<section markdown="block">
### List Literals

Constructing a list using a list literal looks like this:
{% highlight python %}
["some", "stuff", "between", "brackets"]
{% endhighlight %}

* delimited by brackets... [1, 2, 3]
* each value is separated by a comma
* a list with no elements is an __empty list__ 
* an empty list is []
* again, mixed types are allowed (even other lists) - ['pie', 3, 3.14, ['apple', ['cherry']]
</section>

<section markdown="block">
### Printing Lists

You can pass lists directly to the built-in print function.  It will output the list as if it were a string literal: 

{% highlight pycon %}
>>> a = [2, 3, 5, 7]
>>> print(a)
[2, 3, 5, 7]
{% endhighlight %}

You can also use str() or string interpolation to create a string representation of a list:

{% highlight pycon %}
>>> a = [2, 3, 5, 7]
>>> print("Some numbers in a list: %s" % a)
Some numbers in a list: [2, 3, 5, 7]
{% endhighlight %}
</section>

<section markdown="block">
### Built-in List Operators and Functions

Because a __list__ is just another __sequence type__ many of the built-in operators and functions that work with strings behave similarly with lists.

* indexing operators
* iteration
* slicing
* comparison operators
* multiplication/addition
* len
</section>


<section markdown="block">
### Indexing Operations

__What will the following code output? &rarr;__

{% highlight python %}
import math
land_of_ooo = ["jake", "finn", "princess bubblegum"]
a = -1
print(land_of_ooo[0])
print(land_of_ooo[2])
print(land_of_ooo[a])
print(land_of_ooo[int(math.sqrt(1))])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
jake
princess bubblegum
princess bubblegum
finn
{% endhighlight %}
</div>

</section>


<section markdown="block">
### Indexing Operations Continued

__What will the following code output? &rarr;__

{% highlight python %}
import math
land_of_ooo = ["jake", "finn", "princess bubblegum"]
a = -1
print(land_of_ooo[3])
print(land_of_ooo[1.0])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers, not float
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Indexing Operations Continued Some More!

Using the list below, __How would you retrieve "homer"... once using a positive index, and another time using a negative index? &rarr;__

{% highlight python %}
simpsons = ["marge", "homer", "lisa"]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
simpsons[1]
simpsons[-2]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Indexing Operations Summary

* just like characters in a string, elements in a list can be accessed by their index (place)
* indexes start at 0 
* use the value (a variable, a list literial, etc) followed by the square brackets
* ... with the index enclosed: [1, 2, 3][0] &rarr; 1
* negative indexes start at the end of the list: [1, 2, 3][-1] &rarr; 3
</section>

<section markdown="block">
### Iterating Over a List

Just like iterating over a sequence of characters...

* you can use a for loop to iterate over a sequence of values in a list
* your loop variable contains the value of a list element
* that changes to the next element after each iteration

</section>

<section markdown="block">
### Iterating Over a List Example

__What will the following for loop print out? &rarr;__

{% highlight python %}
some_boolean_values = [True, True, False]
for b in some_boolean_values:
	print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
True
True
False
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slicing

Slicing also works on lists.  __What will the folloing code output? &rarr;__

{% highlight python %}
colors = ["red", "green", "blue", "taupe"]
print(colors[0:2])
print(colors[2:])
print(colors[:3])
print(colors[0:100])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['red', 'green']
{% endhighlight %}
{% highlight python %}
['blue', 'taupe']
{% endhighlight %}
{% highlight python %}
['red', 'green', 'blue']
{% endhighlight %}
{% highlight python %}
['red', 'green', 'blue', 'taupe']
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slicing Summary

Again... like slicing strings.

* use square brackets
* ...with start index and end index separated by a colon: [2, 3, 5, 7][1:3] &rarr; [3, 5]
* start and end can be omitted: [2, 3, 5, 7][:2] &rarr; [2, 3]
</section>


<section markdown="block">
### Equality Operators

Lists are compared lexicographically using comparison of corresponding elements; to be equal each element must compare equal and the two sequences must be of the __same type__ and have the __same length__.

__Equal or not equal?__ &rarr;

{% highlight python %}
print([1, 2, 3] == [1, 2, 3])
print(['a', 'b', 'c'] == [1, 2, 3])
print(['a', 'b', 'c'] != [1, 2, 3])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
True
{% endhighlight %}
{% highlight python %}
False
{% endhighlight %}
{% highlight python %}
True
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Greater Than, Less Than

If not equal, the sequences are ordered the same as their __first differing elements__. 

* comparing [1,2,'x'] and [1,2,'y'] is essentially just comparing 'x' and 'y'). 
	* [1, 2, 3] > [1, 2, 1, 2]
* if the corresponding element does not exist, the shorter sequence is ordered first 
	* [1,2] < [1,2,3]

__Equal or not equal?__ &rarr;

{% highlight python %}
['a', 'b', 1, 2] > ['b', 'b', 1, 2]
[5, 2] < [5, 2, 1]
['x', 'y', 'z'] < ['x', 'a', 'z']
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
False
{% endhighlight %}
{% highlight python %}
True
{% endhighlight %}
{% highlight python %}
False
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Addition and Multiplication

Multiplication and addition of lists are similar to the same operations on strings.  __What will the following code output? &rarr;__

{% highlight python %}
toppings = ["mushrooms", "peppers", "onions"]
numbers = [2, 3, 5, 7]
print(toppings + numbers)
print(toppings * 2)
print(numbers * 2)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
["mushrooms", "peppers", "onions", 2, 3, 5, 7]
["mushrooms", "peppers", "onions", "mushrooms", "peppers", "onions"]
[2, 3, 5, 7, 2, 3, 5, 7]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Addition and Multiplication Summary

* list concatenation 
	* __+__
	* adds the elements of one list to another list
	* [1, 2] + [3, 4] &rarr; [1, 2, 3, 4]
* list multiplication
	* __*__
	* repeats a list the given number of times
	* [1, 2] * 3 &rarr; [1, 2, 1, 2, 1, 2]
</section>

<section markdown="block">
### len()

You can still use the built-in function, len, on lists. __What do you think the following code will output? &rarr;__

{% highlight python %}
a = ["foo", "bar", "baz"]
b = []
c = ["foo", "bar", "baz", [1, 2, 3]]
print(len(a))
print(len(b))
print(len(c))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
3
0
4
{% endhighlight %}
</div>
</section>



<section markdown="block">
### Mutability

Unlike strings, however, lists are __mutable__.  That means that you can reassign a value at an index!  __What will the following code print out? &rarr;__

{% highlight python %}
>>> a = [3, 4, 5]
>>> a[0] = "surprise"
>>> print(a)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['surprise', 4, 5]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### List Methods

Lists are __objects__, and they have a slew of __methods__ that you can call on them.  However, because lists are mutable, many methods actually __change the list in place__!  Let's see how this differs from strings:

{% highlight python %}
>>> s = 'hello'
>>> s.upper()
'HELLO'
>>> print(s)
hello
{% endhighlight %}
{% highlight python %}
>>> numbers = [5, 3, 4]
>>> numbers.sort()
>>> print(numbers)
[3, 4, 5]
{% endhighlight %}
</section>

<section markdown="block">
### List Methods Continued

So.... why does this matter?

* most list methods modify the list __in place__
* most list methods __don't return a value__!
* that means... 
	* if you're getting __None__... 
	* you're probably assigning the return result of a list method to a variable

</section>



<section markdown="block">
### Some methods that you can call on lists

{% highlight python %}
li = [1, 2, 3]
{% endhighlight %}

* li.append(4) # appends element to end of list
* li.extend([3, 4]) # appends all items of one list to the other...
* li.insert(2, "asdf") # insert object before index
* li.remove(4) # removes first occurrence of...
* li.pop() # returns and removes the last element
* li.sort() # sorts list in place
* li.count(1) # returns number of occurrences of arg in list
* li.index(1) # returns the index of the element supplied
</section>

<section markdown="block">
### Adding Elements

1. __append__(_object_) - append object to end of list, even another list! 
2. __extend__(_iterable_) - appends all items of one iterable (list, string, etc.) to the list the method was called on
3. __insert__(_index_, _object_) - insert object before index

* use __append__ when you want the whole object added to the end of a list &rarr;
* use __extend__ when you want every element in another list added as an individual element to the original list &rarr;
* use __insert__ when you want to add an element to an arbitrary place in the original list &rarr;
</section>

<section markdown="block">
### Removing Elements

1. __remove__(object) - removes first occurrence of object in list
2. __pop__() - __returns and removes__ the last element, takes an optional argument to specify index

* use __remove__  for finding and removing an element &rarr;
* use __pop__ when you want to delete an element at a specific index (by default, the last element)... you also get the element removed as a return value! &rarr;
</section>

<section markdown="block">
### Miscellaneous Methods

1. __sort__() - sorts a list in place &rarr;
2. __count__(object) - counts the number of occurrences of object in the original list &rarr;
3. __index__(object) - returns the index of the object supplied; causes an error if the object doesn't exist &rarr;

</section>

<section markdown="block">
### Some Exercises

* make the last element in a list the first element
* filter a list of strings
* average
</section>

<section markdown="block">
### Make the First Element Last

* define a function called last_to_first
* it should take a list as an argument
* it should return a new list with the last element as the first element... and every element shifted up one 
	* last_to_first([1, 2, 3, 4] &rarr;
* if there's one element or less in the list, return the list as is
* use at least 3 assertions to test your last_to_first function
* try with just slicing and addition
* or try using pop and insert
</section>

<section markdown="block">
### Make the First Element Last Solution v1

{% highlight python %}
{% include classes/19/last_to_first.py %}
{% endhighlight  %}
</section>

<section markdown="block">
### Make the First Element Last Solution v2

{% highlight python %}
{% include classes/19/last_to_first_pop_insert.py %}
{% endhighlight  %}
</section>

<section markdown="block">
### Filtering a List

__Implement a function called more_characters_than: &rarr;__

* it will take a list of strings, called _words_, and an integer, called _min_, as an input
* it should return a list of strings 
* the resulting list will only have strings with more than _min_ characters
* it will return an empty list if an empty list is inputted
* ignore the case where a list has non-string types or if min is not an integer
* remember to use assertions

</section>

<section markdown="block">
### Filtering a List Example Output

{% highlight pycon %}
print(more_characters_than(["zebra", "cow", "tiger"], 4))
['zebra', 'tiger']
{% endhighlight %}
</section>

<section markdown="block">
### Filtering a List Solution

(btw, there's already a filter function in Python)

{% highlight python %}
{% include classes/18/more_characters_than.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Average

* define a function called average
* it should take a list of numbers as an argument
* it will return the average of the numbers in the list
* empty list will have an average of 0
* remember to use assertions
</section>

<section markdown="block">
### Implementing Average

{% highlight python %}
{% include classes/18/average.py %}
{% endhighlight %}

Using the built-in sum:

{% highlight python %}
def average(numbers):
	return sum(numbers) / len(numbers)
{% endhighlight %}
</section>

<section markdown="block">
### Looking for something?

Testing for membership within a list is similar to testing for a character in a string.  Use the __in__ operator.  It returns True if the operand on the left is an element in the list on right.  __What does the following code print out? &rarr;__

{% highlight python %}
print('c' in ['a','b', 'c'])
print('c' not in ['a', 'b', 'c'])

breakfast = ["oatmeal", "tofu scramble", "ramen"]
if "ramen" in breakfast:
	print("ramen for breakfast")
else:
	print("wise decision")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
True
False
ramen for breakfast
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Deleting List Items

You can delete list items using __del__ statement:  

* the __del__ statement is immediately followed by an indexed list or a list slice
* the value or values of the indexed list or list slice are removed from the original list

__What does the following code print out? &rarr;__

{% highlight python %}
vegetables = ["broccoli", "cauliflower", "brownie sundae", "carrot"]
del vegetables[2]
print(vegetables)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['broccoli', 'cauliflower', 'carrot']
{% endhighlight %}
</div>
</section>

<section markdown="block">
<h3>Strings to Lists and Back</h3>

There are two useful __string methods__ that are often used with lists:

* __split__ turns a string into a list based on a separator string
* __join__ turns a list into a string based on the string it's called on
* __what would the following code output? &rarr;__

{% highlight python %}
comics = "ranma,maison ikkoku,scott pilgrim"
awesome_comics_list = comics.split(",")
print(awesome_comics_list)
print(" and ".join(awesome_comics_list))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['ranma', 'maison ikkoku', 'scott pilgrim']
ranma and maison ikkoku and scott pilgrim
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Split and Join

__If I have the following list, how do I put together each element with an exclamation point and space between each element? How do I turn the resulting string back to a list? &rarr;__

{% highlight python %}
hello = ["Bill", "Phil", "Gil", "Jill"]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
names = "! ".join(hello)
print(names)
print(names.split("! "))
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Random - Choice, Shuffle

The random module offers some methods that can be used on lists:

* __choice__(my_list): retrieves a random item from the supplied list
* __shuffle__(my_list): randomly changes the order of the elements in the list passed in (_in place_)

__Let's try using a couple of these methods &rarr;__
{% highlight python %}
import random
numbers = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(numbers))
random.shuffle(numbers)
print(numbers)
{% endhighlight %}
</section>


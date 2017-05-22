---
layout: slides
title: Lists Review 
---
<section markdown="block" class="title-slide">
# Lists Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Sequences

__What's a sequence, and what are some operations and built-in functions that sequences support?__ &rarr;

<div class="incremental" markdown="block">
A __sequence__ is an ordered collection of elements.  Sequences support operations like:

* indexing to retrieve an element
* slicing to retrieve a subset of elements
* iteration to loop through every element
* concatenation and multiplication
* len()
</div>

</section>

<section markdown="block">
### Sequences Continued

We know two __sequence data types__.  __What are they?__ &rarr;

<div class="incremental" markdown="block">
* strings
* lists
</div>
</section>

<section markdown="block">
### Lists

__What's a list?  What elements are allowed in a list?__ &rarr;

<div class="incremental" markdown="block">
* it's an ordered collection of __values__
* _any_ values!
</div>
</section>

<section markdown="block">
### List Syntax

In code, __what's one way to create a list (as in, using a list literal), and how is an empty list represented?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
"""
a list is delimited by brackets, with each value separated by a comma
"""
items = ["some", "stuff", "between", "brackets"]

"""
an empty list is two square brackets - open and close
"""
an_empty_list = []
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Indexing and Slicing Operations

__How do we index into and slice out substrings of a list?__ &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> items = ['foo', 'bar', 'baz', 'qux']
>>> items[0]
'foo'
>>> items[1:3]
['bar', 'baz']
>>> 
{% endhighlight %}
</div>
</section>

<section markdown="block">
### About Indexes

__Speaking of indexes, what type should an index be (in both indexing and slicing)?__ &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> """ indexes are integers """
>>> items = [True, False, False]
>>> items[0]
True
>>> items[0.0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers, not float
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Indexing 

Given a list __items__, __what are three ways to retrieve the last element (operations, functions  and methods are valid)?__ &rarr;

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> items = [True, False, False]
>>> items[-1]
False
>>> items[len(items) - 1]
False
>>> items.pop()
False
{% endhighlight %}
</div>

</section>

<section markdown="block">
### An Aside on Pop

__By the way, name the two theings that pop does when called on a list.__ &rarr;

<div class="incremental" markdown="block">
* removes the last element of the list it is called on (_mutates_ it)
* returns a value, which is the value of the last element of the list that it is called on
</div>
</section>

<section markdown="block">
### Speaking of Mutability

__What will happen when the code below is executed?  Is anything printed out?  Is there an error?  Does _nothing_ happen?__ &rarr;

{% highlight python %}
items = [1, 2, 3]
items[0] = "boo!"
print(items)
{% endhighlight %}

<div class="incremental" markdown="block">
* lists are _mutable_
* consequently, ['boo!', 2, 3] is printed out
</div>
</section>


<section markdown="block">
### List of Lists 

Using the same list:

{% highlight python %}
stuff = [[9, 16, 25], ['a', 'b', 'c'], [[], "", None]]
{% endhighlight %}

* what indexing syntax would I use to get the letter 'b'?
* what line of code would I use to change None to 'something'? 

<div class="incremental" markdown="block">
{% highlight python %}
stuff[1][1]
stuff[2][2] = 'something'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Every Item in a List

__How can I continuously retrieve every item in a list, one item at a time?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
""" use a for loop """
for number in [24, 48, 12]:
	print "%s more hours to go!" % number

{% endhighlight %}
</div>
</section>

<section markdown="block">
### For Loops

__What is the value of the loop variable, number, during each iteration?__ &rarr;

{% highlight python %}
for number in [24, 48, 12]:
	print "%s more hours to go!" % (number)
{% endhighlight %}

<div class="incremental" markdown="block">
* 24
* 48
* 12
</div>
</section>

<section markdown="block">
### Nested Lists

__How do for loops work with nested lists?  What does this print out and what type is another\_list in each iteration?__ &rarr;

{% highlight python %}
stuff = [[9, 16, 25], ['a', 'b', 'c'], [[], "", None]]
for another_list in stuff:
	print another_list
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
""" another list is always a list in this case! """
[9, 16, 25]
['a', 'b', 'c']
[[], "", None]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Nested Lists Continued

__With the same list, how do I print out every element of every list on its own line with an exclamation point?__ &rarr;

{% highlight python %}
stuff = [[9, 16, 25], ['a', 'b', 'c'], [[], "", None]]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
for inner_list in stuff:
	for item in inner_list:
		print "%s!" % (item)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slicing

__What will the following slices return? &rarr;__

{% highlight python %}
numbers = [5, 11, 17, 19]
print(numbers[0:3])
print(numbers[2:])
print(numbers[:2])
print(numbers[0:100])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[5, 11, 17]
[17, 19]
[5, 11]
[5, 11, 17, 19]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slicing Returns a New Sub List, It Does Not Alter the Original List!

__What will the following slices print? &rarr;__

{% highlight python %}
nonsense = ['foo', 'bar', 'baz', 'qux']
print(nonsense[1:3])
print(nonsense)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['bar', 'baz']
['foo', 'bar', 'baz', 'qux']
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Comparison Operators


__What will the following code output?__ &rarr;

{% highlight python %}
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 6, 3]
d = [1, 6, 3, 2]

print(a != b)
print(b > c)
print(d > c)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
False
False
True
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Addition and Multiplication

__What will the following code output?__ &rarr;

{% highlight python %}
a = [1, 2, 3]
b = ['x', 'y', 'z']
print(a + b)
print(a * 3)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2, 3, 'x', 'y', 'z']
[1, 2, 3, 1, 2, 3, 1, 2, 3]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Length, Deletion and Membership 

What operators and/or functions would I use to (and how would I use them):

* __get the length of a list__ &rarr;
* __delete a list item__ &rarr;
* __determine if a value is a member (or a sublist) of another list__  &rarr;

</section>

<section markdown="block">
### Length, Deletion and Membership Continued

{% highlight python %}
>>> nonsense = ['foo', 'bar', 'baz', 'qux']

>>> len(nonsense)
4
{% endhighlight %}
{% highlight python %}
>>> del nonsense[0] 
>>> print(nonsense)
['bar', 'baz', 'qux']
>>> del nonsense[20]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
{% endhighlight %}
{% highlight python %}
>>> 'baz' in nonsense
True
{% endhighlight %}
</section>

<section markdown="block">
### List are (Mutable) Objects 

Lists are __objects__, and they have a slew of __methods__ that you can call on them.  However, because lists are __mutable__, many methods actually __change the list in place__!  Let's see how this differs from strings:

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
### Lists vs Strings

__Name as many differences between lists and strings as you can!__ &rarr;

<div class="incremental" markdown="block">
* syntax (brackets []s versus quotes ""s)
* mutability (strings are immutable, lists are mutable)
* strings a are a sequence of characters, lists are a sequence of any value
</div>
</section>

<section markdown="block">
### Back to Mutability

__Because lists are mutable, how do list methods typically work?  Do they return values?  Change the original object?__ &rarr;

<div class="incremental" markdown="block">
* most list methods modify the list __in place__
* most list methods __don't return a value__!
* if you're getting __None__...  you're probably assigning the return result of a list method to a variable
</div>
</section>

<section markdown="block">
### Adding Elements

__Name three methods that add elements to a list.  What does each method do?  What are each method's inputs and return value?__ &rarr;

<div class="incremental" markdown="block">
* __append__(_object_) - append object to end of list, even another list; returns None
* __extend__(_iterable_) - appends all items of one iterable (list, string, etc.) to the original list; returns None
* __insert__(_index_, _object_) - insert object before index; returns None
* (also __+__ operator)
</div>
</section>

<section markdown="block">
### Removing Elements

__Name two methods that delete elements from a list.  What does each method do?  What are each method's inputs and return value?__ &rarr;

<div class="incremental" markdown="block">
* __remove__(object) - removes first occurrence of object in list, causes an error if object doesn't exist; returns None
* __pop__() - __returns and removes__ the last element, takes an optional argument to specify index, causes an error if index is out of range
* (also __del__ operator)
</div>

</section>

<section markdown="block">
### Miscellaneous Methods

__Are there any other list methods that we know of?  What does each method do?  What are each method's inputs and return value?__ &rarr;

<div class="incremental" markdown="block">
* __sort__() - sorts a list in place; returns None
* __count__(object) - counts the number of occurrences of object in the original list; returns the count
* __index__(object) - returns the index of the object supplied; causes an error if the object doesn't exist; returns the index
</div>
</section>

<section markdown="block">
## [List Exercises](list_exercises.html)
</section>

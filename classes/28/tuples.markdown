---
layout: slides
title: Tuples Review 
---
<section markdown="block" class="title-slide">
# Tuples Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### What's a Tuple?  

__What's a tuple and how is it different from a list?__

<div class="incremental" markdown="block">
* a __tuple__ is an immutable grouping of data
* a __tuple__ is a sequence type
* it can be considered as an immutable list.  
	* you can't add items (no extend or append)
	* you can't remove items (no remove; del doesn't work)
	* you can't change items (assignment doesn't work)
* consequently, tuples can't be changed, unlike lists
</div>
</section>

<section markdown="block">
### Tuple Attributes

Tuples are:

* __ordered__ - elements are in a sequence
* __immutable__ - cannot be changed
* a __compound type__  
* a __sequence type__ 
</section>

<section markdown="block">
### Tuple Syntax

A tuple is a group of __comma separated values__.  A tuple literal is _just_ values and commas.  

{% highlight pycon %}
>>> dogs = "chihuahua", "pug", "chug"
>>> print(dogs)
('chihuahua', 'pug', 'chug')
{% endhighlight %}

{% highlight pycon %}
>>> birds = ("pelican", "owl", "pigeon")
>>> print(birds)
('pelican', 'owl', 'pigeon')
{% endhighlight %}
</section>

<section markdown="block">
### Tuples in String Formatting and Multiple Assignment

String formatting

{% highlight python %}
"I've %s this %s before!" % ("seen", "this")
{% endhighlight %}

Multiple assignment

{% highlight python %}
a, b, c = 1, 2, 3
{% endhighlight %}
</section>

<section markdown="block">
### Tuple Syntax and Function Parameters?

* Function parameters (both in definitions and when calling functions) are not tuples, even though they're comma separated 
* To __pass a tuple literal to a function use parentheses__ to prevent ambiguity

{% highlight pycon %}
>>> print(1, 2)
1 2
>>> print((1, 2))
(1, 2)
{% endhighlight %}

Even though parentheses are not required for tuples (again, it's the commas that matter), they are necessary in certain situations, such as passing a tuple to a function.  The extra parentheses help avoid ambiguity.
</section>


<section markdown="block">
### Tuple Operations, Functions and Methods

__What are some valid operations and functions that can be used with tuples?__

<div class="incremental" markdown="block">
Tuples support sequence operators and functions such as:

* concatenation (__+__), multiplication (__*__) - both return a tuple
* indexing (__[index]__) - returns value
* slicing (__[m:n]__) - returns a tuple
* iteration - you can loop over elements in a tuple
* length (__len__()) - returns length of tuple
* membership (__in__ and __not in__) - tests for membership in...
</div>
</section>

<section markdown="block">
### Tuple Operations, Functions and Methods Continued

__What are some operations, functions or methods that do not work with tuples?__


<div class="incremental" markdown="block">
Because tuples are immutable the following are not allowed or are not available:

* assignment
* append
* extend
* sort
* etc.
</div>
</section>


<section markdown="block">
### Tuple Operations and Functions Examples

Some operations:

{% highlight python %}
a = (1,2,3)
print(a + (4, 5, 6))
print(a[0])
print(a[:2])
print(len(a))
print(5 in a)
{% endhighlight %}


<div class="incremental" markdown="block">
{% highlight python %}
(1, 2, 3, 4, 5, 6)
1
(1, 2) # note that slicing a tuple returns a tuple!
3
False
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Iteration

Just like iterating over strings or lists.

{% highlight python %}
for value in (1, 2, 3):
	print(value)
{% endhighlight %}
</section>

<section markdown="block">
### Multiple Assignment / Unpacking

We've seen tuples before in multiple assignment

* if there is a tuple of variables on the left side
* and equal number of values in a tuple on the right side
* each value is bound to each variable in order 
* this is also called __tuple unpacking__

{% highlight python %}
a, b, c = 1, 2, 3
first_name, last_name = ("Timothy", "Tupleton")
{% endhighlight %}
</section>

<section markdown="block">
### Tuple Unpacking Examples

__What does this code output?__

{% highlight python %}
values = (1, 2, 3)
a, b, c = values
print(a)
print(b)

c, a, b = values
print(a)
print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
1
2
2
3
{% endhighlight %}
</div>
</section>

<section markdown="block">
### More Info About Multiple Assignment

Tuple unpacking is the most common way of performing multiple assignment... but the assignment operator is actually super flexible:

[More than you ever wanted to know about the assignment operator](http://docs.python.org/3.2/reference/simple_stmts.html#assignment-statements)
</section>

<section markdown="block">
### List of Tuples

A tuple within a list is retrieved as a single object, as with every other element in a list, when using our regular _for loop_variable in some_list_ syntax: 

{% highlight python %}
characters = [("Hiro", "Protagonist"), ("Yours", "Truly")]
for character in characters:
	print(character)
{% endhighlight %}

You get each actual tuple, so this prints out:

{% highlight python %}
('Hiro', 'Protagonist')
('Yours', 'Truly')
{% endhighlight %}
</section>

<section markdown="block">
### Lists of Tuples Continued

Again... __What's the type of person in every iteration?  How many iterations are there?  What does this print out?__


{% highlight python %}
smarties = [("Mr", "Smartypants"), ("Ms", "Knowitall")]
for person in smarties:
	print(person)
{% endhighlight %}

<div class="incremental" markdown="block">
* it's a tuple
* this loops twice
* it outputs:
{% highlight python %}
('Mr', 'Smartypants')
('Ms', 'Knowitall')
{% endhighlight %}
</div>
</section>

<section markdown="block">
### List of Tuples Continued Even More

Unpacking works in for loops as well!  Imagine that each element is retrieved from the outer list.  Each element is a tuple which can be unpacked into multiple loop variables.

{% highlight python %}
characters = [("Hiro", "Protagonist"), ("Yours", "Truly")]
for first, last in characters:
	print("first name is " + first)
	print("last name is " + last)
{% endhighlight %}
</section>

<section markdown="block">
### One Last List of Tuples Example 

{% highlight python %}
pairs_of_numbers = [(1, 2), (2, 3)]
for a, b in pairs_of_numbers:
	print(a + b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
3
5
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Returning Tuples

Tuples and tuple unpacking can provide a method of returning multiple values from a function. __What do you think this prints out?__

{% highlight python %}
def calculate_3d_point():
	result = (2, 4, 0)
	return result

x, y, z = calculate_3d_point()
print("the z coordinate is %s" % (z))
print("the x coordinate is %s" % (2))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
the z coordinate is 0
the x coordinate is 2
{% endhighlight %}
</div>
</section>

<section markdown="block">
### When To Use Tuples 

* some Python constructs use tuples (string formatting, multiple assignment)
* tuples are _write protected_
	* prevent an object from being changed
	* example: constants - values that never change... like origin = (0, 0)
* tuples are _faster_ than lists for some operations
* returning multiple values from a function
* semantics  
	* treat related data as a whole
	* example: points in a 2-dimensional plane
</section>


<section markdown="block">
## Some Tuple Exercises
</section>

<section markdown="block">
### Squares (Again)

* __What are two ways of programmatically drawing a square in turtle?__
* __What are some ways of representing a series of four x, y coordinates?__

<div class="incremental" markdown="block">
* there are a couple of ways to draw a square with turtle:
	* for loop and a combination of either left or right and forward or back
	* goto
* as literals, as separate variables... or as a tuple of tuples!
</div>
</section>

<section markdown="block">
### Drawing a Square, Tuples as Points

1. create a list of tuples that represent x, y coordinates of corners of a square
2. assume that the bottom left corner is at (0, 0), the upper right is (0, 50)
3. use a for loop and tuple unpacking to get each x, y value
4. within the for loop, use goto with your loop variables to draw the square

{% highlight python %}
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
# your code here!
wn.mainloop()
{% endhighlight %}
</section>

<section markdown="block">
### Turtles Using Tuples Solution 

{% highlight python %}
{% include classes/24/turtle_tuple_points.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Greetings

This exercise involves creating a list of tuples.  __Write a function called hello...__

* it should take a list of tuples as an argument
* assume that every tuple is three elements, with an honorific and a first and last name
* it should take each tuple and convert it into a string by:
	* starting with hello, and adding the first element with a period
	* adding the third element with an exclamation point
	* ("Mr", "Sam", "Smartypants") &rarr; Hello Mr. Smartypants
	* note that the first name is ignored
* the function should just print out each resulting string (no return value)

{% highlight python %}
smarties = [("Mr", "Sam", "Smartypants"), ("Ms", "Nelly", "Knowitall")]
hello(smarties)

Hello Mr. Smartypants!
Hello Ms. Knowitall!
{% endhighlight %}
</section>

<section markdown="block">
### Greetings Solutions

__We can do this a couple of ways...__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/25/smarties.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lists of Tuples Exercise Solutions

If we wanted to include the first name... we could use the code below because the operand to the right of a strim formatting operator is _actually_ __a tuple__! 

{% highlight python %}
# tuples can be used in string formatting as is!
def hello(t):
	for person in t:
		print("Hello %s. %s %s!" % (person))
{% endhighlight %}
</section>

<section markdown="block">
### Run Length Encoding

__Run length encoding__ is a simple method of compressing data by:

1. Finding sequences of the same element in the data
2. And converting those sequences to a number and a single element 
3. For example, "loook!!" would be encoded as "1l3o1k2!"
4. [The wikipedia article shows some examples](http://en.wikipedia.org/wiki/Run-length_encoding#Example)

__What's the run length encoded version of "cccaaabbb"?__

<div class="incremental" markdown="block">
3c3a3b
</div>
</section>

<section markdown="block">
### Encode!

__Let's write some pseudocode.  What are some ways to solve this?__


<div class="incremental" markdown="block">
{% highlight python %}
# keep track of the current letter
# keep track of the current letter count
# keep track of all previous letters and counts (what's a good data structure for this?)
# go through every letter in the string
# when we first see a letter, count it as 1, if we see it again, increment that count
# stop incrementing when we see another letter (reset values)
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  A Possible Solution

{% highlight python %}
{% include classes/25/rle.py %}
{% endhighlight %}
</section>

<section markdown="block">
## Review End
</section>

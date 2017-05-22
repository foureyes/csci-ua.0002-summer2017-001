---
layout: slides
title: Calling Functions 
---
<section markdown="block" class="title-slide">
# Calling Functions
{% include title-slide-footer.html %}
</section>


<section markdown="block">
## Let's Make Sure We're Speaking the Same Language!
</section>

<section markdown="block">
### A Function (Again)

__What's a function? &rarr;__

<div class="incremental" markdown="block">
* a __function__...
	* is a named sequence of statements that performs some useful operation 
	* may or may not take parameters (produce a value)
	* may or may not produce a result (return a value)
* a __method__ (also considered a function)...
	* a __function__ that's attached to an __object__ 
	* consequently, in context of an object, is interchangeable with __function__
</div>
</section>

<section markdown="block">
### Examples

__What are some examples of built-in functions or functions in modules? &rarr;__

<div class="incremental" markdown="block">
* built-in __functions__
	* print("something")
	* int("5")
	* intput("enter a number)
* __functions__ in modules
	* math.sqrt(5) 
	* sys.exit() 
</div>
</section>

<section markdown="block">
### Examples

__What are some examples of methods? &rarr;__

<div class="incremental" markdown="block">
So far we've only "officially" learned __methods__ that can be called on a Turtle __object__.  For example, if we have a Turtle called leo: 

* leo.up() 
* leo.forward(50)
* leo.right(90)
</div>
</section>


<section markdown="block">
### Calling a Function

__Define what it means to "call" a function.  How do we call a function?  &rarr;__

<div class="incremental" markdown="block">
A __function call__ is the statement that actually executes a function.  It causes the functions code to run.

Syntactically, we call a function by writing &rarr;:

1. the function name 
2. followed by parentheses
3. with zero or more arguments enclosed within those parentheses
4. (no arguments are ok)
</div>
</section>

<section markdown="block">
### Calling a Method

__Aaaaaaand... how is a method called?  &rarr;__

<div class="incremental" markdown="block">

1. the object name
2. follwed by a dot
3. followed by a function name 
4. followed by parentheses
5. with zero or more arguments enclosed within those parentheses
6. (no arguments are ok)
</div>
</section>

<section markdown="block">
### Arguments 

Based on the definitions of __function__ and __calling a function__, __how can we define argument? &rarr;__

<div class="incremental" markdown="block">
* an argument is a value provided to a function when the function is __called__
* this value (or values) is used within the function
* the argument can be the result of an expression which may involve operators, operands and calls to other functions!
* or simply, _the input_
</div>
</section>

<section markdown="block">
### Arguments / Parameters
What's the difference between an __argument__ and a __parameter__?

* for our purposes, they're the same: the values we pass in to a function (_input_)
* however...  THINKSCI makes a subtle distinction between the two:
	* __argument__: value provided to a function when it's called
	* __parameter__: name used inside a function to refer to the value which was passed to it as an argument
</section>

<section markdown="block">
###  Values and Expressions

Again, an __argument__ can be a __value__ or even an __expression__ (which can be reduced to a value anyway!):

{% highlight python %}
# (t is a Turtle object)

# using a value, 50, as an argument
t.forward(5) 

# using an expression as an argument
t.forward(20 / 4)

# another function that results in a value as an argument
t.forward(math.sqrt(25))
{% endhighlight %}
</section>

<section markdown="block">
### No Input vs Some Input

Some functions and methods require arguments, others don't. 

__Name some functions or methods that take arguments.  Name some that don't require arguments. &rarr;__


<div class="incremental" markdown="block">
* arguments
	* str(5)
	* random.randint(5, 12)
* no argument
	* t.up() # called on a Turtle object, t
	* sys.exit() # called using the sys module
</div>
</section>

<section markdown="block">
### Output / Return Value

Some functions and methods return values; others don't.

__Name some functions or methods that return a value.  Name some that don't. &rarr;__

<div class="incremental" markdown="block">
* returns a value
	* math.sqrt(25)
	* int("5")
	* input('foo')
* doesn't return a value
	* print("nothing to see here")	
	* t.up() # called using the sys module
</div>
</section>

<section markdown="block">
### When You Don't Have a Value

Actually... you do get a value if you call a function that doesn't actually return one!  

<div class="incremental" markdown="block">
* you get a special value called __None__.
* __None__ represents the absence of a value!

For example, assigning the result of print...

{% highlight pycon %}
>>> # print doesn't return a value...
... 
>>> result_from_print = print("foo")
foo
>>> print(result_from_print)
None
>>> 
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Some More About None 

__None__ is valid value in your code.  You can even bind it to a variable name:

{% highlight pycon %}
>>> an_empty_box = None
>>> print(an_empty_box)
None
{% endhighlight %}

* you may want to do this if you want to initialize a variable to _nothing_.  
	* usually, it's better to start with a more meaningful ininitial value
	* for example, if you're summing numbers, zero might make sense as a meaningful initial value
* you can also test for None (if an_empty_box is None:)
</section>

<section markdown="block">
### Return Values

You might have noticed that in one of the examples above, the result of the function was used like any other value.

* for example random.randint(1,6) returns an int
	* it _gives back_ an int
	* consequently it can be used in place of an int
* you can just treat a call to random.randint(1, 6) as a value

{% highlight python %}
# we've seen this (multiply a string by an int):
"hello" * 5

# but we can also do something like this:
"hello" * random.randint(1,6)
{% endhighlight %}
</section>


<section markdown="block">
### Return Values

Some more examples of using return values:

{% highlight python %}
# storing it in a varable
a = math.sqrt(4)

# using it directly in an expression
if math.sqrt(4) > 1 or math.sqrt(4) == 2:
	print("in here!")
{% endhighlight %}
</section>

<section markdown="block">
## Dissecting Some Function Calls

__What's the name of the function, the number of arguments, and the argument values of each function call below? Does the function call return a value? &rarr;__

{% highlight python %}
print("foo")
random.randint(1, 10)
range(10, 100, 2)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
print("foo") # print, 1 arguments, ("foo"), no return value
random.randint(1, 10) # randint, 2 arguments, (1, 10), returns an int
# range, 3 arguments, (10, 100, 2), returns a sequence of numbers
range(10, 100, 2) 
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Review
</section>

<section markdown="block">
### Definitions
* __function__ - named sequence of statements that performs some useful operation 
* __function call__ - the statement that actually executes a function
* __argument__ - a value that's passed in to a function when a function is called
* __None__ - a special value in Python that represents the absence of a value!
</section>

<section markdown="block">
## [Defining Your Own Functions](defining_functions.html)
</section>

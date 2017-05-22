---
layout: slides
title: Returning Values 
---
<section markdown="block" class="title-slide">
# Returning Values
{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Let's Make Sure We're Speaking the Same Language!
</section>

<section markdown="block">
### Functions and Methods (Again)

__What's a function, what's a method? &rarr;__

<div class="incremental" markdown="block">
* a __function__...
	* is a named sequence of statements that performs some useful operation 
	* may or may not take parameters (produce a value)
	* may or may not produce a result (return a value)
* a __method__ (also considered a function)...
	* a __function__ that's attached to an __object__ 
	* basically, a method is something that an object can do / an action that it can perform...
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

* __argument__: value provided to a function when it's called
* __parameter__: a variable in a function that receives an argument that’s passed
	* it's the name used inside a function to refer to the value that was passed to it as an argument
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
* no arguments
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
### Return Values

Even the result of calling input can be substituted as a value:

{% highlight python %}
# we've since this before:
n = int(input("please enter a number"))

# aaand, in some homeworks, I've even seen something like this ...
while input("Keep going? 'N' will stop") == 'N':
	print("Ok, fine!")
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
print("foo") # print, 1 arguments, ("foo"), returns None
random.randint(1, 10) # randint, 2 arguments, (1, 10), returns an int
# range, 3 arguments, (10, 100, 2), returns a sequence of numbers
range(10, 100, 2) 
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Quick Recap
* __function__ - named sequence of statements that performs some useful operation 
* __function call__ - the statement that actually executes a function
* __argument__ - a value that's passed in to a function when a function is called
* __None__ - a special value in Python that represents the absence of a value!
</section>

<section markdown="block" class="title-slide">
## Let's Look at Some Function Definitions
{% include title-slide-footer.html %}
</section>


<section markdown="block">
### Here's a Simple One...

{% highlight python %}
def greet_no_input():
	print("hello")
{% endhighlight %}

__What's the name of this function?  How many arguments do you think it takes?  What does the function do?__

<div class="incremental" markdown="block">
* greet_no_input
* no arguments!
* prints out hello
</div>
</section>

<section markdown="block">
### Another Function...

How about this one?  __What's the name of this function?  How many arguments do you think it takes, and what are they?  What does the function do?__

{% highlight python %}
def greet_with_input(greeting):
	print(greeting)
{% endhighlight %}

<div class="incremental" markdown="block">
* greet_with_input
* one argument, called greeting
* prints out whatever you pass in as greeting
</div>
</section>

<section markdown="block">
### Last One...

__What's the name of this function?  How many arguments do you think it takes, and what are they?  What does the function do?__

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)
{% endhighlight %}

<div class="incremental" markdown="block">
* greet_more_input
* two arguments: greeting and num
* prints out whatever you pass in as _greeting_, but _num_ times 
</div>
</section>


<section markdown="block">
### Function Definition

A few things to note:

1. defining a function doesn't call a function
2. you must explicitly call it __after__ it is defined...
3. (and related...) a function must be defined before it's called!
	* if you call it before you define it, you get an error
	* specifcally a NameError 
	* (similar to what happens when using an undeclared variable)
</section>

<section markdown="block">
### Function Definition Example 1:

__If this is the only code in your program, and you run it, what will be printed to the screen?  Something, nothing, or an error? &rarr;__
{% highlight python %}
def greet():
	print("hello")

greet()
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
hello
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Function Definition Example 2:

__If this is the only code in your program, and you run it, what will be printed to the screen?  Something, nothing, or an error? &rarr;__
{% highlight python %}
def greet():
	print("hello")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# nothing (the function was never called after it was defined)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Function Definition Example 3:

__If this is the only code in your program, and you run it, what will be printed to the screen?  Something, nothing, or an error? &rarr;__
{% highlight python %}
greet()

def greet():
	print("hello")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# we called the function before defining it
NameError: name 'greet' is not defined 
{% endhighlight %}
</div>
</section>

<section markdown="block">
## And Finally... Functions That Return Values

We've used some functions that return values, and we looked at them in an earlier set of slides.  __What type of values do the following functions give back? &rarr;__

* randint(1, 10)
* input("Enter a number")
* float(23)

<div class="incremental" markdown="block">
* int
* str
* float
</div>
</section>

<section markdown="block">
### What About the Functions We've Been Writing

If you assigned the result of one of the functions that we defined, what would get back? __What gets printed to the screen in the following program... and why? &rarr;__

{% highlight python %}
def greet(greeting, num):
	s = greeting * num
	print(s)

result_of_function = greet("hello", 5)
print(result_of_function)
{% endhighlight %}
</section>

<section markdown="block">
### That Functions That We Wrote Don't Return Anything!

The result from the previous slide would be:

{% highlight python %}
hellohellohellohellohello
None
{% endhighlight %}

* hellohellohellohellohello comes from the print in the function
* but None comes from the result of calling the function!
* it doesn't return anything, so we get None back
</section>

<section markdown="block">
### Returning Values

* we can create _fruitful_ functions, that is... _value returning_ functions
* just use the keyword __return__, followed by the value that you want to give back
* here's our previous example rewritten so that rather than printing out the new greeting, it returns a string

{% highlight python %}
def greet(greeting, num):
	s = greeting * num
	return s
{% endhighlight %}
</section>

<section markdown="block">
### So, Now What?

Now that you have a function that returns a value, you can use that function wherever you would use that value.

{% highlight python %}
def greet(greeting, num):
	s = greeting * num
	return s

# using the return value of greet as an argument to input!
response = input(greet("hi", 3))
print(response)
{% endhighlight %}
</section>

<section markdown="block">
### The return Statement

* the __return__ immediately stops the execution of a function
* ...and returns the value that follows it
	* the value can be any value!
	* it can even be an expression
</section>

<section markdown="block">
### Some Examples of the Return Statement

These functions are contrived examples of what you can do with return.  __What type and value do they return? &rarr;__

{% highlight python %}
def foo():
	return "foo"

def bar():
	return "b" + "ar"

def baz():
	return str(math.sqrt(100)) + "!"
{% endhighlight %}

<div class="incremental" markdown="block">
* string, "foo"
* string, "bar"
* string, "10!"
</div>
</section>

<section markdown="block">
### Let's Try Creating a Function That Returns a Value

__Write a function that returns the area of a circle (&pi;r&sup2;)when given a radius, r.&rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
import math
def area(r):
	a = math.pi * r * r
	return a
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Area, Defined Again

Another way to define our area function:

{% highlight python %}
import math
def area(r):
	return  math.pi * r * r
{% endhighlight %}

* code is shorter 
* but no intermediary variable (maybe more difficult to debug?) 
</section>

<section markdown="block">
### Print vs Return

__What's the difference between printing in a function and returning a value from a function? &rarr;__

{% highlight python %}
def greet(greeting, num):
	s = greeting * num
	print(s)

def greet(greeting, num):
	s = greeting * num
	return s
{% endhighlight %}
</section>

<section markdown="block">
### Print vs Return Continued

What's the difference between printing in a function and returning a value from a function?  

* __printing alone will not give you back a value for a function!__  
* however, you can print __and__ return
	* useful for debugging
	* see the example below... where we print out what s is before returning it

{% highlight python %}
def greet(greeting, num):
	s = greeting * num
	print(s)
	return s
{% endhighlight %}
</section>


<section markdown="block">
### Stopping Execution

The return statement stops execution of your function immediately.  __What gets printed in the following example? &rarr;__

{% highlight python %}
def foo():
	print("one")
	print("two")
	return "foo"
	print("three")

foo()
{% endhighlight %}
<div class="incremental" markdown="block">
"one" and "two" are printed, but three is not because the function has already returned the value "foo"
</div>
</section>

<section markdown="block">
### Another Example...

Stopping execution again...

{% highlight pycon %}
>>> def area(r):
...   a = math.pi * r * r
...   print("before return")
...   return a
...   print("after return")
... 
>>> area(6)
before return
113.09733552923255
{% endhighlight %}
</section>

<section markdown="block">
### Multiple Return Statements

You can have multiple return statements in your function!  __Write a function that calculates absolute value using multiple return statements. &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
def absolute_value(x):
	if x >= 0:
		return x
	else:
		return x * -1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Multiple Return Values

You can return more than one value by:

* using return with a comma separated list of values
* in conjunction with multiple assignment

__What do you think this prints out?__ &rarr;

{% highlight python %}
def two_things():
	return "two", "things"
a, b = two_things()
print(b, a)
{% endhighlight %}

<div class="incremental" markdown="block">
</div>
</section>

<!--
<section markdown="block">
## [Some Exercises](exercises.html)
</section>
-->


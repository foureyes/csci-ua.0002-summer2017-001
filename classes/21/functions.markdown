---
layout: slides
title: Functions 
---
<section markdown="block" class="title-slide">
# Functions 
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Function Definition

__What's a function?__

<div class="incremental" markdown="block">
A __function__ is a named sequence of statements that performs some _useful_ operation
</div>
</section>

<section markdown="block">
### Method Definition

__What's a method (well... in the context of programming, of course!)?__

<div class="incremental" markdown="block">
A __method__ is an action that an object/_thing_ can do.  It's basically a function that's attached to an object. 
</div>
</section>

<section markdown="block">
### Function Call Definition

__What's a function call?__ 

<div class="incremental" markdown="block">
A __function call__ is the statement that actually executes a function.  It's just the function's name followed by parentheses, with zero or more arguments within those parentheses.
</div>
</section>

<section markdown="block">
### Argument Definition

__What's an argument (again, in the context of functions, of course)?__ 

<div class="incremental" markdown="block">
An __argument__ is a value that's passed in to a function when a function is called.  It's the input!
</div>
</section>


<section markdown="block">
### None Definition

__What's None?__

<div class="incremental" markdown="block">
__None__ is a special value in Python that represents the absence of a value.
</div>
</section>

<section markdown="block">
### Function Definition

What's the syntax for defining a function?

<div class="incremental" markdown="block">
{% highlight python %}
def <function_name>(<zero_or_more_parameters>):
	<statement #1>
	<statement #2>
	.
	.
	<etc.>
	# an optional return statement
	return <some value>
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Return

What does __return__ do?

<div class="incremental" markdown="block">
* it's a statement that immediately stops the execution of a program
* and returns the value that is immediately after it
</div>
</section>

<section markdown="block">
### Return Continued

__What's value is given back if a function doesn't return anything?__

<div class="incremental" markdown="block">
__None__ 
</div>
</section>

<section markdown="block">
### Parameters Example

__Using the following function and function call, what are the values of both greeting and num within the function? What's the output?&rarr;__

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	return s

import math
print(greet_more_input("hello".upper() * 2, int(math.sqrt(4))))
{% endhighlight %}

<div class="incremental" markdown="block">
* greeting &rarr; "HELLOHELLO"
* num &rarr; 2
* output &rarr; HELLOHELLOHELLOHELLO
</div>
</section>

<section markdown="block">
### And The Tricky One

__Using the following function and function call, what are the values of both greeting and num within the function? What's the output?&rarr;__

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	return s

num = "yo"
greeting = 1
print(greet_more_input(num, greeting))
{% endhighlight %}

<div class="incremental" markdown="block">
* greeting &rarr; "yo"
* num &rarr; 1
* output &rarr; "yo"
</div>
</section>

<section markdown="block">
### Another Parameters Example
{% highlight python %}
{% include classes/16/join_three_strings.py %}
{% endhighlight %}

__What are the values of a, b and c in the above function when called as below:&rarr;__
{% highlight python %}
join_three_strings('one', 'two', 'three')
{% endhighlight %}
{% highlight python %}
join_three_strings('three', 'one', 'two')
{% endhighlight %}
{% highlight python %}
a = 'three'
b = 'two'
c = 'one'
join_three_strings(c, b, a)
{% endhighlight %}

<div class="incremental" markdown="block">
* a = 'one', b = 'two', c = 'three'
* a = 'three', b = 'one', c = 'two'
* a = 'three', b = 'two', c = 'one'
</div>
</section>

<section markdown="block">
### Parameters Summary
* __parameters__ 
	* variable names used within a function 
	* reference the values passed in as arguments
* parameters are positional; order determines what names match to what variables
	* def f(p1, p2, p3):
	* p1 will refer to the first value passed in
	* p2 to the second
	* etc.
</section>

<section markdown="block">
### Accessing a Variable Outside of a Function 

__What do you think will happen here?  Will something be printed out?  Nothing?  Or an error?__

{% highlight python %}
{% include classes/15/scope1.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
Oddly... it's fine.  Something is printed out.  It seems like the function has access to s, which was declared outside of the function. 
</div>
</section>

<section markdown="block">
### How About Variables Declared Inside a Function?

__What do you think will happen here?  Will something be printed out?  Nothing?  Or an error?__

{% highlight python %}
{% include classes/15/scope2.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
Uh-oh.  Looks like you can't access variables that are inside a function.
</div>
</section>

<section markdown="block">
### How About Parameters?

__What do you think will happen here?  Will something be printed out?  Nothing?  Or an error?__

{% highlight python %}
{% include classes/15/scope2b.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
This is the same as the previous slide.  You can't access the parameters (by their name) that you passed in to the function from outside of the function.
</div>
</section>

<section markdown="block">
### And Lastly... 

__What do you think will happen here?  Will something be printed out?  Nothing?  Or an error?__

{% highlight python %}
{% include classes/15/scope3.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
Hmmm... it looks like names created within a function are _local_ to that function.  They don't override names in the global space.
</div>
</section>

<section markdown="block">
### What Does This All Mean?

A __scope__ holds the current set of available names (variables) and the values that they point to.  

* anything that we define in the top level of indentation our program is said to be in the __global scope__
* in the following example, the variables _a_ and _b_ are in the __global scope__
* they can be accessed from anywhere, even within the function

{% highlight python %}
a, b = 25, "something"

def foo():
	c = "bar"
	print(b)
	print(c)
# what will this print out?
foo()
{% endhighlight %}
</section>

<section markdown="block">
### Scope

Variables that are defined in your function (one indentation level in), however, are only available within your function.  They are _local_ to that function.  The example below won't work.

{% highlight python %}

def foo():
	c = "bar"
	return c

print(c)
{% endhighlight %}
</section>

<section markdown="block">
### Scope Continued

Furthermore, variables that are declared within a function that have the same name as a global variable are totally different variables/values!  They don't overwrite the outer, global variable (there's a way to do this, though).  What will this print?

{% highlight python %}
c = "on toast"
def foo():
	c = "grape jelly"
	print(c)

foo()
print(c)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
grape jelly
on toast
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Scope Summary

* variables declared outside of a function can be accessed within a function
* variables declared inside of a function cannot be accessed outside of a function (they're __out of scope__)
* parameters in a function cannot be accessed outside of a function either
* variables declared within a function don't override those declared outside of a function
</section>



<section markdown="block">
### Return Values
__What's the difference between these two definitions of our function?  What gets printed out for each code sample? &rarr;__

Version #1

{% highlight python %}
{% include classes/16/join_three_strings.py %}
print(join_three_strings('one', 'two', 'three'))
{% endhighlight %}

Version #2

{% highlight python %}
{% include classes/16/join_three_strings_no_return.py %}
print(join_three_strings('one', 'two', 'three'))
{% endhighlight %}
</section>

<section markdown="block">
### Return Values Continued
The first definition (#1) returns a string, while the other (#2) doesn't return a value.  Here are the values that are returned from functions #1 and #2:

1. 'one two three'
2. None

Note however, that the actual output is: 

{% highlight python %}
# version 1
one two three

# version 2 (the print within the function gets executed, followed by the
# print outside of the function)
one two three
None
{% endhighlight %}
</section>

<section markdown="block">
### The Return Statement
* a function can return a value after it is called
* this is done by using the __return__ statement
* the __return__ statement immediately stops the execution of a function
* ...and returns the value that follows it 
	* the value can be any value! (return True)
	* it can even be an expression (return 1 + 1)
* if a function doesn't explicitly return a value, it gives back __None__, a special value that means the absence of a value
</section>

<section markdown="block">
### Defining a Function vs Calling a Function
__What gets printed out for each version of code?__
{% highlight python %}
# version 1
{% include classes/16/join_three_strings.py %}
{% endhighlight %}
{% highlight python %}
# version 2
{% include classes/16/join_three_strings.py %}
join_three_strings('one', 'two', 'three')
{% endhighlight %}
{% highlight python %}
# version 3
{% include classes/16/join_three_strings.py %}
print(join_three_strings('one', 'two', 'three'))
{% endhighlight %}
<div class="incremental" markdown="block">
1: nothing, 2: nothing, 3: 'one two three'
</div>
</section>

<section markdown="block">
### Testing Programs / Functions
So far, we've tested our programs by:

* printing things out to the screen
* manually inspecting the output
* ...for every test case that we have

Some shortcomings of manual testing

* it's tedious!
* it's error prone!

__What can we do to make testing less tedious and error prone? &rarr;__
</section>

<section markdown="block">
### Assertions for Testing

Let's get the computer to test it for us!  Assertions are a way to systematically check the state of our program.

* we can test _expected_ values against the _actual_ values by using an __assert__ statement
* the __assert__ statement will program execution if if a specified condition is __not True__
* for testing, that condition is _expected_ value == _actual_ value
</section>

<section markdown="block">
### Assert Syntax

{% highlight python %}
assert <some condition>, "a string representing a test"
{% endhighlight %}

1. the keyword __assert__
2. followed by any condition - an expression that returns True or False (usually expected == observed)
3. followed by a comma
4. followed by a string that represents the test 
</section>

<section markdown="block">
### An Assertion Example

__Let's use assertions to test an incorrect implementation of our function - one that doesn't have spaces between the strings. &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/16/join_three_strings_with_asserts.py %}
{% endhighlight %}

{% highlight python %}
# output shows line number and error...
Traceback (most recent call last):
  File "foo.py", line 4, in <module>
    assert "ha ha ha" == join_three_strings("ha", "ha", "ha"), "joined string should have spaces"
AssertionError: joined string should have spaces
{% endhighlight %}
</div>
</section>

<section markdown="block">
### An Assertion Example That Actually Passes

__Let's fix the program... and see what happens. &rarr;__

{% highlight python %}
{% include classes/16/join_three_strings_with_asserts_with_fix.py %}
# results in no output
{% endhighlight %}
</section>

<section markdown="block">
### Another Assertion Example

__Let's use assertions to test an incorrect implementation of an absolute_value function &rarr;__
{% highlight python %}
def absolute_value(x):
	if x >= 0:
		return x
	else:
		return -1
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
assert 1 == absolute_value(-1), "absolute value of negative # is positive"
assert 1 == absolute_value(1), "absolute value of positive # is same #"
assert 0 == absolute_value(0), "absolute value of 0 is 0"
{% endhighlight %}

</div>
</section>

<section markdown="block">
### Questions About Assertions
* why use assertions
	* to test specific portions of your program
	* to cut down on manual testing
	* they're almost like inline documentation for your functions
* why use assertions over if statements
	* you can actually _turn off_ assertions when you run your program
	* more concise than if statements
	* specifically meant for checking the internal state of your program </section>
</section>

<section markdown="block">
### Example Question #1

* write a function called join_three_strings
* it should take three arguments: a, b, c
* it should return a single string composed of a, b, and c __separated__ by a space
* handle non-string arguments (see last example)
* use at least two assertions to test

Example Usage:

{% highlight pycon %}
>>> print(join_three_strings('one', 'two', 'three'))
one two three
>>> print(join_three_strings('1', '2', '3'))
1 2 3
>>> print(join_three_strings(1, 2, 3))
1 2 3
{% endhighlight %}
</section>

<section markdown="block">
### Example Question #1 Solution
{% highlight python %}
{% include classes/16/join_three_strings.py %}
assert "one two three" == join_three_strings('one', 'two', 'three'), "three strings are joined with a space"
assert "1 2 3" === join_three_strings(1, 2, 3), "joins three ints as strings"
{% endhighlight %}
</section>

<section markdown="block">
### Example Question #2 

__Using the function definition below, what is the value and type of _a_? &rarr;__

{% highlight python %}
{% include classes/16/join_three_strings.py %}
a = join_three_strings(4, 'five', 6)
{% endhighlight %}

<div class="incremental" markdown="block">
* "4 five 6"
* string
</div>
</section>

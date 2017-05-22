---
layout: slides
title: Returning Values 
---
<section markdown="block" class="title-slide">
# A Little More About Returning Values
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### The return Statement

The __return__ statement does two things!

1. immediately stops the execution of a function
2. ...and returns the value that follows it
	* the value can be any value!
	* it can even be an expression
</section>


<section markdown="block">
### Functions that Return Values

* functions can give back values
* that is, when they're evaluated, they yield a value
	* abs(-5) gives back &rarr; the integer, 5
	* str(200) gives back &rarr; the string, "200"
* these functions can be used as values because they give back a value when evaluated
</section>

<section markdown="block">
### None

If you do not specify a return value for your function, it will return __None__.

* __None__ is the absence of a value
* the example below shows a function that gives back None

{% highlight python %}
def add_two_fives():
	# not returning anything, nope!
	result = 5 + 5

num = add_two_fives()
print(num)
{% endhighlight %}
</section>

<section markdown="block">
### Area of a Circle

This function:

* takes one parameter, the radius
* gives back the area of a circle using __return__

{% highlight python %}
import math
def area(r):
	a = math.pi * r * r
	return a
{% endhighlight %}
</section>

<section markdown="block">
### Outputting to the Screen vs Returning a Value (Part 1)

<aside>What's the difference between printing within a function and returning a value from a function?</aside> 

* __What gets printed to the screen? &rarr;__
* __What value is stored in the variable called greeting? &rarr;__

{% highlight python %}
def say_hello():
	print("hello")

greeting = say_hello()
{% endhighlight %}

<div class='incremental' markdown='block'>
* __"hello"__ is printed
* the value, __None__, is in greeting
</div>
</section>

<section markdown="block">
### Outputting to the Screen vs Returning a Value (Part 2)

* __What gets printed to the screen? &rarr;__
* __What value is stored in the variable called greeting? &rarr;__

{% highlight python %}
def say_hello():
	return "hello"

greeting = say_hello()
{% endhighlight %}

<div class='incremental' markdown='block'>
* nothing gets printed
* the string, __"hello"__, is in greeting
</div>
</section>

<section markdown="block">
### Outputting to the Screen vs Returning a Value (Part 3)

* __What gets printed to the screen? &rarr;__
* __What value is stored in the variable called greeting? &rarr;__

{% highlight python %}
def say_hello():
	print("hello")
	return "hello"

greeting = say_hello()
{% endhighlight %}

<div class='incremental' markdown='block'>
* __"hello"__ gets printed
* the value, __"hello"__, is in greeting
</div>
</section>

<section markdown="block">
### Outputting to the Screen vs Returning a Value (Part 4)

<aside markdown="block">
Last one... _really_
</aside>
__What gets printed to the screen? &rarr;__

{% highlight python %}
def say_hello():
	print("hello")

greeting = say_hello()
print(greeting)
{% endhighlight %}

<div class='incremental' markdown='block'>
{% highlight python %}
hello
None
{% endhighlight %}
</div>
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
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
before return
113.09733552923255
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Multiple Return Statements

You can have multiple return statements in your function!  Here's an implementation of absolute value:

{% highlight python %}
def absolute_value(x):
	if x >= 0:
		return x
	else:
		return x * -1
{% endhighlight %}
<!--_-->
</section>

<section markdown="block">
### Just Return

We usually see return statements followed by the value being returned.  However, a return statement can be written without any value:

* without a value, return stops the execution of the code in the function
* it gives back __None__ 



</section>

<section markdown="block">
### Just Return Continued

__What does the following program output?__ &rarr;
{% highlight python %}
def give_back_nothing():
	return

result = give_back_nothing()
print('give_back_nothing returns:', result)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
give_back_nothing returns: None
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Just Return Another Example

Here's an example of using a bare return to bail out of the function if the input is incorrect:

{% highlight python %}
def velocity(distance, time):
	if time == 0:
		return
	
	v = distance / time
	return v
{% endhighlight %}

</section>

<section markdown="block">
## [IPO Charts and Functions Exercises](exercises.html)
</section>

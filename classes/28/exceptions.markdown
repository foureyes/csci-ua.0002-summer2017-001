---
layout: slides
title: Exceptions Review 
---
<section markdown="block" class="title-slide">
# Exceptions Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Exceptions

Errors that occur during runtime are called __exceptions__.
</section>

<section markdown="block">
### Exceptions in the Wild

__What are some exceptions that we've seen?  That is, what errors have occurred during runtime?__ 

<div class="incremental" markdown="block">
* using an out of range index on a list or string that's
* dividing by zero
* using an undefined variable
* using an operator on incompatible types
* converting a value to a type that it can't be converted to
* __Let's try to cause some exceptions!__
</div>
</section>

<section markdown="block">
### Exception Examples

{% highlight pycon %}
Traceback (most recent call last):
  File "/tmp/exceptions.py", line 1, in <module>
    5 / 0
ZeroDivisionError: integer division or modulo by zero

Traceback (most recent call last):
  File "/tmp/exceptions.py", line 1, in <module>
    int("foo")
ValueError: invalid literal for int() with base 10: 'foo'

Traceback (most recent call last):
  File "/tmp/exceptions.py", line 2, in <module>
    print(a[3])
IndexError: list index out of range

Traceback (most recent call last):
  File "/tmp/exceptions.py", line 1, in <module>
    "foo" + 5
TypeError: cannot concatenate 'str' and 'int' objects
{% endhighlight %}
</section>

<section markdown="block">
###  A Closer Look at a Runtime Error
{% highlight python %}
Traceback (most recent call last):
  File "/tmp/exceptions.py", line 1, in <module>
    "foo" + 5
TypeError: cannot concatenate 'str' and 'int' objects
{% endhighlight %}

We see the following details:

* which file caused the exception
* the line number
* the actual code that caused it
* the kind of exception / error plus some additional details
</section>

<section markdown="block">
### Types of Exceptions 

A list of [all exception types](http://docs.python.org/3.2/library/exceptions.html) can be found at: [http://docs.python.org/3.2/library/exceptions.html](http://docs.python.org/3.2/library/exceptions.html)

The base exception is just Exception, but there are specific ones after that.  From the previous slides, and our past experience programming, some exceptions we've seen include:

* ZeroDivisionError
* IndexError
* TypeError
* NameError
* ValueError
</section>

<section markdown="block">
### What do all of These Errors Mean!?

* ZeroDivisionError
* IndexError
* TypeError
* NameError
* ValueError


<div class="incremental" markdown="block">
* ZeroDivisionError - divide by zero
* IndexError - index out of range
* TypeError - function or operation applied to inappropriate type
* NameError - name (variable, function, etc) doesn't exist / not yet declared
* ValueError - function or operation gets right type, but inappropriate value
</div>
</section>

<section markdown="block">
### So Many Exceptions

The root Exception, and the other exception types that follow from it is called an __exception hierarchy__
</section>

<section markdown="block">
### Exception Handling

There's a construct in most programming languages that lets you handle exceptions.  In python, that construct is a __try-except__ block.  It's similar to an if-else:

{% highlight python %}
try:
	# stuff that I want to do
except:
	# stuff to do if an error occurs
{% endhighlight %}
</section>

<section markdown="block">
### try-except

The __try__ block watches out for any statements within that block that causes errors.

If there is an error, the code in the __except__ block will be run. 
</section>

<section markdown="block">
### try-except Example 1

__What is the output of this code?__

{% highlight python %}
a = [1, 2, 3]
try:
	print(a[100])
except:
	print("sorry, try another!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
sorry, try another!
{% endhighlight %}
</div>
</section>

<section markdown="block">
### try-except Example 2

__What is the output of this code?__

{% highlight python %}
a = [1, 2, 3]
try:
	print(a[0])
except:
	print("sorry, try another!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Feet to Inches

In the following program, non numeric input (for example, typing in 'hello') will cause the program to crash (this is because of a ValueError exception!  __Modify the program using try-except to deal with non-numeric input.__

{% highlight python %}
inches = input("gimmeh some inches\n>")
print(float(inches)/12)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
inches = input("gimmeh some inches\n>")
try:
    print(float(inches)/12)
except:
    print("don't do that")
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Other Exceptions

In the previous program, using __try-except__ allowed the program to gracefully handle a __ValueError__.  __Can that exception happen in the following program?  Are there any other exceptions (that were mentioned in earlier slides) that can happen?__

{% highlight python %}
people = input("how many people are eating pizza?\n>")
print("Each person can have %s slices" % (8/int(people)))
{% endhighlight %}
<div class="incremental" markdown="block">
* ValueError - for non numeric input
* ZeroDivisionError - for 0 as input
</div>
</section>

<section markdown="block">
### Fixing the Pizza Pie Problem

__How do we fix it (original code below)?__

{% highlight python %}
people = input("how many people are eating pizza?\n>")
print("Each person can have %s slices" % (8/int(people)))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
people = input("how many people are eating pizza?\n>")
try:
    print("Each person can have %s slices" % (8/int(people)))
except:
    print("No one's gettin' nuthin'")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Fixing the Pizza Pie Problems Continued

What if we want to deal with ValueErrors and ZeroDivisionError differently?

Say either:

1. That's not a number! (ValueError)
2. More for me! (ZeroDivisionError)
</section>

<section markdown="block">
### Specific Exceptions, Multiple Except Blocks

You can catch specific exception types, and add an arbitrary number of except blocks for every exception type that may occur.

{% highlight python %}
try:
	# some tricky stuff
except NameOfErrorType1:
	# handle it gracefully
except NameOfErrorType2:
	# handle it gracefully too
{% endhighlight %}
</section>

<section markdown="block">
### Back to Pizza

Dealing with multiple exceptions...

{% highlight python %}
people = input("how many people are eating pizza?\n>")
try:
    print("Each person can have %s slices" % (8/int(people)))
except:
    print("No one's gettin' nuthin'")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
people = input("how many people are eating pizza?\n>")
try:
    print("Each person can have %s slices" % (8/int(people)))
except ZeroDivisionError:
    print("More for me!")
except ValueError:
    print("That's not a number!")
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Implement Three Card Monte

Here's a text version of [three card monte](http://en.wikipedia.org/wiki/Three-card_Monte).

{% highlight python %}
pick a cup: 0, 1, or 2
>0
['.', 'o', 'o']
you win

pick a cup: 0, 1, or 2
>0
['o', '.', 'o']
you lose

pick a cup: 0, 1, or 2
>asdf
['.', 'o', 'o']
not a number
you lose

pick a cup: 0, 1, or 2
>400
['o', '.', 'o']
that cup doesn't exist
you lose
{% endhighlight %}
</section>

<section markdown="block">
### Three Card Monte Requirements

* in our version, we're using "cups"
* keep a penny under 1 cup
* represent the three cups as a list
* 'o' for empty '.' for a penny
* "shuffle" the list
* ask for input... a number that's 0, 1, or 2
* if the program gets non-numeric input, say that it's not a number
* if the number causes an IndexError, say that the cup doesn't exist
* if either exception occurs, the player loses
* if the user finds the penny, the player wins
</section>

<section markdown="block">
###  A Potential Solution

{% highlight python %}
import random
cups = ['o', '.', 'o']
random.shuffle(cups)
n = input("pick a cup: 0, 1, or 2\n>")
result = None

print(cups)
try:
    result = cups[int(n)]
except IndexError:
    print("that cup doesn't exist")
except ValueError:
    print("not a number")

if result == ".":
    print("you win")
else:
    print("you lose")
{% endhighlight %}
</section>

<section markdown="block">
## Review End
</section>

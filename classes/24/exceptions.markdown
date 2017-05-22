---
layout: slides
title: Exceptions 
---
<section markdown="block" class="title-slide">
# Exceptions
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
* these all correspond to an _exception_ __Let's try to cause some!__ &rarr;
</div>
</section>

<section markdown="block">
### Types of Exceptions 

The base or _generic_ exception is just called __Exception__.  [However there are many other exceptions](http://docs.python.org/3.2/library/exceptions.html) that follow from this base Exception.

__Here are the ones that we just saw__ &rarr;

<div class="incremental" markdown="block">
* __ZeroDivisionError__ - divide by zero
* __IndexError__ - index out of range
* __TypeError__ - function or operation applied to inappropriate type
* __NameError__ - name (variable, function, etc) doesn't exist / not yet declared
* __ValueError__ - function or operation gets right type, but inappropriate value
</div>
</section>

<section markdown="block">
### In Case There's an Error...

* python actually allows you to gracefully recover from from exceptions!
* __let's take a look at why we'd want to do this__ &rarr;
</section>

<section markdown="block">
### A Short Program

Let's write a simple  __interactive program__ that __converts inches to feet__:

* __ask the user for numeric input__ - some number of inches
* __accept decimal values as well__, such as 1.5 inches
* __divide that number by 12__ to get feet
* print out the result

<div class="incremental" markdown="block">
{% highlight python %}
inches = input("inches\n>")
print(float(inches)/12)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Soooo... That Works Great

Let's try running the program...

Everything works fine until?  __Is there a certain kind of input that will cause an error in this program?__

<div class="incremental" markdown="block">
{% highlight python %}
inches
>asdf
Traceback (most recent call last):
  File "foo.py", line 2, in <module>
    print(float(inches)/23)
ValueError: invalid literal for int() with base 10: 'asdf'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Can We Prevent This Error from Happening?

__...Maybe!  Let's try a couple of things.__ &rarr;

<div class="incremental" markdown="block">
How about isdigit and isnumeric?

{% highlight python %}
s = 'asdf'
print(s.isdigit())
print(s.isnumeric())
{% endhighlight %}

But they don't let legitimate input through!

{% highlight python %}
s = '3.2'
print(s.isdigit())
print(s.isnumeric())
{% endhighlight %}

</div>
</section>

<section markdown="block">
### "Defensive Programming" Continued

__Are there any other ways to allow strings like 3.2 in, but still prevent strings that are not composed of numbers and a decimal point?__ &rarr;

<div class="incremental" markdown="block">
* loop through every character, and make sure that it's only a number or a decimal point!?
* use find to check for decimal; create another string without that and check if it's a digit
* _ughhhh_ ... nevermind, these all seem a bit clunky
</div>
</section>

<section markdown="block">
### EAFP

Sometimes it's...

<strong>E</strong>asier to <strong>A</strong>sk <strong>F</strong>orgiveness than <strong>P</strong>ermission

* instead of defensive programming...
* let's just try it
* and ask for forgiveness if we made a mistake
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

* The __try__ block watches out for any statements within that block that causes errors.
* If there is an error, the code in the __except__ block will be executed. 
* Otherwise, the code will execute normally, and the except block will be ignored

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
### Let's Take Another Look at Our Conversion Program

__Let's modify our program so that it behaves in a similar way, but uses try-except instead of testing with an if statement first.__

{% highlight python %}
inches = input("inches\n>")
print(float(inches)/12)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
inches = input("inches\n>")
try:
    print(float(inches)/12)
except:
    print("don't do that")
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Other Exceptions

We saw that we could handle a ValueError in our program.  __Can that exception happen in the following program?  Are there any other exceptions (that we just talked about in an earlier slide) that can happen?__ &rarr;

{% highlight python %}
# of slices in a pie
people = input("how many people are eating pizza?\n>")
print("Each person can have %s slices" % (8/int(people)))
{% endhighlight %}
<div class="incremental" markdown="block">
* ValueError - for non numeric input
* ZeroDivisionError - for 0 as input
</div>
</section>

<section markdown="block">
### Fixing the Pizza Pie Problems 

__How do we fix it (original code below)?__ &rarr;

{% highlight python %}
# of slices in a pie
people = input("how many people are eating pizza?\n>")
print("Each person can have %s slices" % (8/int(people)))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# of slices in a pie

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

__So... let's apply that to our pizza program__ &rarr;

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

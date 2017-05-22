---
layout: slides
title: Built-in Modules Review 
---

<section markdown="block" class="title-slide">
# Modules Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### First, Built-In Functions!

Before we went into modules, we _briefly_ looked at a few more built-in functions.  __What were they &rarr;__

<div class="incremental" markdown="block">
* __abs__(x) - returns a number that is the absolute value of x
* __len__(s) - returns the length of a sequence type (such as a string) as an int
* __round__(x [,digits]) - round a number to a given precision in decimal digits (default 0 digits)
* __dir__([object]) - returns a list of names in a module or in the current namespace
* more here: [http://docs.python.org/py3k/library/functions.html](http://docs.python.org/py3k/library/functions.html)
</div>

</section>

<section markdown="block">
### Modules
<aside>Even more functionality can be found in <em>modules</em></aside>

__What's a module? &rarr;__

<div class="incremental" markdown="block">
* just a file containing Python definitions and statements intended for use in other Python programs
* __modules__  _provide standardized solutions for many problems that occur in everyday programming_
* they help organize the standard library by grouping together related functionality (for example, all math related functions)
</div>
</section>

<section markdown="block">
### The Modules That We're Familiar With

__We learned about three modules.  What are they, and what are some functions and constants that they contain? &rarr;__

<div class="incremental" markdown="block">
* __math__: pi, sqrt(n), floor(n), ceil(n), sin(n), cos(n), tan(n)
* __random__: random(), randint(a, b)
* __sys__: version, exit()
</div>
</section>

<section markdown="block">
### Using Functions and Constants in Modules

__Let's write a program that:&rarr;__

* prints the squareroot of 18671041
* generates and prints a random number between 1 and 100

<div class="incremental" markdown="block">
{% highlight python %}
import math
import random
n = math.sqrt(18671041)
print(n)
m = random.randint(1, 100)
print(m)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Import and the Dot Operator

We use the keyword, __import__, followed by the __name of the module__ to bring in a module.

{% highlight python %}
import math
import random
import sys

print(math.pi)
print(random.random())
sys.exit()
{% endhighlight %}
</section>


<section markdown="block">
### The Import Statement

When you use the import statement...

{% highlight python %}
import math
{% endhighlight %}

* all of the code in the module is executed
* which makes all of the definitions (variables, functions, etc.) in the module available to you by using:
	* the __module name__
	* followed by the __dot operator__
	* followed by a __function call__ or a __variable name__
</section>


<section markdown="block">
### The math Module

* math
	* __pi__ - a constant that contains the value of pi&rarr; 
	* __floor__(x) - returns the smallest integer less than or equal to x&rarr;
	* __ceil__(x) - returns the smallest integer greater than or equal to x&rarr;
	* __sqrt__(x) - returns the square root of x&rarr;
	* __cos__(x) - returns the cosine of x radians &rarr;
	* __sin__(x) - returns the sine of x radians &rarr;
	* __tan__(x) - returns the tangent of x radians &rarr;
</section>

<section markdown="block">
### The random and sys Modules
* random
	* __random__() - return a random float that's between 0 and 1
	* __randint__(a, b) - returns a random int that's a <= n <= b
* sys
	* __exit__([arg])_ - exits form python
	* __version__ - a constant that contains the version of Python
</section>


<section markdown="block">
### Rationale for Modules

Modules are used:

* to encourage code reuse (DRY - don't repeat yourself)
* to provide "namespacing" to avoid naming collisions
* to provide a way of organizing code
</section>

<section markdown="block">
### Behind the Scenes
<aside>A Closer Look at Modules</aside>
What happens when we import?

* the name of the module actually corresponds to a python file
* Python looks in the current working folder (as well as several other locations) for a file named after the module your importing
* imagine placing the contents of that file directly into the file you're working on (at the point of the import statement)
</section>

<section markdown="block">
### An Example Module

In fact, we can make our own modules!  We'll take a look at this later, but to illustrate how modules work, we can create two files in the same directory:

* my_awesome_module.py
* hello.py

{% highlight python %}
print(d1)
# my_awesome_module.py
print("inside my_awesome_module")
x = 42

# hello.py
import my_awesome_module
print("hello")
print(my_awesome_module.x)
{% endhighlight %}
</section>

<section markdown="block">
### An Example Module Continued

__What do you think will be output when we run hello.py? &rarr;__

<div class="incremental" markdown="block">

{% highlight python %}
inside my_awesome_module
hello
42
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Um... So Where Are All of Those Other Modules?
<aside markdown="block">
They're Definitely _Not_ in the Current Directory
</aside>

Where do sys, math, random, and other modules come from?  If modules are just files, we should just be able to find them!

* the current directory
* _or_ a list of specified directories called the __PYTHON_PATH__
* location usually varies by system and version...
</section>

<section markdown="block">
### Where Was That?

For example, on __OSX Mountain Lion__ and __Python 3.3__, you may be able to find modules in:

{% highlight python %}
# for me, it's here:
/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/

# for you, maybe somewhere in....
/System/Library/Frameworks/Python.framework/Versions/ ...
{% endhighlight %}

</section>

<section markdown="block">
### Why Do Modules Exist?

That's great, but why bother with using and/or creating modules (aside, of course, from bringing in additional built-in functionality)?

* they encourage code reuse (DRY - don't repeat yourself)
* they provide "namespacing" to avoid name collisions
* they provide a way of organizing code
</section>

<section markdown="block">
### Three Modules Out of ??? / HALP!

There are many more modules to explore.  Check out the [official documentation](http://docs.python.org/py3k/library/index.html) for a more comprehensive list.  You'll find modules like:

* tkinter - for graphical user interfaces
* turtle - a pen-plotter like drawing library
* wave - for reading/writing WAVE (audio files)
* http.server - a simple Python web server
* and so on...
</section>

<section markdown="block">
### HALP!!!
To find help on these modules:

* the first place to look is obvs the [official documentation](http://docs.python.org/py3k/library/index.html) 
* you can also check out the python docs in IDLE (go to Help&rarr;Python Docs)
* you can fiddle around in the interactive shell
		* dir()
		* help()

{% highlight pycon %}
>>> help(abs)
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> a = "foo"
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']
>>> import math
>>> dir(math)
{% endhighlight %}
</section>

<section markdown="block">
### How About a Practical Application, PLZ?

__Rewrite our guess number game so that it uses a random number instead of a hardcoded one. It should display the correct answer after you guess.&rarr;__

{% highlight pycon %}
# Run 1:
Guess a number between 1 and 10!
> 5
Nope, I was thinking of 10.

# Run 2:
Guess a number between 1 and 10!
> 8
You guessed right; I was thinking of 8.
{% endhighlight %}

</section>


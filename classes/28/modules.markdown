---
layout: slides
title: Modules 
---
<section markdown="block" class="title-slide">
# Modules
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Built-in Modules

__What are some modules we've used, and what do they do? &rarr;__

<div class="incremental" markdown="block">
* math
* random
* sys
* turtle
</div>
</section>

<section markdown="block">
### The math Module

* math
	* __pi__ - a constant that contains the value of pi&rarr; 
	* __floor__(x) - returns the smallest integer less than or equal to x&rarr;
	* __ceil__(x) - returns the smallest integer greater than or equal to x&rarr;
	* __sqrt__(x) - returns the square root of x&rarr;
	* __cos__(x) - returns the cosine of x radians &rarr;
</section>

<section markdown="block">
### The random Module
* random
	* __random__() - return a random float that's between 0 and 1&rarr;
	* __randint__(a, b) - returns a random int that's a <= n <= b&rarr;
	* __choice__(list) - chooses a random element from a list
	* __shuffle__(list) - shuffles a list in place
</section>

<section markdown="block">
* sys
	* __exit__([arg])_ - exits form python&rarr;
	* __version__ - a constant that contains the version of Python&rarr;
</section>
<section markdown="block">
* turtle
	* __Turtle__() - constructor that creates a turtle object
		* __forward__(n)
		* __up__()
		* __goto__()
		* etc
	* __Screen__() - constructor that creates a screen object
</section>




<section markdown="block">
### Creating a Module

We can actually create our own modules.

* a __module__ is just a file!
* we can import everything that we've written
* you can import functions and variables from an existing file
	* __make sure that both files are in the same directory__
	* use the __import__ statement
	* the module name is the __file name without the .py__ extension
</section>

<section markdown="block">
### Creating a Module Example

__Create 2 files: greetings.py and using_a_module.py &rarr;__

{% highlight python %}
#greetings.py
def hello():
	return "hi there"
{% endhighlight %}

{% highlight python %}
#using_a_module.py
import greetings
print(greetings.hello())
{% endhighlight %}

Run it!
</section>

<section markdown="block">
### Some Questions

__What would happen if you didn't have an import? &rarr;__
__What would happen if you put in the extension of your file name? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
Traceback (most recent call last):
  File "/tmp/using_a_module.py", line 1, in <module>
    print(greetings.hello())
NameError: name 'greetings' is not defined

Traceback (most recent call last):
  File "/tmp/using_a_module.py", line 1, in <module>
    import greetings.py
ImportError: No module named py
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Why Create Your Own Modules?

What's the motivation for creating your own modules? 

<div class="incremental" markdown="block">
* organizing your code
	* keep related code together
	* prevent source code from being long and unwieldy
* code reuse
	* use your module in other programs
	* share your module with others!
</div>
</section>

---
layout: slides
title:  Making Modules 
---

<section markdown="block" class="title-slide">
# Making Modules
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Modules

* a __module__ is just a file!
* ...a file with Python code in it
* __what are some modules that we've used? &rarr;__

<div class="incremental" markdown="block">
* random
* math
* turtle
</div>
</section>

<section markdown="block">
### Creating a Module

We can actually create our own modules.

* again, it's just a file...
* we can actually import everything that we've written!
* so... you can import functions and variables from a file that you've written
	* make sure that both files are in the same directory
	* use the import statement
	* the module name is the file name without the .py extension

</section>

<section markdown="block">
### Creating a Module Example

__Try this on your own... create 2 files: greetings.py and using_a_module.py &rarr;__

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

* organizing your code
	* keep related code together
	* prevent source code from being long and unwieldy
* code reuse
	* use your module in other programs
	* share your module with others!
</section>

<section markdown="block">
## [Exercises](exercises.html)
</section>


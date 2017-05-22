---
layout: slides
title: Review 
---
<section markdown="block" class="title-slide">
# print("hi")
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### A First Program
<aside>"Hello world!"</aside>
* "Hello world!" is traditionally the [first program you write when learning a new language](http://en.wikipedia.org/wiki/List_of_Hello_world_program_examples)
* simply outputs "Hello world!"

Follow these steps:

1. create a new file (File &rarr; New Window)
2. type in:	__print("Hello world!")__
3. run your program (Run &rarr; Run Module)
	* you will be prompted you to save your file
	* save your file as hello.py (make sure you keep the .py extension!)

<details>
</details>
</section>

<section markdown="block">
## Let's Take a Closer Look at "Hello World" ...

{% highlight python %}
print("Hello world!")
{% endhighlight %}
</section>

<section markdown="block">
### SPACE!
* notice there's no space prior to __print__
* Python is __whitespace significant__
	* whitespace matters
	* it mostly matters at the beginning of lines
	* indentation specifies the beginning and end of a group of lines of code
	* interior spacing usually doesn't matter
* this will work &rarr;
{% highlight python %}
print  (      "Hello world!")
{% endhighlight %}
* this won't &rarr;
{% highlight python %}
        print("Hello world!")
{% endhighlight %}
* we'll see more about spacing in our next class
</section>

<section markdown="block">
### Print

* print is a built-in __function__
* __what's a function?__ &rarr;

<div class="incremental" markdown="block">
* a function is a bunch of code that gets executed whenever the name of the function is _called_
* it's a black box that does _something_
* similar to functions you've seen in math
	* it may have parameters (inputs)
	* it can return a value (output)
	* though it doesn't necessarily have to have parameters or return values
</div>
</section>

<section markdown="block">
### Print Continued
* __print__ is a built in function... that will output whatever you give it to the console followed by a __new line__
* you can tell it's a built-in function because it's highlighted (purple)
* if you start typing it and open parentheses, you get a hint &rarr;
	* notice - it can take more than one parameter or argument!
	* you can give print multiple parameters by separating them with a comma; all parameters will be printed out separated by a space &rarr; 
{% highlight python %}
print("Hi", "there")
{% endhighlight %}
</section>

<section markdown="block">
### A Quick Note About Functions
* we will go into the rest of the hint when we cover functions
* for now we're just interested in calling functions
* you call a function by 
	* typing the function's name 
	* open parentheses 
	* any __arguments__ (that is, values that you use as input for the function), separated by commas
	* close parentheses
{% highlight python %}
a_function_name("argument 1", 2, 3.0)
{% endhighlight %}
</section>

<section markdown="block">
### A String
* the one argument that we pass to the __print__ function  is __"Hello world!"__
* this is called a __string__...
* it's just a sequence of characters
* note that it's surrounded by quotes!
</section>

<section markdown="block">
### One Last Look...
* a function named __print__
* being called with exactly one __argument__
* the one argument is a __string__:
{% highlight python %}
print("Hello world!")
{% endhighlight %}
</section>

<section markdown="block">
### A Reminder About a Neat Trick

Again... as mentioned previously, you can use __help__(_thing_) in the __interactive shell__ to show information about built-in functions and other Python features:

{% highlight pycon %}
>>> help(print)
{% endhighlight %}
</section>

<section markdown="block">
### Some More New Stuff
<aside>For the remainder of this class:</aside>
* we'll talk a little more about strings and other __types__ of __values__
* comments
* the operations that you can use on those types
* variables
* user input
* design, input, processing and output
</section>

<section markdown="block">
## [Let's Move on to Values and Data Types](values-and-types.html)
</section>


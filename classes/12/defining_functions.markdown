---
layout: slides
title: Defining Functions 
---
<section markdown="block" class="title-slide">
# Defining Functions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Some Quick Examples...
</section>

<section markdown="block">
### We Can Define Our Own Functions!
<aside>Yes, Actually.</aside>

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
### We Can Define Our Own Functions (Continued)!

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
### We Can Define Our Own Functions (Continued Some More)!

... Aaaand this one?  __What's the name of this function?  How many arguments do you think it takes, and what are they?  What does the function do?__

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
### Defining a Function - Syntax

__Based on our examples, let's figure out how we define a function:__

<div class="incremental" markdown="block">
{% highlight python %}
def <function_name>(<zero_or_more_parameters>):
	<statement #1>
	<statement #2>
	.
	.
	<etc.>
{% endhighlight %}
</div>
</section>

<section markdown="block">
### The Header Line
<aside>A Closer Look</aside>

The beginning of a function consists of:

1. the keyword, __def__ (this never changes)
2. followed by the function's name
	* (whatever you want, but something meaningful)
	* same rules for variable names apply (alphanumeric and underscores)
3. parentheses surrounding parameters (if any)
	* can just be () if no parameters are required
	* multiple parameters are separated by commas
	* the parameters specify what information must be provided to the function
4. lastly, a colon to signify the end of the header line
</section>

<section markdown="block">
### Parameters

A __parameter__ is "a name used inside a function to _refer_ to the value which was passed to it as an argument".

* sometimes we'll use __parameter__ and __argument__ interchangeably
* note that whatever value you pass in to the function, you can now refer to it within the body using the parameter's name
* we'll take a look at this in a little bit...
</section>

<section markdown="block">
### Function Body

The __body__ of a function:

* consists of one or more statements
* the values that were passed in as arguments in the call to the function:
	* can be accessed by the parameter names
	* these names correspond to the position that they were in when the function was called
</section>

<section markdown="block">
### ...And Back to Parameters

Let's see what that means. Whatever values you pass in to the function, you can now refer to it within the body using the parameter's name (based on the position of the argument).

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

greet_more_input("hello", 5)
{% endhighlight %}
</section>

<section markdown="block">
### Parameters Example 1:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

greet_more_input("hola", 23)
{% endhighlight %}

<div class="incremental" markdown="block">
* greeting &rarr; "hola"
* num &rarr; 23
</div>
</section>

<section markdown="block">
### Parameters Example 2:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

greet_more_input("hey " + "there", math.sqrt(25))
{% endhighlight %}

<div class="incremental" markdown="block">
* greeting &rarr; "hey there"
* num &rarr; 5
</div>
</section>

<section markdown="block">
### Parameters Example 3:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

num = "hi"
greeting = 20
greet_more_input(num, greeting)
{% endhighlight %}

<div class="incremental" markdown="block">
* greeting &rarr; "hi"
* num &rarr; 20
</div>
</section>

<section markdown="block">
### Let's Take a Closer Look

{% highlight python %}
#                    num       greeting
#                      |        |
#                    "hi"      20
#                      |        |
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

num = "hi"
greeting = 20
greet_more_input(num, greeting)
{% endhighlight %}
</section>

<section markdown="block">
### Function Definition

The entire block of code you wrote, the header and the body of the function, is called the __function definition__.  Here are a few things to note about your function definition:

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
### Program Flow

What we've seen so far:

* statements are executed from top to bottom
* each line is executed exactly once


</section>

<section markdown="block">
### Program Flow Coninued

Defining our own functions means:

* still top to bottom, so we have to define the function first
* but once a function is called... 
	1. go to function
	2. execute that code
	3. go back to where function was called
* the body of a function can be executed as many times a function is called
</section>

<section markdown="block">
### Program Flow Example

__Let's walk through this program line-by-line &rarr;__

{% highlight python %}
def exclaim(word, num):
	punctuation = num * '!'
	s = word + punctuation
	print(s)

print("hello")
exclaim("hi", 1)
print("hey there")
exclaim("howdy", 10)
{% endhighlight %}

[Example Run in Python Tutor](http://www.pythontutor.com/visualize.html#code=def+exclaim(word,+num)%3A%0A++++punctuation+%3D+num+*+'!'%0A++++s+%3D+word+%2B+punctuation%0A++++print(s)%0A%0Aprint(%22hello%22)%0Aexclaim(%22hi%22,+1)%0Aprint(%22hey+there%22)%0Aexclaim(%22howdy%22,+10)&mode=display&cumulative=false&py=2&curInstr=0)

</section>

<section markdown="block">
### Using a Main Function

Sometimes you'll see a function called main() within a program

* this signifies that this is the _main_ line of execution
* all of the code for the program is written in that function
* the last line of the code calls that function
* the rationale for doing this is to:
	* keep your code organized
	* isolate your function definitions from the actual program (handy when creating modules)
* we'll see this a bit more later...
</section>

<section markdown="block">
### Main Function Example

{% highlight python %}
def exclaim(word, num):
	punctuation = num * '!'
	s = word + punctuation
	print(s)

def main():
	name = input("What's your name?\n>")
	greeting = "hi %s" % (name)
	exclaim(greeting, 5)

main()
{% endhighlight %}
</section>


<section markdown="block">
## [Returning Values](returning_values.html) ("fruitful functions")
</section>

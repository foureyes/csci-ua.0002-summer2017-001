---
layout: slides
title: String Objects, String Methods, Built-Ins
---
<section markdown="block" class="title-slide">
# String Objects, String Methods, Built-Ins
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Objects

We're going to be talking about __objects__ ... _alot_. (And probably even more so, if you continue to 101, 102, etc.).

So, in the context of programming, an __object__ is:

* a _thing_ that a variable name can refer to, like a string, or a range of numbers
* ...in fact, all of the values in Python are things
* "hello" is a str object, 42 is an int object
* an __object__ can have __attributes__ ...data associated with an object
* an __object__ can have __methods__ ...which are basically things that the object can do
</section>

<section markdown="block">
### Methods

* a __method__ is essentially a function that's associated with a particular object
* you can _call_ a method just like a function... but you have to use the dot operator
* object.method() - it's similar to using a method in a module!
* for example: "hello".upper() 
* ...means I'm calling the upper() function on a str object
* in fact... we can see some methods on objects that we've used before!

{% highlight python %}
dir("hello")
{% endhighlight %}
</section>

<section markdown="block">
### Strings as Objects!

So, strings have some methods.  __Let's try them out! &rarr;__

(remember, you call methods on objects themselves)

1. upper() 
2. lower()
3. isdigit()
4. find(s)
5. others - use dir in interactive shell

{% highlight python %}
dir("a string")
help("a string".upper)
{% endhighlight %}
</section>

<section markdown="block">
### The len() Method

Returns the length of a sequence.

{% highlight python %}
print(len("cat"))
# gives 3
{% endhighlight %}
</section>

<section markdown="block">
## [String Exercises](exercises.html)
</section>

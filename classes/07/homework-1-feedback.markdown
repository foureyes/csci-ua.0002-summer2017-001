---
layout: slides
title: About Class #7 
---
<section markdown="block" class="title-slide">
# Homework #1 Feedback
{% include title-slide-footer.html %}
</section>

<section markdown="block">
## General Feedback

</section>
<section markdown="block">
### Output vs Program

* please don't submit the output of your program
* ... and don't send a copied and pasted version of your interaction with the interactive shell (that will give an error)

Don't send a file that looks like this:
{% highlight python %}
>>> print("hello")
hello
{% endhighlight %}
</section>



<section markdown="block">
### Print vs String Concatenation

__Using multiple arguments when calling print is not the same as using string concatenation.__

This is two string arguments being passed to print...

{% highlight python %}
print("hello", "there")
{% endhighlight %}

This is a single argument created by adding strings...

{% highlight python %}
print("hello" + " " + "there")
{% endhighlight %}

Lastly, avoid doing this (it works, but it's confusing!)...

{% highlight python %}
print("hello"" ""there")
{% endhighlight %}
</section>

<section markdown="block">
### Variable Names

__One convention that we use for naming variables is: keep variable names lowercase__

This is preferred:

{% highlight python %}
greeting = "hello"
{% endhighlight %}

Over these:

{% highlight python %}
Greeting = "hello"
GREETING = "hello"
{% endhighlight %}
</section>

<section markdown="block">
### Operators

Try to use spaces between operators:

{% highlight python %}
var x = 5 + (10 * 2)
{% endhighlight %}

Avoid this...

{% highlight python %}
var x=5+(10*2)
{% endhighlight %}
</section>

<section markdown="block">
## temperature.py, miles.py
</section>

<section markdown="block">
### Floats / Ints

* totally optional, but if you want to accept floating point numbers, don't use int in your conversion
* (__no points were taken off for this__)
* what happens if you convert the user input into int?


{% highlight python %}
5.0
{% endhighlight %}

(hint... it comes in as a string because of input)
</section>

<section markdown="block">
## tree.py
</section>

<section markdown="block">
### Draw a Tree

* escape backslashes
* add spaces before and after

{% highlight python %}
print(" /\\ ")
print("/  \\")
{% endhighlight %}

... But really ...it wasn't the code that was the issue. The assignment asked for __two trees!__

</section>

<section markdown="block">
### Lost in a Forest

Your tree programs:

* for maximum effect, [play this](https://www.youtube.com/watch?v=RGT4V6JmINA&t=3m45s) while scrolling through slowly
* [trees](../../resources/txt/trees.txt)
</section>


<section markdown="block">
## [Review](review.html)
</section>

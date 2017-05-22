---
layout: slides
title: List Comprehensions 
---
<section markdown="block" class="title-slide">
# List Comprehensions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Create a List of Squares 

__How would I create a list of numbers that are the square root of 0 through 9?__ &rarr;

{% highlight python %}
""" don't just use the list literal """
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
squares = []
for i in range(10):
	squares.append(i**2)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Create a List of Squares 

__How would I create a list of numbers that are the square root of 0 through 9, but only include squares that are divisible by 2?__ &rarr;

{% highlight python %}
""" don't just use the list literal """
[0, 4, 16, 36, 64]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
squares = []
for i in range(10):
	if i % 2 == 0:
		squares.append(i**2)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Quick Summary

* in each instance, we created a list by starting with an empty list
* ...using a for loop
* ...and appending on each iteration

</section>


<section markdown="block">
### List Comprehensions

__List comprehensions__ are another, more concise way of creating lists.  A list comprehension is __syntactic sugar__ (syntax within a programming language that is designed to make things easier to read or to express) for the code that we created previously. 

List comprehensions __make new lists__
</section>

<section markdown="block">
### List Comprehension Syntax

* consists of square brackets to make a list
* a for loop-like expression within the brackets
* before the for loop-like expression, an expression that _calculates_ each element of the new list
* after the for loop-like expression, an optional expression that determines if an element should be in the new list
</section>

<section markdown="block">
### Two Examples: Squares, and Squares Divisible by 2

{% highlight python %}
[x * x for x in range(10)]
[x * x for x in range(10) if x % 2 == 0]
{% endhighlight %}
</section>

<section markdown="block">
### Another List Comprehension

__Write a list comprehension that creates a new list by adding exclamation points to every element in an existing list.__ &rarr;

{% highlight python %}
items = ['foo', 'bar', 'baz', 'busy']
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[s + '!' for s in items]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And Another List Comprehension!

__Limit the previous list to strings of length 3.__ &rarr;

{% highlight python %}
"""
filter the list called items (below), so that the resulting list is:
['foo', 'bar', 'baz']
"""
items = ['foo', 'bar', 'baz', 'busy']
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[s for s in items if len(s) == 3]
{% endhighlight %}
</div>
</section>

<section markdown="block">
## [Tuples](tuples.html)
</section>

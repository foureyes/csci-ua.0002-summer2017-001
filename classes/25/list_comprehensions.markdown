---
layout: slides
title: List Comprehensions 
---
<section markdown="block" class="title-slide">
# List Comprehensions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### List Comprehensions

__What's a list comprehension?__ &rarr;


<div class="incremental" markdown="block">
* __list comprehensions__ are concise way of creating/generating lists
* it is __syntactic sugar__ (syntax within a programming language that is designed to make things easier to read or to express) 
* list comprehensions __make new lists__.
* often, each element of new list is the result of some operations applied to each member of another sequence or iterable (map)
* ...or create a subsequence of elements that satisfy a certain condition (filter)

</div>
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
"""  each element in new list
     | for loop 
     | |  """
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

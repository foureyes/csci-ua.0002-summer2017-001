---
layout: slides
title: Iteration Using Indexes 
---
<section markdown="block" class="title-slide">
# Iteration Using Indexes
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Every Element of a List

__What construct do we use go over every element in a list?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
"""a for loop"""
words = ['dog', 'cat', 'mouse']
for word in words:
	print(word)
{% endhighlight %}

__What does the variable, word, represent?__ &rarr;

...each element in the list.  In this case, the next string on each iteration.
</div>
</section>

<section markdown="block">
## The loop variable is the current element
</section>

<section markdown="block">
### Indexing Into a Sequence

How do we retrieve an element at a specific place from a list or a string?  For example, __to get the second element from the list a = [1, 2, 3], what code would I write? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
a[1]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Indexes

What are some attributes of list and string __indexes__? That is... when you index into a sequence type... 

* __What date type does the index have to be? &rarr;__
* __Are list indexes sequential and consecutive, or are they unordered? &rarr;__

<div class="incremental" markdown="block">
* Indexes are ints
* They are sequential and consecutive
</div>
</section>

<section markdown="block">
### Generating a Sequence of Integers

One way of iterating over every item in a list or a string is to go through each element by indexing.  

__...But how would you generate all of those indexes and go through each one? &rarr;__  

Hint: there are two ways to do this using constructs / statements that we've used before.

<div class="incremental" markdown="block">
* for loop with range
* while loops
</div>
</section>

<section markdown="block">
### For Loops and Indexes

__Use a for loop to print out every element in the list words = ["quill", "qat", "quip"]: &rarr;__

Some hints:

* what parameters should be passed to range?
	* what's the start index?
	* what's the last index?
* how do you access a list element?

<div class="incremental" markdown="block">
{% highlight python %}
words = ["quill", "qat", "quip"]
for i in range(0, len(words)):
	print(i, words[i])
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A More Idiomatic Way to Do It

You can use two loop variables and the built-in __enumerate__ function:

* __enumerate__ takes one argument, an iterable (like a list)
* it allows you to have two loop variables that are comma separated:
	* an index	
	* the actual element
	
{% highlight python %}
words = ["quill", "qat", "quip"]
for i, word in enumerate(words):
	print(i, word)
{% endhighlight %}
</section>

<section markdown="block">
### Using Enumerate

Another look at __enumerate__.  Note that there are now two loop variables:

* __idx__ is the index
* __word__ is the element

We can pull out the index, actual element, and the element at that index (just for demonstration).

{% highlight python %}
nonsense = ["foo", "bar", "baz"]
for idx, word in enumerate(nonsense):
	print(idx, word, nonsense[idx])
{% endhighlight %}
</section>


<section markdown="block">
### While Loops and Indexes

__Use a while loop to print out every element in the list words = ["quill", "qat", "quip"]: &rarr;__

Some hints:

* what index do you start with?
* what's the end condition?
* how do you access a list element?

<div class="incremental" markdown="block">
{% highlight python %}
words = ["quill", "qat", "quip"]
i = 0
while i < len(words):
	print(i, words[i])
	i += 1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### The "Usual" Way

__Finally, to round things out, use a for loop - without indexes - to print out every element in the list words = ["quill", "qat", "quip"] (again, no indexes): &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
words = ["quill", "qat", "quip"]
for word in words:
	print(word)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Reversing a List

__Write a function that takes a list as an input and returns the list in reverse order (btw, there's already a slicing trick and a list method that does this) &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/21/reverse_a_list.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Another (More Destructive Way) to Reverse a List

__Can you use pop to do it? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/21/reverse_a_list_with_pop.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### But Wait - What Happened?

__What's the output of the pop() version of the solution? &rarr;__

{% highlight python %}
{% include classes/21/reverse_a_list_with_pop.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['will', 'soon', 'disappear']
['disappear', 'soon', 'will']
[]
{% endhighlight %}
</div>
</section>

<section markdown="block">
## [Nested Loops, Nested Lists](nested_loops.html)
</section>

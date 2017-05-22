---
layout: slides
title: List Exercises 
---
<section markdown="block" class="title-slide">
# List Exercises
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### About List Exercises

* note that the following exercises create and return new lists!
* there are built-in functions and constructs in Python that make these exercises easier
	* for now, we'll do it the difficult way
	* we'll go over some of these constructs in-depth in later classes
* these exercises will map, filter or reduce a list...

</section>

<section markdown="block">
### Pluralize All (Map)

__Implement a function called pluralize_all: &rarr;__

* it will take a list of strings called __words__
* it should return a list of strings 
* the resulting list will have plural versions of every string passed in
* assume that each element in the list is a string that's a singular word
* you can use a naive method of pluralization (just add an 's'!)
* it will return an empty list if an empty list is inputted
* remember to use assertions
</section>

<section markdown="block">
### Pluralize All ... Output

{% highlight pycon %}
print(pluralize_all(["zebra", "cow", "tiger"]))
['zebras', 'cows', 'tigers']
{% endhighlight %}

<!--_-->
</section>

<section markdown="block">
### Pluralize All Potential Solution

{% highlight python %}
def pluralize_all(words):
	new_list = []
	for word in words:
		new_list.append(word + 's')
	return new_list
{% endhighlight %}
</section>


<section markdown="block">
### More Characters Than (Filter)

__Implement a function called more_characters_than: &rarr;__

* it will take a list of strings, called _words_, and an integer, called _min_, as an input
* it should return a list of strings 
* the resulting list will only have strings with more than _min_ characters
* it will return an empty list if an empty list is inputted
* ignore the case where a list has non-string types or if min is not an integer
* remember to use assertions

</section>

<section markdown="block">
### More Characters Than Example

{% highlight pycon %}
print(more_characters_than(["zebra", "cow", "tiger"], 4))
['zebra', 'tiger']
{% endhighlight %}
</section>

<section markdown="block">
### More Characters Than Potential Solution

{% highlight python %}
{% include classes/18/more_characters_than.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Average (Reduce)

* define a function called average
* it should take a list of numbers as an argument
* it will return the average of the numbers in the list
* empty list will have an average of 0
* remember to use assertions
</section>

<section markdown="block">
### Implementing Average

{% highlight python %}
{% include classes/18/average.py %}
{% endhighlight %}

Using the built-in sum:

{% highlight python %}
def average(numbers):
	return sum(numbers) / len(numbers)
{% endhighlight %}
</section>

<section markdown="block">
### Notes

Interested in other ways to do this?  __Check out...__ &rarr;

* [List Comprehensions](https://docs.python.org/3.1/tutorial/datastructures.html#list-comprehensions) (we'll check this out in a later class)
* [map()](https://docs.python.org/3/library/functions.html#map)
* [filter()](https://docs.python.org/3/library/functions.html#filter)

</section>

<section markdown="block">
## [Lists and Mutability](mutability.html)
</section>


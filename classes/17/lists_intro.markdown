---
layout: slides
title: 
---
<section markdown="block" class="title-slide">
# Lists
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Types of Types

There are higher classifications of types - like types of types! For example, the following types are numeric:

* int
* float
* complex

You can do similar operations on all of these types

</section>
<section>
<h3>Sequences</h3>

There are a group of types called sequences.
<ul>
	<li>an ordered collection of "stuff"</li>
	<li>index into (retrieve item from) sequences by using brackets [i], with <strong>initial index 0</strong></li>
	<li>negative indexes start from the right, where -1 is the last character</li>
	<li>a subset of a sequence from index n <em>up to</em> m can be sliced out using [m:n]</li>
	<li>again... m - up to, but not including!</li>
</ul>
</section>

<section markdown="block">
### We've Seen This Before in Strings

Strings are a sequence type; they're an ordered set of characters.

{% highlight pycon %}
>>> "nerds"[0] #first element,  
>>> "nerds"[4] #last element (n - 1)
>>> "nerds"[5] #IndexError 
>>> "nerds"[-1] #from the right  
>>> "nerds"[-2] #again
>>> "nerds"[0:2] #slices
>>> "nerds"[3:1] #nothing to slice
>>> "nerds"[3:-1] #something to slice even though negative
>>> "nerds"[3:] #no end index,  >>> "nerds"[:2] #no start index
{% endhighlight %}

</section>

<section>
<h3>Lists</h3>

A list is another sequence type.  However, instead of characters, it's an ordered collection of _values_.  Any values!
<ul>
	<li>Delimited by brackets... []</li>
	<li>[] is an empty list (what Boolean value does this evaluate to if used as an expression in a condition?)</li>
	<li>Each value is separated by commas</li>
	<li>A list of integers - [1, 2, 3, 4]</li>
	<li>A list of strings - ['foo', 'bar', baz']</li>
	<li>A list of integers, strings and other lists! - ['foo', 1, ['foo', 'bar', 'baz']]</li>
</ul>
</section>




<section>
<h3>len()</h3>

You can still use the built-in function, len, on lists.

{% highlight pycon %}
>>> print(len(["foo", "bar", "baz"])
... 
KeyboardInterrupt
>>> print(len(["foo", "bar", "baz"]))
3
>>> print(len([]))
0
>>> print(len(["foo", "bar", "baz", [1, 2, 3]]))
4
{% endhighlight %}
</section>

<section markdown="block">
### Iterating Over a List

Just like iterating over a sequence of charactersi...

* you can use a for loop to iterate over a sequence of values in a list
* your loop variable contains the value of a list element
* that changes to the next element after each iteration

{% highlight python %}
junk = ["skittles", "snickers", "nerds"]
# candy is our loop variable... it will represent each element of the list
for candy in junk:
	print("I <3 {0}!".format(candy)) 
{% endhighlight %}
</section>

<section>
<h3>Some functions that you can call on lists</h3>
<ul>
	<li>li.append(4) # appends element to end of list</li>
	<li>li.remove(4) # removes first occurrence of...</li>
	<li>li.pop() # Returns and removes the last element</li>
	<li>li.extend([3, 4]) # appends all items of one list to the other...</li>
	<li>li.sort() # sorts list in place</li>
	<li>[1, 2, 4, 1, 5, 1].count(1) # returns number of occurrences of arg in list</li>
</ul>
</section>

<section>
<h3>Looking for something?</h3>
<ul>
	<li>['a', 'b', 'c'].index('c') # return index of item, or exception</li>
	<li>'c' in ['a','b', 'c'] # returns boolean</li>
</ul>
</section>

<section>
<h3>Strings to Lists and Back</h3>
<ul>
	<li>"a,b,c".split(",")</li>
	<li>",".join(['a', 'b', 'c'])</li>
</ul>
</section>


<section markdown="block">
### Excercises

* create a function called three_letter_words
	* it takes a list
	* it returns a list of 3 letters words from original list
* create a function called larger_than_five
	* it takes a list
	* it returns a list of numbers > 5 from the original list
	* it returns a list, and that list only has numbers larger than 5
* create a function that returns a random list of numbers (1 through 10) that are &gt;= 21
* hints:
	* use a for loop!
	* start with an empty list and append items
</section>

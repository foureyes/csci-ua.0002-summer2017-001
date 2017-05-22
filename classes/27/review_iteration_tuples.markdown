---
layout: slides
title: Review 
---
<section markdown="block" class="title-slide">
# Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Aliasing 

I have a variable called __fungi__.  It's a list of strings.  I'd like to create an __alias__ called __same_as_fungi__ for it - that is, I'd like to create a variable name that refers to the same object as the original. 
{% highlight python %}
fungi = ['yeasts', 'molds', 'mushrooms']
# create an alias here called same_as_fungi
same_as_fungi.pop()
print('fungi %s' % (fungi))
print('same_as_fungi %s' % (same_as_fungi))

# resulting output: 
# fungi ['yeasts', 'molds']
# same_as_fungi ['yeasts', 'molds']
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
same_as_fungi = fungi
{% endhighlight %}
</div>
</section>

<section markdown="block">
### What if We Wanted to Make a Copy

Let's __clone__ an existing list rather than creating an __alias__ for it.  How can you write this in code?

{% highlight python %}
fungi = ['yeasts', 'molds', 'mushrooms']
# clone here; call it copy_of_fungi
copy_of_fungi .pop()
print('fungi %s' % (fungi))
print('copy_of_fungi %s' % (copy_of_fungi))
# results in
# fungi ['yeasts', 'molds', 'mushrooms']
# copy_of_fungi ['yeasts', 'molds']
{% endhighlight %}

<div class="incremental" markdown="block">
You can use __slicing__ to clone:

{% highlight python %}
copy_of_fungi = fungi[:]
# or copy_of_fungi = fungi[0:len(fungi)]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### In Functions 

When you pass a list as an argument to a function, you're actually passing a reference to the list.  __What will the following code print out? &rarr;__

{% highlight python %}
import random
def add_a_fungus(list_of_stuff):
	"""adds a random fungus to whatever list is passed in!"""
	fungus_to_add = random.choice(['mushroom', 'mold', 'yeast'])
	list_of_stuff.append(fungus_to_add)

numbers = [1, 2, 3]
result = add_a_fungus(numbers)
print(numbers)
print(result)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2, 3, 'mushrooms']
None
{% endhighlight %}
</div>

<!--_-->
</section>

<section markdown="block">
### Remove Vowels From Every Element in a List

__Create a function called no_vowels_please; implement it two different ways:__ &rarr;

* returns a new list
	* the new list contains every element with vowels removed
* modifies the list in place
	* every element in the list passed in should be overwritten with that same element without vowels
</section>

<section markdown="block">
### First...

__Let's create a reusable function that will remove vowels for us!__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
def remove_vowels(s):
	no_vowels = ''
	for c in s:
		if c.lower() not in 'aeiou':
			no_vowels += c
	return no_vowels

assert 'rdvrk' == remove_vowels('aardvark')
assert 'ntlp' == remove_vowels('antelope')
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Remove Vowels From Every Element in a List (New List)

__Implement no_vowels_please__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
def no_vowels_please(words):
	vowels_removed = []
	for word in words:
		vowels_removed.append(remove_vowels(word))
	return vowels_removed

assert ['rdvrk', 'ntlp'] == no_vowels_please(['aardvark', 'antelope'])
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Remove Vowels From Every Element in a List (In Place)

__Implement no_vowels_please_in_place__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
def no_vowels_please_in_place(words):
	for i in range(len(words)):
		words[i] = remove_vowels(words[i])
animals = ['aardvark', 'antelope']
no_vowels_please_in_place(animals)

assert ['rdvrk', 'ntlp'] == animals
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Iterating Over a List Using Indexes

Notice that the _in place_ version accessed every element in the list using a for loop and __generated indexes__.  This is possible because:

* list indexes are __ints__
* indexes are __sequential and consecutive__
</section>


<section markdown="block">
### We Could Have Used a While Loop Too

__Implementation of no_vowels_please_in_place with a while loop...__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
def no_vowels_please_in_place(words):
	count = 0
	while count < len(words):
		words[count] = remove_vowels(words[count])
		count += 1

animals = ['aardvark', 'antelope']
no_vowels_please_in_place(animals)
assert ['rdvrk', 'ntlp'] == animals
{% endhighlight %}
</div>

</section>

<section markdown="block">
### And Finally, With Enumerate

__Implementation of no_vowels_please_in_place with enumerate...__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
def no_vowels_please_in_place(words):
	for i, word in enumerate(words):
		words[i] = remove_vowels(word)

animals = ['aardvark', 'antelope']
no_vowels_please_in_place(animals)
assert ['rdvrk', 'ntlp'] == animals
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Reversing a List

Iterating using indexes is useful for changing things in place, but it's also necessary for certain algorithms.  For example, bubble sort requires an awareness of the following element.  Here's an example of reversing a list... 

{% highlight python %}
{% include classes/21/reverse_a_list.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Again, With List Comprehensions

__We can actually replace our new list version of no_vowels_please with a single list comprehension...__ &rarr;

{% highlight python %}
def remove_vowels(s):
	no_vowels = ''
	for c in s:
		if c.lower() not in 'aeiou':
			no_vowels += c
	return no_vowels
{% endhighlight %}

<div class='incremental'>
{% highlight python %}
words = ['aardvark', 'antelope']
no_vowels = [remove_vowels(word) for word in words]
print(no_vowels)
{% endhighlight %}
</div>
<!--_-->
</section>

<section markdown="block">
### Filtering With List Comprehensions

We can use list comprehensions to filter lists as well... __let's create a list comprehension that takes a list of words and returns a new list that only contains words that end in 'k'__ &rarr;

{% highlight python %}
words = ['aardvark', 'antelope']
{% endhighlight %}

<div class='incremental'>
{% highlight python %}
last_letter_k = [ w for w in words if w[-1] == 'k']
print(last_letter_k)
{% endhighlight %}
</div>
<!--_-->
</section>

<section markdown="block">
### List Comprehensions Summary

* syntatic sugar (a _convenience_) for making new lists
* again, list comprehensions __make new lists__.
* consists of square brackets (like a list)
* a for loop-like expression within the brackets
* before the for loop-like expression, an expression that _calculates_ each element of the new list
* after the for loop-like expression, an optional expression that determines if an element should be in the new list
</section>

<section markdown="block">
### What's a Tuple?  

__What's a tuple and how is it different from a list?__

<div class="incremental" markdown="block">
* a __tuple__ is an immutable grouping of data
* a __tuple__ is a sequence type
* it can be considered as an immutable list.  
* consequently, tuples can't be changed, unlike lists
</div>
</section>

<section markdown="block">
### Tuple Syntax

__What's the syntax for creating a tuple?__

<div class="incremental" markdown="block">
* comma separated list of values
* add parentheses to prevent ambiguity (for example, in function calls)
{% highlight python %}
t = 1, 2, 3
type(t)
print(t)

t = (1, 2, 3)
type(t)
print(t)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Tuple Operations, Functions and Methods

__What can and can't you do with tuples?__


<div class="incremental" markdown="block">
* supports sequence operators such as:
	* concatenation (__+__), multiplication (__*__) - both return a tuple
	* indexing (__[index]__) - returns value
	* slicing (__[m:n]__) - returns a tuple
	* iteration - you can loop over elements in a tuple
* because tuples are immutable...	
	* no append
	* no extend
	* etc.
* __Let's try these out!__
</div>
</section>

<section markdown="block">
### Multiple Assignment / Unpacking

We've seen tuples before in multiple assignment

* if there is a tuple of variables on the left side
* and equal number of values in a tuple on the right side
* each value is bound to each variable in order 
* this is also called __tuple unpacking__

{% highlight python %}
a, b, c = 1, 2, 3
first_name, last_name = ("Timothy", "Tupleton")
{% endhighlight %}
</section>

<section markdown="block">
### Lists of Tuples

__What's the type of person in every iteration?  How many iterations are there?  What does this print out?__


{% highlight python %}
smarties = [("Mr", "Smartypants"), ("Ms", "Knowitall")]
for person in smarties:
	print(person)
{% endhighlight %}

<div class="incremental" markdown="block">
* it's a tuple
* this loops twice
* it outputs:
{% highlight python %}
('Mr', 'Smartypants')
('Ms', 'Knowitall')
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lists of Tuples Exercise

__Write a function called hello...__

* it should take a list of tuples as an argument
* assume that every tuple is three elements, with an honorific and a first and last name
* it should take each tuple and convert it into a string by:
	* starting with hello, and adding the first element with a period
	* adding the third element with an exclamation point
	* ("Mr", "Sam", "Smartypants") &rarr; Hello Mr. Smartypants
	* note that the first name is ignored
* the function should just print out each resulting string (no return value)

{% highlight python %}
smarties = [("Mr", "Sam", "Smartypants"), ("Ms", "Nelly", "Knowitall")]
hello(smarties)

Hello Mr. Smartypants!
Hello Ms. Knowitall!
{% endhighlight %}
</section>

<section markdown="block">
### Lists of Tuples Exercise Solutions

__We can do this a couple of ways...__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/25/smarties.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lists of Tuples Exercise Solutions

By the way, if we wanted to include the first name... we could use the code below.  __Why does this work__

{% highlight python %}
# tuples can be used in string formatting as is!
def hello(t):
	for person in t:
		print("Hello %s. %s %s!" % (person))
{% endhighlight %}

<div class="incremental" markdown="block">
As mentioned in the previous class, we use tuples in familiar constructs in Python... such as multiple assignment.  It turns out, the second operand of a string formatting is a tuple.
</div>
</section>

<section markdown="block">
### Run Length Encoding

__Run length encoding__ is a simple method of compressing data by:

1. Finding sequences of the same element in the data
2. And converting those sequences to a number and a single element 
3. For example, "loook!!" would be encoded as "1l3o1k2!"
4. [The wikipedia article shows some examples](http://en.wikipedia.org/wiki/Run-length_encoding#Example)

__What's the run length encoded version of "cccaaabbb"?__

<div class="incremental" markdown="block">
3c3a3b
</div>
</section>

<section markdown="block">
### Encode!

__Let's write some pseudocode.  What are some ways to solve this?__


<div class="incremental" markdown="block">
{% highlight python %}
# keep track of the current letter
# keep track of the current letter count
# keep track of all previous letters and counts (what's a good data structure for this?)
# go through every letter in the string
# when we first see a letter, count it as 1, if we see it again, increment that count
# stop incrementing when we see another letter (reset values)
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  A Possible Solution

{% highlight python %}
{% include classes/25/rle.py %}
{% endhighlight %}
</section>

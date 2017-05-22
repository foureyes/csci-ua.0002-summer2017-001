---
layout: slides
title: Iteration Using Indexes 
---
<section markdown="block" class="title-slide">
# Iteration Using Indexes
{% include title-slide-footer.html %}
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

* __What data type does the index have to be? &rarr;__
* __Are list indexes sequential and consecutive, or are they unordered? &rarr;__

<div class="incremental" markdown="block">
* Indexes are ints
* They are sequential and consecutive
</div>
</section>

<section markdown="block">
### Getting an Index With an Item

Occasionally, you'll want to determine the index of the item that you're working on.  __For example...__ &rarr;
</section>

<section markdown="block">
### Getting an Index With an Item Exercise 1

__Printing out the index of a list item along with the actual item__ &rarr;

{% highlight python %}
names = ['Alice', 'Bob', 'Carol']
# loop through list to print out
0 Alice
1 Bob
2 Carol
{% endhighlight %}
</section>

<section markdown="block">
### Getting an Index With an Item Exercise 2

__Changing a list _in place_ (that is assigning a new value to each element in a list)__ &rarr;

{% highlight python %}
names = ['Alice', 'Bob', 'Carol']
# make every item in names uppercase without creating a new list
print(names)
# prints out...
['ALICE', 'BOB', 'CAROL']
{% endhighlight %}

</section>

<section markdown="block">
### Getting the Index With the List Item

There are a few ways to loop through a list so that you have access the index of every item:

1. using __enumerate__() (the most _pythonic_ way)
2. using a count variable in conjunction with a for loop
3. using indexes to iterate
</section>

<section markdown="block">
### Using the Built in Enumerate Function

__enumerate__() is a built in function that: 

* takes a list as an argument
* it returns a list-like structure composed of tuples
* each tuple consists of the index and the value of each element in the list

{% highlight python %}
names = ['Alice', 'Bob', 'Carol']
index_value_pairs = enumerate(names)
# index_value_pairs will give back an index and a value if iterated over...
{% endhighlight %}


</section>

<section markdown="block">
### Enumerate Example

__Printing out the index of a list, ['Alice', 'Bob', 'Carol'], item along with the actual item.__ &rarr;

<div class="incremental" markdown="block">

{% highlight python %}
names = ['Alice', 'Bob', 'Carol']
for index, name in enumerate(names):
	print(index, name)
{% endhighlight %}

__Making every element in names uppercase without creating a new list.__ &rarr;

{% highlight python %}
names = ['Alice', 'Bob', 'Carol']
for index, name in enumerate(names):
	names[index] = name.upper()
print(names)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Using a Count Variable

__Printing out the index of a list, ['Alice', 'Bob', 'Carol'], item along with the actual item.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
index = 0
names = ['Alice', 'Bob', 'Carol']
for name in names:
	print(index, name)
	index += 1 
{% endhighlight %}

__Making every element in names uppercase without creating a new list.__ &rarr;

{% highlight python %}
index = 0
names = ['Alice', 'Bob', 'Carol']
for name in names:
	names[index] = name.upper()
	index += 1 
print(names)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Generating a Sequence of Integers

One last way of iterating over every item in a list or a string is to go through each element by indexing.  

__...But how would you generate all of those indexes and go through each one? &rarr;__  

Hint: there are two ways to do this using constructs / statements that we've used before.

<div class="incremental" markdown="block">
* for loop with range
* while loops
</div>
</section>

<section markdown="block">
### For Loops and Indexes

__Use a for loop to print out every element in the list a = ["quill", "qat", "quip"]: &rarr;__

Some hints:

* what parameters should be passed to range?
	* what's the start index?
	* what's the last index?
* how do you access a list element?

<div class="incremental" markdown="block">
{% highlight python %}
a = ["quill", "qat", "quip"]
for i in range(0, len(a)):
	print(a[i])
{% endhighlight %}
</div>
</section>

<section markdown="block">
### While Loops and Indexes

__Use a while loop to print out every element in the list a = ["quill", "qat", "quip"]: &rarr;__

Some hints:

* what index do you start with?
* what's the end condition?
* how do you access a list element?

<div class="incremental" markdown="block">
{% highlight python %}
a = ["quill", "qat", "quip"]
i = 0
while i < len(a):
	print(a[i])
	i += 1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Generating Indexes

__Printing out the index of a list, ['Alice', 'Bob', 'Carol'], item along with the actual item.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
names = ['Alice', 'Bob', 'Carol']
for index in range(len(names)):
    print(index, names[index])
    index += 1
{% endhighlight %}

__Making every element in names uppercase without creating a new list.__ &rarr;

{% highlight python %}
names = ['Alice', 'Bob', 'Carol']
for index in range(len(names)):
    names[index] = names[index].upper()
    index += 1
print(names)
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Reversing a List

__Write a function that takes a list as an input and returns the list in reverse order (btw, there's already a list method that does this) &rarr;__

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

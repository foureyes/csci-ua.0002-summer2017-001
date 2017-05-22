---
layout: slides
title: Methods, Functions, and References 
---

<section markdown="block" class="title-slide">
# Review - Methods, Functions, and References
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Removing Elements

__Name three ways to remove element(s) from a list &rarr;__

<div class="incremental" markdown="block">
* __remove__(value) # removes first occurrence of value
* __pop__() # returns and removes the last element
* del # sorts list in place
</div>
</section>

<section markdown="block">
### Removing Elements Example

__What's the output of this code? &rarr;__
{% highlight python %}
{% include classes/22/remove.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['Bob', 'Linda', 'Lousie', 'Gene'] None
['Bob', 'Linda', 'Gene', 'Lousie'] Gene
['Bob', 'Linda', 'Gene', 'Lousie']
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Removing Elements Notes

* __remove__ does not return a value
* __remove__ gives an error when the value doesn't exist
* __pop__ returns the element removed
* __pop__ can actually take an index as an argument (someone had asked about this during the last class)
* __pop__ gives an error if the index doesn't exist
* __del__ gives an error if the index doesn't exist
</section>

<section markdown="block">
### Adding Elements

__Name two ways to remove element(s) from a list &rarr;__

<div class="incremental" markdown="block">
* __append__(object) # appends value to end of list
* __extend__(iterable) # appends all items of one iterable (list, string, etc.) to the other...
</div>
</section>

<section markdown="block">
### Adding Elements Example

__What's the output of this code? &rarr;__

{% highlight python %}
{% include classes/22/add.py %}
{% endhighlight %}

</section>

<section markdown="block">
### Adding Elements Example Output

{% highlight python %}
['red', 'green', 'blue']
['red', 'green', ['blue', 'orange']]
['red', 'green', ['blue']]
['red', 'green', 'blue', 'orange']
{% endhighlight %}
</section>

<section markdown="block">
### Adding Elements Notes

* __append__ actually adds the entire object as a single element to the original list
* __extend__ adds every element of a list or string to the original list
</section>

<section markdown="block">
### Other List Functions

* __What method can you use to find the number of occurrences of a value in a list?__
* __What methods places a list's elements in order?__

<div class="incremental" markdown="block">
* __sort__() # sorts list in place
* __count__(value) # returns number of occurrences of value in list
</div>
</section>

<section markdown="block">
### Count and Sort Examples

__What's the output of this code? &rarr;__

{% highlight python %}
{% include classes/22/count_and_sort.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
2
0
[3, 1, 1, 2]
[1, 1, 2, 3]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Strings and Lists

* __What method can I use to turn a string into a list? &rarr;__
* __What type of object is this method called on? &rarr;__
* __What method can I use to turn a list into a string? &rarr;__
* __What type of object is this method called on? &rarr;__

<div class="incremental" markdown="block">
* __split__(delimiter) # breaks apart a string into list elements
* str
* __join__(glue) # joins elements of a list into a string using the string that the method was called on as "glue"
* str
</div>

</section>

<section markdown="block">
### Strings and Lists Example
__Use this list to create a string separated by the word ' yikes! ' &rarr;__
{% highlight python %}
monsters = ['zombies', 'vampires', 'mummies']
{% endhighlight %}

__Use this string to create a list of animals, but don't include 'oh my' &rarr;__

{% highlight python %}
oz = "lions and tigers and bears, oh my"
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/22/strings_and_lists.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Random - Choice, Shuffle

* __What function from the random module can be used to retrieve a random element from a list? &rarr;__
* __What function from the random module can be used to mix up a list? &rarr;__

<div class="incremental" markdown="block">
* __choice__(my_list): retrieves a random item from the supplied list
* __shuffle__(my_list): randomly changes the order of the elements in the list passed in (_in place_)
</div>

</section>

<section markdown="block">
### Generating Random Elements from a List

Using the alphabetically sorted list of sounds below... 

1. __Print 20 sounds randomly &rarr;__
2. __Print each sound exactly once in random order &rarr;__

{% highlight python %}
sounds = ['beep', 'buzz', 'fizz', 'honk']
{% endhighlight %}
</section>

<section markdown="block">
### Generating Random Elements from a List Solution

{% include classes/22/sounds.py %}

</section>

<section markdown="block">
### References 

__What's the output of the following code? &rarr;__

{% highlight python %}
a = [1, 2, 3]
b = [1, 2, 3]
b.append(4)
print(a)
print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2, 3]
[1, 2, 3, 4]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### References Continued

__What's the output of the following code? &rarr;__

{% highlight python %}
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2, 3, 4]
[1, 2, 3, 4]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lists and Functions - the Long Way to Do It

__What's the output of the following code? &rarr;__

{% highlight python %}
community = ['Leonard', 'star-burns', 'the dean']
def remove_last_two(things):
	# not a great way to do this; we'll see using indexes later
	new_list = []
	count = 1
	for item in things:
		if count > len(things) - 2:
			break
		new_list.append(item)
		count += 1
	return new_list

result = remove_last_two(community)
print("result is %s" % (result))
print("community is still %s" % (community))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
result is ['Leonard']
community is still ['Leonard', 'star-burns', 'the dean']
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lists and Functions - a Shorter Way

__What's the output of the following code? &rarr;__

{% highlight python %}
community = ['Leonard', 'star-burns', 'the dean']
def remove_last_two(things):
	# frazzled face!
	return things[:-2]

result = remove_last_two(community)
print("result is %s" % (result))
print("community is still %s" % (community))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
result is ['Leonard']
community is still ['Leonard', 'star-burns', 'the dean']
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lists, Functions and References

__What's the output of the following code? &rarr;__

{% highlight python %}
community = ['Leonard', 'star-burns', 'the dean']
def remove_last_two(things):
	# magnitude!
	things.pop()
	things.pop()
	return things

result = remove_last_two(community)
print("result is %s" % (result))
print("community is now %s" % (community))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
result is ['Leonard']
community is now ['Leonard']
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Some Notes

* remember - __lists__ are __mutable__... functions like pop actually change the list
* however, list slicing __returns a new list__

{% highlight python %}
a = [1, 2, 3, 4]
b = a[:2]
print(a) # remains unchanged
print(b)
{% endhighlight %}
</section>

<section markdown="block">
## [Addendum to List Methods](addendum.html)
</section>


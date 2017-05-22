---
layout: slides
title: Lists 
---
<section markdown="block" class="title-slide">
# Lists
{% include title-slide-footer.html %}
</section>


<section markdown="block">

### Sequences

We've seen __numeric__ types, like int, float and complex.  Another kind/classification of type is a __sequence__. A __sequence__:

* consists of an ordered collection of elements
* with each element identified by an index

Sequences support operations like:

* indexing to retrieve an element
* slicing to retrieve a subset of elements
* concatenation
* multiplication

</section>

<section markdown="block">
### Strings are Sequences

A __string__ is an ordered sequence of characters.  It is a __sequence__ type.  It supports:

{% highlight pycon %}
"blubbins?"[0] #index, first element -> "b" 
"blubbins?"[-1] #index, last element -> "?"
"blubbins?"[1:4] #slices -> "lub"
"blubbins?"[4:] #slices -> "bins?"
"what the " + "blubbins?" # concatenates -> "what the blubbins?"
"blubbins?" * 2 # repeats -> "blubbins?blubbins?"
{% endhighlight %}
</section>

<section markdown="block">
### Lists

A __list__ is another sequence type.  

* instead of characters, it's an ordered collection of __values__
* _any_ values!
* an example of a list of ints and strings

{% highlight python %}
# a list of ints
stuff = [1, "one", 2, "two"]
{% endhighlight %}
</section>

<section markdown="block">
### List Literals

Constructing a list using a list literal looks like this:
{% highlight python %}
["some", "stuff", "between", "brackets"]
{% endhighlight %}

* delimited by brackets... [1, 2, 3]
* each value is separated by a comma
* a list with no elements is an __empty list__ 
* an empty list is []
* again, mixed types are allowed (even other lists) - ['pie', 3, 3.14, ['apple', ['cherry']]
</section>

<section markdown="block">
### Printing Lists

You can pass lists directly to the built-in print function.  It will output the list as if it were a string literal: 

{% highlight pycon %}
>>> a = [2, 3, 5, 7]
>>> print(a)
[2, 3, 5, 7]
{% endhighlight %}

You can also use str() or string interpolation to create a string representation of a list:

{% highlight pycon %}
>>> a = [2, 3, 5, 7]
>>> print("Some numbers in a list: %s" % a)
Some numbers in a list: [2, 3, 5, 7]
{% endhighlight %}
</section>

<section markdown="block">
### Indexing Operations Summary

* an empty list is just []
* just like characters in a string, elements in a list can be accessed by their index (place)
* indexes start at 0 
* use the value (a variable, a list literal, etc) followed by the square brackets
* ... with the index enclosed: [1, 2, 3][0] &rarr; 1
* negative indexes start at the end of the list: [1, 2, 3][-1] &rarr; 3
</section>

<section markdown="block">
### Iterating Over a List

Just like iterating over a sequence of characters...

* you can use a for loop to iterate over a sequence of values in a list
* your loop variable contains the value of a list element
* that changes to the next element after each iteration

</section>

<section markdown="block">
### Iterating Over a List Example

__What will the following for loop print out? &rarr;__

{% highlight python %}
some_boolean_values = [True, True, False]
for b in some_boolean_values:
	print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
True
True
False
{% endhighlight %}
</div>
</section>



<section markdown="block">
### Slicing

Slicing also works on lists.  __What will the folloing code output? &rarr;__

{% highlight python %}
colors = ["red", "green", "blue", "taupe"]
print(colors[0:2])
print(colors[2:])
print(colors[:3])
print(colors[0:100])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['red', 'green']
['blue', 'taupe']
['red', 'green', 'blue']
['red', 'green', 'blue', 'taupe']
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slicing Summary

Again... like slicing strings.

* use square brackets
* ...with start index and end index separated by a colon: [2, 3, 5, 7][1:3] &rarr; [3, 5]
* start and end can be omitted: [2, 3, 5, 7][:2] &rarr; [2, 3]
</section>

<section markdown="block">
### Equality Operators

Equality operators work with lists as you'd expect:

{% highlight python %}
print([1, 2, 3] == [1, 2, 3])
print(['a', 'b', 'c'] == [1, 2, 3])
print([1, 2, 3] != [1, 2, 3])
print(['a', 'b', 'c'] != [1, 2, 3])
{% endhighlight %}

Outputs:

{% highlight python %}
True
False
False
True
{% endhighlight %}
</section>

<section markdown="block">
### Addition and Multiplication

Multiplication and addition of lists are similar to the same operations on strings.  __What will the following code output? &rarr;__

{% highlight python %}
toppings = ["mushrooms", "peppers", "onions"]
numbers = [2, 3, 5, 7]
print(toppings + numbers)
print(toppings * 2)
print(numbers * 2)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
["mushrooms", "peppers", "onions", 2, 3, 5, 7]
["mushrooms", "peppers", "onions", "mushrooms", "peppers", "onions"]
[2, 3, 5, 7, 2, 3, 5, 7]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Addition and Multiplication Summary

* list concatenation 
	* __+__
	* adds the elements of one list to another list
	* [1, 2] + [3, 4] &rarr; [1, 2, 3, 4]
* list multiplication
	* __*__
	* repeats a list the given number of times
	* [1, 2] * 3 &rarr; [1, 2, 1, 2, 1, 2]
</section>

<section markdown="block">
### Mutability

Unlike strings, however, lists are __mutable__.  That means that you can reassign a value at an index!  __What will the following code print out? &rarr;__

{% highlight python %}
>>> a = [3, 4, 5]
>>> a[0] = "surprise"
>>> print(a)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['surprise', 4, 5]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Mutability and List Methods

__Remember - most list methods actually change the object that you're calling the method on!__  Many list methods don't return values... but there are some that do.  __What are some list methods that return values?__

<div class="incremental" markdown="block">
* pop - returns last element
* index - returns index of value
</div>
</section>

<section markdown="block">
### Mutability and List Methods Continued

__What does this code output?__
{% highlight python %}
a = [3, 2, 1]
a.sort()
b = a.pop()
print(a)
print(b)

{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2]
3
{% endhighlight %}
</div>
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

{% highlight python %}
{% include classes/22/sounds.py %}
{% endhighlight %}

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
### Lists, Functions and References

__What's the output of the following code? &rarr;__

{% highlight python %}
numbers = [1, 2, 3]
def remove_last_two(things):
	things.pop()
	things.pop()
	return things

result = remove_last_two(numbers)
print("result is %s" % (result))
print("numbers is now %s" % (numbers))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# they're the same, a reference to numbers was passed in... as
# a side effect of calling pop on things, numbers was changed too
result is [1]
numbers is now [1]
{% endhighlight %}
</div>
</section>


<section markdown="block">
### A Few More Notes

* this side effect from passing references to functions only matter with mutable types
	* strings and numbers can't be changed (there's no equivalent to append or sort)
	* be careful when passing lists in as arguments to a function
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

What are some attributes of list and string indexes?  

* __What type are they (what type is the variable i below)? &rarr;__
* __Are list indexes sequential and consecutive, or can they skip numbers? &rarr;__

{% highlight python %}
a = ["foo", "bar", "baz"]
i = 1
print(a[i])
print(a[i + 1])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
* Indexes are ints
* They are sequential and consecutive; they do not skip numbers
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Generating a Sequence of Integers

We generally don't care about indexes when we loop over a list, but an alternate way of iterating over every item is to go through each element by indexing.  

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
### The "Usual" Way

__Finally, to round things out, use a for loop - without indexes - to print out every element in the list a = ["quill", "qat", "quip"]: &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
a = ["quill", "qat", "quip"]
for word in a:
	print(word)
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

<section markdown="block">
### Some Common Patterns

* a lot of list exercises that we do in class fall into one of these patterns:
	* map - map a function to every element in a list, like half of every value
	* filter - create a new list with elements filtered out, like only greater than 5
	* reduce - reduce a list to a single value, like sum
* (there are python functions and constructs that do this - see list comprehensions, lambdas and filter, map and reduce)
</section>

<section markdown="block">
### Map

Apply a transformation to every element.  __Write a function that halves the value of every element of a list passed in.__  It returns a new list.

{% highlight python %}
a = [20, 10, 4]
def half_of_each(numbers):
	result = []
	for number in numbers:
		result.append(number/2)
	return result

print(half_of_each(a))
{% endhighlight %}
</section>

<section markdown="block">
### Reduce

Reduce a list to a single value.  __Write a function that sums every element of a list passed in.__  It returns a value.

{% highlight python %}
a = [20, 10, 4]
def sum_all_numbers(numbers):
	result = 0
	for number in numbers:
		result += number
	return result

print(sum_all_numbers(a))
{% endhighlight %}
</section>

<section markdown="block">
### Filter

Filter the elements in a list to create a new list.  __Write a function that takes a list passed in and returns a new list with only numbers that are less than 10.__ 

{% highlight python %}
a = [20, 10, 4]
def less_than_ten(numbers):
	result = []
	for number in numbers:
		if number < 10:
			result.append(number)
	return result

print(less_than_ten(a))
{% endhighlight %}
</section>

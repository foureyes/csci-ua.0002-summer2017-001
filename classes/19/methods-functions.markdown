---
layout: slides
title: Lists - Methods and Functions 
---

<section markdown="block" class="title-slide">
# Lists - Methods and Functions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### List Methods

These methods are called _on list objects_!

* __append__(object) # appends value to end of list
* __extend__(iterable) # appends all items of one iterable (list, string, etc.) to the other...
* __remove__(value) # removes first occurrence of value
* __pop__() # returns and removes the last element
* __sort__() # sorts list in place
* __insert__(i, object) # adds an object to the list at index
* __count__(value) # returns number of occurrences of value in list
* __index__(object) # returns the index of the object supplied
</section>

<section markdown="block">
### Adding Elements to a List

* __append__(object) adds an object to the end of a list
* __extend__(iterable) adds all of the elements of an iterable object, such as a list or a string, to the end of a list. 
* __insert__(i, object) adds object as an element before the index
* __insert__, __append__, and __extend__ __do not__ return a value; they change the list in place!
</section>

<section markdown="block">
### Adding Elements to a List Example

__what does this code output? &rarr;__

{% highlight python %}
{% include classes/21/append_and_extend.py %}
{% endhighlight %}

</section>

<section markdown="block">
### Adding Elements to a List Example - Output

{% highlight python %}
['Knuth', 'Ritchie', ['Church', 'Turing']]
['Camus', 'Chomsky', 'Church', 'Turing']
['a', 'b', 'c', 'x', 'y', 'z']
None
None
{% endhighlight %}
</section>

<section markdown="block">
### Removing Elements from a List

* __remove__(value) removes the first occurrence of the value from a list, but it causes an error if that value isn't in the list
* __pop__() # removes the last element of a list and returns it

__remove__ vs __pop__: both remove and pop change values in place (that is, the original object will be modified).  However, __remove__ does not return anything... while __pop__ returns the removed element.
</section>

<section markdown="block">
### Removing Elements From a List Example

__what does this code output? &rarr;__

{% highlight python %}
{% include classes/21/remove_and_pop.py %}
{% endhighlight %}

</section>

<section markdown="block">
### Removing Elements From a List Example - Output

{% highlight python %}
[2, 5, 3, 7]
None
[2, 5, 3]
7
Traceback (most recent call last):
  File "remove_and_pop.py", line 10, in <module>
    primes.remove(11)
ValueError: list.remove(x): x not in list
{% endhighlight %}
</section>


<section markdown="block">
### Count and Sort

* __count__(value) - returns the number of times a value is found in a list
* __sort__() - sorts a list in place (that is, the object that this method was called on is modified)
* __index__(object) - returns the index of the object supplied; causes an error if the object doesn’t exist 

__count__ returns an  int.  __sort__ does not return a value; it acts on the original object.

</section>

<section markdown="block">
### Count and Sort Example

__what does this code output? &rarr;__

{% highlight python %}
{% include classes/21/count_and_sort.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[4, 5, 5, 6]
None
2
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Built-in Functions: len() 

* len returns the length of a sequence type:  
* in the context of a string, it will give back the length of a string (the number of characters)
* in the context of a list, it will give back the number of elements in a list
* consequently, for both strings and lists, len(object) - 1 gives back the last index of a string or a list
* __it's not a method!__, it's just a built in function
	* you don't call it on an object
	* instead, you pass an argument as an object to it
	* why?  for consistency across built-in objects and custom objects
	* see [Principle of Least Astonishment](http://lucumr.pocoo.org/2011/7/9/python-and-pola/)
</section>

<section markdown="block">
### len() 

__what does this code output? &rarr;__

{% highlight python %}
{% include classes/21/len_function_example.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
3
0
franc
Traceback (most recent call last):
  File "len_function_example.py", line 6, in <module>
    print(defunct_currency[len(defunct_currency)])
IndexError: list index out of range
{% endhighlight %}
</div>
<!-- no_print -->
</section>

<section markdown="block">
### Built-in Statement: del

__del__ is a statement removes an element or slice of elements from a list:  

* it's neither a method or a function call; it's a statement (like return)
* to use __del__, use the keyword, __del__ followed by an indexed list or a sliced list
* del removes the elements _in place_ (that is, the original list is modified)
* an error occurs if you delete something that's out of range
</section>

<section markdown="block">
### del Example

__what does this code output? &rarr;__

{% highlight python %}
{% include classes/21/del_statement_example.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[2, 5]
Traceback (most recent call last):
  File "del_statement_example.py", line 5, in <module>
    del numbers[3]
IndexError: list assignment index out of range
{% endhighlight %}
</div>
</section>

<section markdown="block">
### del vs remove()

Both __del__ and __remove__() remove elements from a list, and they both do it in place.  However...

* __del__ removes by index
* __remove__() removes by value
* __del__ is a statement while __remove__ is a method
</section>

<section markdown="block">
### split and join

There are two useful __string methods__ that are often used with lists:

* __split__ turns a string into a list based on a separator string
* __join__ turns a list into a string based on the string it's called on
* __both are called on string objects!__
* __what would the following code output? &rarr;__

{% highlight python %}
comics = "ranma,maison ikkoku,scott pilgrim"
awesome_comics_list = comics.split(",")
print(awesome_comics_list)
print(" and ".join(awesome_comics_list))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['ranma', 'maison ikkoku', 'scott pilgrim']
ranma and maison ikkoku and scott pilgrim
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lengths of Names

__Implement a short program that: &rarr;__ 

* asks the user for a comma separated list of names
* prints out length of each name entered

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/21/lengths_of_names.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Random - Choice, Shuffle

The random module offers some methods that can be used on lists:

* __choice__(my_list): retrieves a random item from the supplied list
* __shuffle__(my_list): randomly changes the order of the elements in the list passed in (_in place_)

__Let's try using a couple of these methods &rarr;__

{% highlight python %}
import random
numbers = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(numbers))
random.shuffle(numbers)
print(numbers)
{% endhighlight %}
</section>

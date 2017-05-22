---
layout: slides
title: Mutability, References, and Aliasing 
---
<section markdown="block" class="title-slide">
# Mutability, References, and Aliasing
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Mutability

An object is _mutable_ if you can modify or change its data.
</section>

<section markdown="block">
### Mutability - Strings and Lists

* __Are strings mutable? &rarr;__
* __Are lists mutable? &rarr;__

<div class="incremental" markdown="block">
* strings __cannot be changed__; they are __immutable__.
* lists __can be changed__; they are mutable
</div>
</section>

<section markdown="block">
### Strings vs Lists... Indexing and Assignment

__What's the output of the following code? &rarr;__

{% highlight python %}
{% include classes/21/indexing_and_assignment.py %}
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
[1, 1, 3]
Traceback (most recent call last):
  File "indexing_and_assignment.py", line 5, in <module>
    b[1] = "1"
TypeError: 'str' object does not support item assignment
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lists, Indexing and Assignment

You can change values in a list!

* index into the list
* use the assignment operator (=)
* example:

{% highlight python %}
really_famous_cats = ["nermal", "felix", "sylvester"]
really_famous_cats[0] = "garfield"
# assignment works just fine!
{% endhighlight %}
</section>

<section markdown="block">
### List Methods vs String Methods

The behavior of the methods in lists and strings are consistent with the mutability of each type:

* string methods __don't change the object they're called on__; they return a new value
* list methods usually __change the object they're called on__; they change the object in place
</section>

<section markdown="block">
### List Methods vs String Methods Example

__What does this code output? &rarr;__
{% highlight python %}
{% include classes/21/list_string_methods.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
one two three
ONE TWO THREE
[1, 2, 3]
None
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Variables 

__What's a variable? &rarr;__

<div class="incremental" markdown="block">
* a __variable__ is a name that __refers__ to a value
* note the wording; it's intentional
	* in other contexts, variables may be thought of as holding values
	* in Python, variables are references (that is, they point to) values
</div>
</section>

<section markdown="block">
### Variables as References

Imagine variables as names that point to objects:

{% highlight python %}
a = [1, 2, 3]
{% endhighlight %}

{% highlight pycon %}
a ------> [1, 2, 3]
{% endhighlight %}
</section>

<section markdown="block">
### Variables as References Continued

Assignment is just pointing a reference.  When a new value is assigned to a name, it's the reference that's being changed.  

In the following reassignment example, notice that there are no more names that reference the initial list, [1, 2, 3].

{% highlight python %}
a = [1, 2, 3]
a = [4, 5, 6]
{% endhighlight %}

{% highlight pycon %}
          [1, 2, 3]

a ------> [4, 5, 6]
{% endhighlight %}
</section>

<section markdown="block">
### Aliasing

When one variable is assigned to another variable, both variables end up referring to the same object:

{% highlight python %}
a = [1, 2, 3]
b = a
{% endhighlight %}

{% highlight pycon %}
a ---+ 
     |--> [1, 2, 3]
b ---+ 
{% endhighlight %}

</section>

<section markdown="block">
### Aliasing Continued

The actual list object, [1, 2, 3], now has two names that refer to it.  Referencing the same object with more than one name is called __aliasing__.  

In the code below, a and b refer to the same list.  __What will the values of a and b be if we append 4 to b? &rarr;__

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
See in [python tutor](http://pythontutor.com/visualize.html#code=a+%3D+%5B1,+2,+3%5D%0Ab+%3D+a%0Ab.append(4)&mode=display&cumulative=false&py=3&curInstr=0)
</div>
</section>

<section markdown="block">
### Aliasing Continued Some More!

__Aliasing causes side effects in mutable objects!__  However, if an object is immutable, like a string, these side effects don't occur (since the object can't be changed anyway!).  __What gets printed out here? &rarr;__

{% highlight python %}
a = "hello" 
b = a
b.upper()
print(a)
print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
hello
hello
# b never changed, so neither did a
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And if Aliasing Was Not the Intention

If you'd like to make a new list rather than refer to the same list (that is have each variable point to a different object - though two equal objects)...

{% highlight pycon %}
a ------> [1, 2, 3]

b ------> [1, 2, 3]
{% endhighlight %}

...you can use list slicing, which always gives back a new list.  Creating a new list that is equivalent to, but a different object from the original, is called __cloning__.
</section>

<section markdown="block">
### Cloning

You can slice out the entire list to clone a list from the start index (0) to end index (len(list_of_elements) - 1):

{% highlight python %}
a = [1, 2, 3]

# cloned!
b = a[0:3]
{% endhighlight %}

Alternatively, there's shortcut to slicing out the whole string (without having to deal with precise start and end indexes)... 

__Just leave out the start and end (m, n) index from the slice.__

{% highlight python %}
b = a[:]
{% endhighlight %}
</section>

<section markdown="block">
### And What About Functions?

When parameters are passed to functions the value is a reference!  __What will this code print out? &rarr;__

{% highlight python %}
{% include classes/21/functions_lists_references.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2, 3, 1]
{% endhighlight %}
See in [Python tutor](http://pythontutor.com/visualize.html#code=numbers+%3D+%5B1,+2,+3%5D%0A%0Adef+add_four_to_list(a)%3A%0A++++a.append(4)%0A++++%0Aadd_four_to_list(numbers)&mode=display&cumulative=false&py=3&curInstr=0)
</div>
</section>

<section markdown="block">
### Kind of Important

__Changes made to a mutable object that's an argument to a function can be seen both within and outside of the function (all refer to  the same object!).__ &rarr;


The following function finds the largest integer in a list of integers, but it inadvertently sorts the original.

{% highlight python %}
# hm... maybe not the best way to find the greatest, but ...
def find_greatest(numbers):
    numbers.sort()
    return numbers[-1]

my_numbers = [5, 6, 1, 4]
greatest = find_greatest(my_numbers)

#hey wait a second, this isn't the original list!
print('original list:', my_numbers)
print(greatest)
{% endhighlight %}

</section>


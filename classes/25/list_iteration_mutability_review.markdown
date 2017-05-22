---
layout: slides
title: References, Aliasing, and Indexes 
---
<section markdown="block" class="title-slide">
# References, Aliasing, and Indexes
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Aliasing 

In the following code, a and b refer to the same object.  The object is a list, which is a __mutable__ type.  __What will be printed out in the following code?__ &rarr;

{% highlight python %}
a = [5, 3, 7]
b = a
b.sort()
print(a)
print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[3, 5, 7]
[3, 5, 7]
{% endhighlight %}
See in [python tutor](http://pythontutor.com/visualize.html#code=a+%3D+%5B5,+3,+7%5D%0Ab+%3D+a%0Ab.sort()%0A&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)
</div>
</section>

<section markdown="block">
### Aliasing Continued

It's not the same thing for immutable objects though. 

{% highlight python %}
a = "hello" 
b = a
b.upper()
print(a)
print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# upper doesn't change the original string anyway!
hello
hello
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Cloning

If you'd like to copy a list (rather than alias), you can __clone__ a list by using __slicing__.  

* you can slice out the entire list to clone a list 
* go from the start index (0) to end index (len(list_of_elements) - 1):

{% highlight python %}
a = [1, 2, 3]

# cloned!
b = a[0:3]
{% endhighlight %}

__Alternatively, leave out both m and n:__ 

{% highlight python %}
b = a[:]
{% endhighlight %}
</section>

<section markdown="block">
### In Functions...

When you pass a list as an argument to a function: 

* you're actually passing a reference to the list
* parameter passing creates an alias 

__What will this code print out? &rarr;__

{% highlight python %}
{% include classes/21/functions_lists_references.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2, 3, 1]
{% endhighlight %}
See in [Python tutor](http://pythontutor.com/visualize.html#code=numbers+%3D+%5B1,+2,+3%5D%0A%0Adef+add_four_to_list(a)%3A%0A++++a.append(4)%0A++++%0Aadd_four_to_list(numbers)&mode=display&cumulative=false&py=3&curInstr=0)
</div>

<!--_-->
</section>

<section markdown="block">
### Changing in Place

It's possible to create a function that modifies the parameter that was passed in.  Both a (outside of the function) and number (within the function) point to the same actual object.  In this case, there's no return value; instead the list is modified in place (nothing is returned).

__What do you think the output of this code is?__ &rarr;

{% highlight python %}
a = [1, 2, 3]
def one_less(numbers):
	for i in range(len(numbers)):
		numbers[i] = numbers[i] - 1

one_less(a)
print(a)
{% endhighlight %}

<div class='incremental' markdown='block'>
{% highlight python %}
[0, 1, 2]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Square Every Element

__Create a function called squared; implement it two different ways:__ &rarr;

* returns a new list
	* the new list contains every element squared
* modifies the list in place
	* every element in the list passed in should be overwritten with the square of that element
</section>

<section markdown="block">
### Square Every Element (New List)

{% highlight python %}
def squared(numbers):
	new_numbers = []
	for number in range(len(numbers)):
		new_numbers.append(number * number)
	return new_numbers
a = [1, 2, 3]
b = squared(a)
print(a)
print(b)
{% endhighlight %}
</section>

<section markdown="block">
### Square Every Element (In Place)

{% highlight python %}
a = [1, 2, 3]
def squared(numbers):
	for i in range(len(numbers)):
		numbers[i] = numbers[i] * numbers[i]
b = squared(a)
print(a)
print(b)
{% endhighlight %}
</section>

<section markdown="block">
### Iterating Over Every Item in a List

__What is the code that we would use to print out every element in the following list?__ &rarr;

{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
for name in names:
	print(name)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Indexes

__What code would we use to print out the 1st element in the following list, and then the 2nd element?__ &rarr;

{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
print(names[0])
print(names[1])
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Indexes Continued

__In the previous example, what type was the index?  Are indexes sequential or random?__

<div class="incremental" markdown="block">
* list indexes are __ints__
* indexes are __sequential and consecutive__
</div>

</section>

<section markdown="block">
### Iteration and Indexes

__Is it possible to generate the indexes used in the print statements below without hardcoding the values?  If so, how?__ &rarr;

{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
print(names[0])
print(names[1])
{% endhighlight %}

<div class="incremental" markdown="block">
* use a for loop and range to generate sequential and consecutive ints
* use a while loop loop to generate ints
* use the built-in function enumerate to get indexes
</div>
</section>

<section markdown="block">
### For Loops and Indexes

__Use a for loop to print out every element in the list below, with the index of the element before it.__ &rarr;

{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
"""print out...
0 Mabel
1 Dipper
2 Stan
"""
{% endhighlight %}

<div class='incremental' markdown='block'>
{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
for i in range(0, len(names)):
	print(i, names[i])
{% endhighlight %}
</div>
</section>

<section markdown="block">
### While Loops and Indexes

__How can we generate indexes with a while loop?__ &rarr;

{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
"""print out...
0 Mabel
1 Dipper
2 Stan
"""
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
i = 0
while i < len(names):
	print(i, names[i])
	i += 1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Enumerate

We also looked at a built in function called __enumerate__.  

* it takes a list
* it returns an _iterable_ object
	* yields a tuple on each loop
	* 1st element of tuples is the index of an item in the original list
	* 2nd element of tuple is the actual item in the original list

{% highlight python %}
names = ["Mabel", "Dipper", "Stan"]
t = enumerate(names)
for i, name in t:
	print(i, name)
{% endhighlight %}
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

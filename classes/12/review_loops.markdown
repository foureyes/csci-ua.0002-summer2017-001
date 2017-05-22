---
layout: slides
title: For Loops, For vs While 
---
<section markdown="block" class="title-slide">
# Review For Loops, For vs While
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### For Loops

__What's a for loop? &rarr;__

<div class='incremental' markdown="block">

A __for loop__ is a statement that allows a chunk of code to be executed repeatedly.  This repetition is achieved by iterating over every item in an iterator / __iterable object__.  

</div>

</section>

<section markdown="block">
### Iterable Objects 

An _iterable object_:

* is a _thing_ (_object_) that contains other values / _members_
* is capable of returning each of its members __one at a time__
* examples of iterable objects include: 
	* strings
	* lists
	* __range objects__
</section>


<section markdown="block">
### Range and Range Objects

__What's a range object and how is it created? &rarr;__

<div class='incremental' markdown="block">

* a __range__ object a data type that represents an arithmetic sequence, such as 2, 4, 6, 8
* range objects are created by using the built-in range() function.
</div>
</section>

<section markdown="block">
### Range Objects Continued

Range objects can take one to three arguments.  __What happens when you call range with one, two, and three arguments? &rarr;__

<div class='incremental'>
{% highlight python %}
stop = 10
a = range(stop)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

start, stop = 5, 10
b = range(start, stop)
# 5, 6, 7, 8, 9

start, stop, step = 5, 10, 2
c = range(start, stop, step)
# 5, 7, 9
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Some Things to Remember

* _stop_ argument in all three forms specifies the value that the sequence goes up to but does not include
* _start_ argument is the first element of the sequence
* a negative _step_ means count backwards

{% highlight python %}
print(list(range(8, -1, -2)))
{% endhighlight %}
</section>

<section markdown="block">
### Guess the Sequence

__What is the start, stop, and step?  What is the resulting arithmetic sequence? &rarr;__

<div class="incremental" markdown="block">

{% highlight python %}
range(50, 0, -10)
{% endhighlight %}
{% highlight python %}
# start:50, stop:0, step:-10
# 50, 40, 30, 20, 10
{% endhighlight %}

{% highlight python %}
range(4)
{% endhighlight %}
{% highlight python %}
# start:0, stop:4, step: 1
# 0, 1, 2, 3
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Ladder Plz

__Write a program that prints out an ascii art ladder.__

* ask for a height
* print out a ladder with that many rungs
	* can you implement using a for loop and printing out on each iteration?
	* or how about just string multiplication?

{% highlight python %}
height plz 
> 3
 ========
 |      |
 ========
 |      |
 ========
 |      |
{% endhighlight %}
</section>

<section markdown="block">
### Ladder Plz

{% highlight python %}
rungs = int(input('height plz\n> '))
for rung in range(rungs):
    print('========\n|      |')

rungs = int(input('height plz\n> '))
print('========\n|      |\n' * rungs)
{% endhighlight %}
</section>

<section markdown="block">
### Ladder Plz, Added Twist

Uh-oh.  Our ascii ladders are crummy.  Every rung has a 1 in three chance of being broken.  __How would you draw a ladder where each rung could potentially be broken? &rarr;__

{% highlight python %}
height plz
> 5
========
|      |
========
|      |
=~   .~=
|      |
========
|      |
=~   .~=
|      |
{% endhighlight %}
</section>

<section markdown="block">
### Ladder Plz, Added Twist

A potential solution...

{% highlight python %}
import random
rungs = int(input('height plz\n> '))
for rung in range(rungs):
    broken = random.randint(1, 3)
    if broken == 1:
        print('=~   .~=\n|      |')
    else:
        print('========\n|      |')
{% endhighlight %}
</section>

<section markdown="block">
### For Loops...

__When should you use them? &rarr;__

<div class="incremental" markdown="block">
* you know ahead of time how many iterations you'll have to go through
* you have to go through every element in an _iterable_ object 
	* every number in a sequence of numbers
	* every _item_ in a list
	* every character in a string
</div>
</section>

<section markdown="block">
### While Loops

__When should you use them? &rarr;__

<div class="incremental" markdown="block">
* when you don't know how many iterations you'll have to go through!
* when you must repeat something until some condition is met
* generally not a great option for counting (need to keep track of counter separately)
</div>
</section>


<section markdown="block">
### Let's Try Using Both...
* count to 0 to 25 by 5's
	* implement using while
	* implement using for
* print out a series of numbers, each randomly chosen from (1 through 10) that add up to 50 (you can go over)
	* implement using while
	* implement using for
</section>

<section markdown="block">
## [Nested Loops](nested.html)
</section>

---
layout: slides
title: For Loops 
---
<section markdown="block" class="title-slide">
# While Loops, Quick Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### While Loop Syntax

__How does it go again? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
"""
while <some condition>:
    <do stuff>
"""
{% endhighlight %}
{% highlight python %}
a = 1
while a == 1:
	print(a)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Sentinel Variables 

We also talked about variables that hold state outside of the loop.  These variables can be used to control whether or not the condition is met.  We saw this sample last week.  __What does this program output? &rarr;__

{% highlight python %}
keep_on_going = True
while keep_on_going:
	print "I'm going!"
	keep_on_going = False
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
I'm going!
{% endhighlight %}
</div>
</section>


<section markdown="block">
## EASY, right?

</section>

<section markdown="block">
### Try Counting the Digits in a Number

<aside>(this is in How to Think Like a Computer Scientist)</aside>

__Write a program that prints out number of digits in a number: &rarr;__

* ask the user for a number
* convert the input to an integer (don't just use len()!)
* count the digits
* print out the count
</section>

<section markdown="block">
### Let's See What This Does!

Example Output:

{% highlight python %}
"""
please enter a number
> 5
1

please enter a number
> 5432
4
"""
{% endhighlight %}
</section>

<section markdown="block">
### What About Some Pseudocode?

__Let's try designing our solution / writing some pseudocode before diving into actual coding.  &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
"""
ask the user for a number
while the number isn't 0 yet...
    set the number equal to the number over 10
    (this will be one place less)
    keep track of the number of times we divide by 10     
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Solution for Counting Digits

{% highlight python %}
{% include classes/09/places.py %}
{% endhighlight %}
</section>

<section markdown="block">
## [for](for.html)
</section>

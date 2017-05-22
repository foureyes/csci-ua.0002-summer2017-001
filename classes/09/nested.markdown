---
layout: slides
title: Nested Loops
---
<section markdown="block" class="title-slide">
# You Can Loop Within a Loop!
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Nested Loops

A __nested loop__ is just a loop inside the body of another loop.

It's loops [all the way down](http://en.wikipedia.org/wiki/Turtles_all_the_way_down).

</section>

<section markdown="block">
### Nested Loops Example

__What does this print out? &rarr;__

{% highlight python %}
for max in range(2, 5):
	count = 1
	while count < max:
		print(count)
		count += 1
	print('--')
{% endhighlight %}
<div class="incremental">
{% highlight python %}
1
--
1
2
--
1
2
3
--
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Make Me a Passowrd, Plz

__Let's create a password generator:&rarr;__

* the program will ask the user for a password length
* if the user enters a number greater than 0, it will generate a password:
	* the password will be the length that the user specified
	* each character will be a digit from 0 through 9
	* the new password will be generated
* the program will continue to ask the user for a password length 
* ... and loop until the user enters 0 for the password length
* (that is, exit if the user enters 0)
* implement with a for loop nested inside a while loop

</section>

<section markdown="block">
### Password Generator Example Output

{% highlight python %}
Please enter a password length (0 to exit)
>10
2402991612
Please enter a password length (0 to exit)
>5
60773
Please enter a password length (0 to exit)
>2
72
Please enter a password length (0 to exit)
>0
{% endhighlight %}
</section>

<section markdown="block">
### Password Generator Solution

{% highlight python %}
{% include classes/09/pwgen.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Nested for Loops

__What does this code output? &rarr;__

{% highlight python %}
print('i j\n-----')
for i in range(2):
	for j in range(4):
		print(str(i), str(j))
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
i j
-----
0 0
0 1
0 2
0 3
1 0
1 1
1 2
1 3
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Breaking Down Nested Loops

* the inner most loop must finish iterating before the outer loop goes on to its next iteration
* both loop variables are accessible in the body of the innermost loop
</section>

<section markdown="block">
### Triangle

__Try to draw this shape by using nested for loops: &rarr;__

{% highlight python %}
"""
*
**
***
****
*****
"""
{% endhighlight %}

* note that the first row has 1 star, the second has 2 stars, etc.
* try accumulating strings into a row using the inner loop
</section>

<section markdown="block">
### Potential Solution for Triangle

{% highlight python %}
{% include classes/09/triangle.py %}
{% endhighlight %}

</section>

---
layout: slides
title: Break and Continue 
---

<section markdown="block" class="title-slide">
# Break and Continue
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Break

The __break__ statement:

* when encountered in the body of a loop... 
* immediately causes the loop to end
* works for both for and while loops

</section>

<section markdown="block">
### Break Example

Using break in a for loop to: 

* roll a six sided die at most 10 times
* stop rolling as soon as a 1 is rolled 

__Let's try running this a few times__ &rarr;
{% highlight python %} 
import random
for i in range(10):
	roll = random.randint(1, 6)
	print(roll)
	if roll == 1:
		break

{% endhighlight %}
</section>

<section markdown="block">
### Break Question \#1

__What does this code output?__&rarr;
{% highlight python %} 
for i in range(5):
	print(i)
	if i > 1:
		break

print('fin')
{% endhighlight %}

<div class="incremental" markdown="block">
Stops looping after first iteration because of break...

{% highlight python %} 
0
1
2
fin
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Break Question \#2

__Fill out the body of this while loop so that it stops asking continue when the input is exactly 'n'.__&rarr;

* keep asking continue
* stop asking when input is 'n'
* use existing code (the while loop)
* use break

{% highlight python %} 
while True:
	keep_going = input('Continue?\n>')
	# your code goes here

print('done')
{% endhighlight %}


</section>

<section markdown="block">
###  Break Question \#2 Potential Solution
{% highlight python %} 
while True:
	keep_going = input('Continue?\n>')
	if keep_going == 'n':
		break

print('done')
{% endhighlight %}
</section>

<section markdown="block">
###  Approximating Square Root

You can calculate a square root by hand using __Newton's method for finding square roots__.

* start with almost any approximation
* a better approximation can be found with the following formula

{% highlight python %}
# original_number is the number that we're trying to find the sqrt of
# current_guess is the current candidate for result of sqrt
# better_guess is a slightly better approximation / guess

better_guess = (current_guess + original_number/current_guess)/2
{% endhighlight %}

* this formula can be repeatedly applied until the difference between the consecutive better approximations reaches some threshold
</section>

<section markdown="block">
###  Approximating Square Root

__Write a program the approximates the square root by using the method described in the previous slides. &rarr;__

* ask the user for a number
	* make an initial guess at the square root by taking number / 2
* use Newton's method to refine guess
	* loop forever
	* iteratively create a new_guess by: new_guess is (guess + original_number / guess) / 2
	* once the difference between the new guess and the old guess is 0.0001, stop (use built in absolute value function, __abs__)
	* reset current guess to new_guess before going to next iteration

{% highlight python %}
square root calculator
enter a number
> 25
5.000000000016778
{% endhighlight %}
</section>

<section markdown="block">
###  Approximating Square Root Potential Solution

{% highlight python %}
{% include classes/12/newtons.py %}
{% endhighlight %}
</section>

<section markdown="block">
###  Tell me When to Stop

__Count down from 10 to 1...&rarr;__

* after each number, ask the user if they want to stop
* if the user says stop, immediately exit the loop
* use break to do this

<div class='incremental'>
{% highlight python %} 
10
type 'stop' to end countdown!
> 
9
type 'stop' to end countdown!
> 
8
type 'stop' to end countdown!
> stop
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Tell me When to Stop Solution

{% highlight python %}
{% include classes/12/countdown.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Continue

The __continue__ statement immediately skips to the next iteration of the loop.  This works for both for and while loops.

{% highlight python %} 
for i in range(4):
	if i == 1:
		continue
	print(i)
{% endhighlight %}
</section>

<section markdown="block">
### Counting (Yet Again)

__Count to 15 by 1s, skip multiples of 3.  Use continue.  &rarr;__

(yeah, you can do this without continue too).

{% highlight python %} 
1
2
4
{% endhighlight %}
</section>

<section markdown="block">
### Counting (Yet Again)

A solution using continue.

{% highlight python %} 
{% include classes/12/skip5.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Counting (Another)

__Count to 30 by 3's, skip all 20's &rarr;__

{% highlight python %} 
0
3
6
9
12
15
18
21
24
27
30
{% endhighlight %}
</section>

<section markdown="block">
### Counting (Another)

A solution using continue...

{% highlight python %} 
{% include classes/12/twenties.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Break and Continue

* generally, you can use a while with some condition as an alternative to break
* you can also potentially use an if statement with a different boolean expression as an alternative to continue
* some texts discourage the use of break and continue (or at least, overuse of)
	* could lead to many points of exit
	* complex code
</section>

<!--
<section markdown="block">
## [Turtle](turtle.html)
</section>
-->

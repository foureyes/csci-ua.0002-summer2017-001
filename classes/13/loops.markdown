---
layout: slides
title: Loops Recap 
---
<section markdown="block" class="title-slide">
# Loops Recap
{% include title-slide-footer.html %}
</section>

<section markdown="block">
## Super Quick Review Before we Move On

</section>


<section markdown="block">
### Repeating Blocks of Code

Python has two looping structures:

* __while__ - a _condition controlled_ loop that repeats a block of code as long as a condition (a boolean expression) is True
* __for__ - a _count controlled_ loop that repeats a block of code for a specific number of times
</section>

<section markdown="block">
### While Loops

{% highlight python %}
while some_boolean_expression:
	print("repeat an indented block of code")
{% endhighlight %}

* repeats the indented body of code as long as condition (some boolean expression) is true
* __if there's something wrong__ with the loop stopping or not stopping, __check the condition__ 
* if you want the loop to stop, must have something that influences the condition:
	* for example, counting requires that we maintain a count variable outside of the loop 
	* another example, looping on input means keeping track of what a user types in
</section>

<section markdown="block">
### For Loops

{% highlight python %}
for loop_variable in iterable_object:
	print("repeat an indented block of code")
{% endhighlight %}

* iterates over every element in an _iterable_ object
* an __iterable object__ can be composed of multiple elements and is capable of _yielding_ each element one at a time 
* a __range__ is an iterable object that represents an arithmetic sequence of numbers
* __loop variable__ represents the current element of the iterable object
* no need to explicitly increment the loop variable
</section>

<section markdown="block">
### Controlling Loops

Python has two constructs to change the flow of a loop:

* __break__ - immediately stops the loop from running and _jumps_ out of the loop 
* __continue__ - go to the next iteration of the loop
</section>

<section markdown="block">
### break

* the break statement is used to immediately leave the body of the loop that it is in
* the next statement to be executed is the first one after the body of the loop

__What is the output of the following code?__ &rarr;

{% highlight python %}
for i in range(5, 21, 5):
	if i % 3 == 0:
		break 
	print(i)
print("done")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
5
10
done
{% endhighlight %}
</div>
</section>

<section markdown="block">
### continue

* the continue statement causes the program to immediately skip the processing of the rest of the body of the loop
* ...but instead of jumping out of the loop, it _continues_ on to the next iteration

__What is the output of the following code?__ &rarr;

{% highlight python %}
for i in range(5, 21, 5):
	if i % 3 == 0:
		continue 
	print(i)
print("done")
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
5
10
20
done
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Nested Loops

Lastly, we've talked about nested loops.

* a nested loop is just a loop within the body of another loop
* for every iteration of the outer loop, the inner loop must finish all of its iterations

</section>

<section markdown="block">
### Squares!

* __what are the x, y coordinates of the first square?__ &rarr;
* __... and the second square?__ &rarr;
* __... and the last square?__ &rarr;

{% highlight python %}
import turtle
t, wn = turtle.Turtle(), turtle.Screen()
size, spacing = 20, 5
step = size + spacing
for y in range(0, -201, -step):
    for x in range(0, 201, step):
        t.up()
        t.goto(x, y)
        t.down()
        # draw a square
        for line in range(4):
            t.forward(size)
            t.left(90)
wn.mainloop()
{% endhighlight %}

The first is at (0, 0), second is at (0, 25).
</section>

<section markdown="block">
### Squares! Answers

* __the first square is drawn at (0, 0)__
* __the second square is drawn at (0, 25)__
* __the last square is drawn at (-200, 200)__

{% highlight python %}
t, wn = turtle.Turtle(), turtle.Screen()
size, spacing = 20, 5
step = size + spacing
for y in range(0, -201, -step):
    for x in range(0, 201, step):
        t.up()
        t.goto(x, y)
        t.down()
        # draw a square
        for line in range(4):
            t.forward(size)
            t.left(90)
wn.mainloop()
{% endhighlight %}

__Let's try this out!__ &rarr;
</section>

<section markdown="block">
## [Turtle Review](turtle_review.html)
</section>



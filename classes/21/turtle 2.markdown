---
layout: slides
title: Turtle 
---
<section markdown="block" class="title-slide">
# Turtle 
{% include title-slide-footer.html %}
</section>


<section markdown="block">
### Turtle 

__What's turtle?__

<div class="incremental" markdown="block">
* that allows you to draw programmatically
	* virtual pen plotter
	* commands are given to a movable pen
* provides functions and __objects__ for drawing
	* objects include screen, turtle, etc.
	* methods on those objects move the turtle, set the pen color, pick up the pen, etc.
</div>
</section>

<section markdown="block">
### Using the turtle Module
__Describe the basic steps for using the turtle module (what's the pseudocode) &rarr;__

<div class="incremental" markdown="block">
1. bring in the turtle module
2. create a Screen object
3. create at least one Turtle object 
4. tell the Screen object to start the program
</div>
</section>

<section markdown="block">
### Actual Code

__And for the real code? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/10/template.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Quick Run Through What the Code Does...

bring in the turtle module
{% highlight python %}
import turtle
{% endhighlight %}
create a Screen object (this provides a canvas to draw on, and some window related commands)
{% highlight python %}
wn = turtle.Screen()
{% endhighlight %}
create a Turtle object to draw with
{% highlight python %}
leo = turtle.Turtle() # then do stuff with your new turtle!
{% endhighlight %}
start the program!
{% highlight python %}
wn.mainloop()
{% endhighlight %}
</section>

<section markdown="block">
### Creating a Turtle Object

In the case of Turtle, there's no literal (like a string, int or list).  Instead, to create an object, you have to use something that looks like a function call (it's actually a __constructor__).  Calling Turtle() gives you back a Turtle object:

{% highlight python %}
leo = turtle.Turtle() 
{% endhighlight %}

</section>

<section markdown="block">
### A Few Things to Remember...

* the turtle starts at the center (0, 0)
* the turtle is facing right (imagine that it's looking east)
* positive x values are to the right of the origin, positive y, above
</section>

<section markdown="block">
### Basic Turtle Methods

These are all methods that you can call on your __Turtle__ object.

* __forward__(_distance_) - move the turtle forward by the specified _distance_
* __right__(_angle_) - turn the turtle right by _angle_ degrees
* __left__(_angle_) - turn the turtle left by _angle_ degrees
* __back__(_distance_) - move the turtle back by the specified _distance_

{% highlight python %}
t.forward(200)
t.right(45)
{% endhighlight %}
</section>

<section markdown="block">
### Screen and Pen Drawing Attributes

Methods you can call on your __Turtle__ object:

* __color__(_colorstring_) - change the color of your _pen_ to _colorstring_, which can be "red", "green", etc.
* __pensize__(_size_) - change the size of your pen to _size_

{% highlight python %}
t.color("blue")
{% endhighlight %}

Methods you can call on your __Screen__ object

* __bgcolor__(_colorstring_) - change the background color of your window to _colorstring_
{% highlight python %}
wn.bgcolor("pink")
{% endhighlight %}
</section>

<section markdown="block">
### Moving Without Drawing

Methods you can call on your __Turtle__ object:

* __up__() - pick the pen up so that the turtle object doesn't draw when it moves
* __down__() - put the pen down so that the turtle object draws when it moves
{% highlight python %}
t.up()  # picks the pen up, doesn't draw when the turtle moves
{% endhighlight %}
</section>


<section markdown="block">
### Going Somewhere?

A method you can call on your __Turtle__ object:

__goto__(_x_, _y_) - move the turtle to the specified coordinates ..._x_ and _y_.  Note that if the pen is down, it will draw up to that coordinate.

{% highlight python %}
t.goto(200, 200)  # picks the pen up, doesn't draw when the turtle moves
{% endhighlight %}
</section>

<section markdown="block">
### Example Question #1

__What does this draw? &rarr;__

{% highlight pycon %}
>>> for i in range(4):
...   t.forward(100)
...   t.left(90)
{% endhighlight %}

<div class="incremental" markdown="block">
A square!
</div>
</section>

<section markdown="block">
### Example Question #2

__Finish this code to draw a square (same as previous)__
{% highlight pycon %}
for i in range(_____):
	t.forward(100)
	t._____________________
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight pycon %}
for i in range(4):
	t.forward(100)
	t.left(90)
	# or t.right(90)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Some Others

* create a function that...
* draw multiple...

</section>


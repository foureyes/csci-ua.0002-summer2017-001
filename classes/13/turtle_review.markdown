---
layout: slides
title: Turtle Review 
---
<section markdown="block" class="title-slide">
# Turtle Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Objects and Methods

First, let's take a step back and try to recall __objects__ and __methods__.

* __What's an object? &rarr;__
* __What's a method? &rarr;__
</section>

<section markdown="block">
### Objects

* __object__ - a _thing_ that a variable name can refer to
* all of the values in Python are _things_
* "hello" is a str object, 42 is an int object
* an __object__ can have __attributes__ ...data associated with an object
* an __object__ can have __methods__ ...actions that the object can perform
</section>

<section markdown="block">
### Methods

* a __method__ is essentially a function that's associated with a particular object
* you can _call_ a method just like a function... but you have to use the dot operator
* object.method() - it's similar to using a method in a module!
* for example: leo.forward(200) 
* ...means I'm calling the forward() function on an object called __leo__ (turns out, that's a _turtle_ object)

</section>

<section markdown="block">
### Turtle 

__turtle__ is a Python module...

* that allows you to draw programmatically
	* virtual pen plotter
	* commands are given to a movable pen
* a Python implementation of Logo
	* instead of a pen, it's called a turtle
	* (imagine a turtle that leaves tracks on a sandy beach!)
	* provides functions and __objects__ for drawing
		* objects include screen, turtle, etc.
		* methods on those objects move the turtle, set the pen color, pick up the pen, etc.
</section>

<section markdown="block">
### The Basic Steps for Using Turtle Are:

__Does anyone remember? (Doesn't have to be code... just describe what you would do) &rarr;__

<div class="incremental" markdown="block">
1. bring in the turtle module
2. create a Screen object
3. create at least one Turtle object 
4. tell the Screen object to start the program
</div>
</section>

<section markdown="block">
### Here's Some Template Code

You'll need to write this stuff every time you use turtle

{% highlight python %}
{% include classes/14/template.py %}
{% endhighlight %}
</section>

<section markdown="block">
### What Does That Code Do?

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
### Back to Objects
<aside>One last note regarding objects</aside>

Notice that the creation of an object looks like a function call.  Calling Turtle() gives back a Turtle object.

{% highlight python %}
leo = turtle.Turtle() 
{% endhighlight %}

</section>

<section markdown="block">
### The Drawing Environment

* we're drawing on a two-dimensional plane
* __where does the turtle start?__
* __which way is the turtle facing?__
* __where are the positive x values... and the positive y values__?

<div class="incremental" markdown="block">
* the turtle starts at the center (0, 0)
* the turtle is facing right (imagine that it's looking east)
* positive x values are to the right of the origin, positive y, above
</div>
</section>

<section markdown="block">
## Let's Draw!
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
### Let's Draw Some Simple Shapes 

Draw these simple shapes.  

* a triangle
	* with a side of length 100
	* interior angles should all be 120 (180 - 60)
	* with a yellow outline on a blue background
* two squares
	* each with a side of length 100
	* 10 pixels apart
	* with a purple outline the has a pensize of 5

</section>


<section markdown="block">
### Draw a House!

__Try drawing a house: a square with an equilateral triangle on top: &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/13/house.py %}
{% endhighlight %}
</div>
</section>


<section markdown="block">
## [Functions That Return Values](returning_values.html)
</section>


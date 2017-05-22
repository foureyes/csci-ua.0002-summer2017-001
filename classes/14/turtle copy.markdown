---
layout: slides
title: Turtle Graphics 
---
<section markdown="block" class="title-slide">
# Turtle Graphics
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Turtle

__turtle__ is a Python module...

* that allows you to draw programmatically
	* think of a virtual [pen plotter](http://blog.makezine.com/2011/05/06/sharpie-pen-plotter/)
	* commands are given to a movable pen
	* that pen can move and draw on a two dimensional plane
	* the pen is called a turtle!
* it's essentially a Python implementation of another language called [Logo](http://en.wikipedia.org/wiki/Logo_(programming_language))

</section>

<section markdown="block">
### Some History

So, what's this __Logo__ thing about?

* Logo is an __educational__ language
* one of its most well-known features is turtle graphics 
* built on theory of constructionist learning
	* learning by experimentation
	* learning by making tangible things!
* created in the mid 60's(!) by a group of computer scientists: Daniel G. Bobrow, Wally Feurzeig, Seymour Papert and Cynthia Solomon
</section>

<section markdown="block">
### Seymour Papert

* Papert, in particular, is well known for his work in education and computing
* developed an influential theory on learning called _[constructionism](http://en.wikipedia.org/wiki/Constructionist_learning)_
* was the director of the MIT Artificial Intelligence Laboratory
* besides inventing Logo, also collaborated with Lego (it's not confusing that that's one vowel away from Logo) on a robotics kit called [Mindstorms](http://en.wikipedia.org/wiki/Lego_Mindstorms)

</section>

<section markdown="block">
### (And Like Many Great Computer Scientists, He Has a Beard)

<div class="img-container" markdown="block">![Seymour Papert](../../resources/img/papert.jpg)
</div>

</section>

<section markdown="block">
### Great, So... Why Turtle?

Imagine you have turtle hanging out on the beach...

<div class="img-container" markdown="block">![Turtle](../../resources/img/turtle.jpg) 
</div>
</section>

<section markdown="block">
### Turtles Drawing Stuff

* imagine further that it's a robotic turtle (__AWESOME!__)
* ...that you can give commands to
	* move forward
	* turn around
* as it moves, it leaves tracks on the ground
* turtle graphics _simulates this_ (seriously)
	* your window is a sandy beach
	* the turtle, is... well... um... a turtle (a virtual robotic one)
</section>

<section markdown="block">
### What Does That Mean for Us?

So... in Python, we now have access to our own drawing turtle

* we can draw by writing code
* that code is analogous to the commands that we would give the turtle (or pen, or pointer, or _whatever_)
	* move forward
	* turn around
* but in addition, we can also
	* change colors
	* ask for user input
	* etc.
</section>

<section markdown="block">
### Hello Turtle
<aside>Enough Talk.  What Does This Code Actually Look Like?</aside>

This draws a line (that's exactly 200 pixels).  (exciting).  Let's try running it.
{% highlight python %}
{% include classes/12/hello.py %}
{% endhighlight %}
</section>

<section markdown="block">
### About the Drawing Environment

* obviously, we're drawing on a two-dimensional plane
* the turtle starts at the center
* the turtle is facing right (imagine that it's looking east)
* __can you guess what the coordinates (x and y values) are at the center__?
* __where are the positive x values... and the positive y values__?

</section>

<section markdown="block">
### About the Drawing Environment Continued

* you can use __leo.forward(200)__ as a clue!
* if that drew a 200 pixel line, then, maybe
* the center is at (0, 0)
* positive x values are to the right of the origin, positive y, above
* (yeah, maybe that's obvious, but some graphics packages have a different coordinate plane)
</section>

<section markdown="block">
### A Few Tips for Running Programs

Running these programs (from IDLE or from Terminal!) cause a new window to pop up.  You may encounter some minor annoyances:

* the window usually opens up behind the interactive shell (or Terminal)
* if there's an error, the window of your program may hang
	* close the interactive shell to get rid of it
	* ...or force quit the window
* your prints still show up in the shell, but you'll have to juggle two windows
</section>

<section markdown="block">
### Let's Dissect That Code

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
leo = turtle.Turtle()
{% endhighlight %}
</section>

<section markdown="block">
### Let's Dissect That Code Continued
tell the turtle to move forward 200 pixels
{% highlight python %}
leo.forward(200)
{% endhighlight %}
start the program!
{% highlight python %}
wn.mainloop()
{% endhighlight %}
</section>

<section markdown="block">
### Objects

So... I used the word __object__ there a few times.  What does that actually mean?

* __object__ - a _thing_ that a variable name can refer to, like a screen or a turtle
* ...in fact, all of the values in Python are things
* they're objects too: "hello" is a str object, 42 is an int object
* an __object__ can have __attributes__ ...data associated with an object
* an __object__ can have __methods__ ...which are basically things that the object can do
</section>

<section markdown="block">
### Methods

* a __method__ is essentially a function that's associated with a particular object
* you can _call_ a method just like a function... but you have to use the dot operator
* object.method() - it's similar to using a method in a module!
* for example: leo.forward(200) 
* ...means I'm calling the forward() function on the turtle object called leo
* in fact... we can see some methods on objects that we've used before!

{% highlight python %}
dir("hello")
{% endhighlight %}
</section>

<section markdown="block">
### Let's Look at That Code Again...
{% highlight python %}
{% include classes/12/hello.py %}
{% endhighlight %}
</section>

<section markdown="block">
### The Basic Steps Are...

What did we have to do?

1. bring in the turtle module
2. create a Screen object
3. create at least one Turtle object 
4. tell the Screen object to start the program
</section>

<section markdown="block">
### So, That's Some Boilerplate Stuff

We should probably convert our hello program into a template.  You'll need to write this stuff every time you create a program with turtle:

{% highlight python %}
{% include classes/12/template.py %}
{% endhighlight %}
</section>

<section markdown="block">
### A Note On Names

* in the template, I use __t__ as the variable name for my turtle.  
* it's just a variable name; it can be anything you want (same with __wn__, but you have to change wn everywhere you see it)
* in fact, in my previous programs, I called the turtle leo, in honor of one of these guys

<div class="img-container" markdown="block">![Turtle](../../resources/img/tmnt.gif) 
</div>

</section>

<section markdown="block">
## BTW, I Definitely Encourage You to Follow Along When I Code Up Examples!
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
### Forward, Right, Left, Back - Code

__BTW... what do you think this draws? &rarr;__

{% highlight python %}
{% include classes/12/basic.py %}
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
### Color, Background and Pen Size
{% highlight python %}
{% include classes/12/color.py %}
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
### Pen Up, Pen Down

__BTW... what do you think this draws? &rarr;__

{% highlight python %}
{% include classes/12/pen.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Going Somewhere?

A methods you can call on your __Turtle__ object:

__goto__(_x_, _y_) - move the turtle to the specified coordinates ..._x_ and _y_.  Note that if the pen is down, it will draw up to that coordinate.

{% highlight python %}
t.goto(200, 200)  # picks the pen up, doesn't draw when the turtle moves
{% endhighlight %}
</section>

<section markdown="block">
### Goto

__BTW... what do you think this draws? &rarr;__

{% highlight python %}
{% include classes/12/goto.py %}
{% endhighlight %}
</section>

<section markdown="block">
###  Let's Use What We Know to Create a Square!

__How would we tell the turtle to create a square with the upper left corner at the origin? Each side should be 200px long.  We just learned goto, so let's try that.&rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/12/square_goto.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Another Square!

__Same thing, but this time, just use forward or back and either left or right.  &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/12/square_basic.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### One Last Square!

__How can we simplify the previous version?  There was a lot of repeated code! &rarr;__

<div class="incremental" markdown="block">
Let's try it with loops!

{% highlight python %}
{% include classes/12/square_with_loops.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Confused Turtle

__Let's try incorporating random &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/12/confused.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Reviewing Objects and Methods

__What's an object and what's a method? &rarr;__

* __object__ - a _thing_ that a variable name can refer to, like a Screen, Turtle, int or str
* an __object__ can have __methods__ ... things that the object can do
* a __method__ is a function that you can call from a particular object
</section>

<section markdown="block">
### Again a Few Tips for Running Programs

Running these programs (from IDLE or from Terminal!) cause a new window to pop up.

* the window usually opens up behind the interactive shell (or Terminal)
* if there's an error, the window of your program may hang. __demo &rarr;__
	* close the interactive shell to get rid of it
	* ...or force quit the window
* your prints still show up in the shell, but you'll have to juggle two windows. __demo &rarr;__
</section>

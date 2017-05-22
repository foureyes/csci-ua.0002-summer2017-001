---
layout: slides
title: Turtle Animation 
---
<section markdown="block" class="title-slide">
# Turtle Animation
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Additional Turtle Methods

* __clear__() - removes drawing from screen
* __hideturtle__() - does not show turtle (triangle)
* __circle__(int) - draws a circle using supplied radius

{% highlight python %}
t.clear()
t.hideturtle()
t.circle(15)
{% endhighlight %}
</section>


<section markdown="block">
### Additional Screen Methods

* __tracer__(int) - when called with 0, turns off animation of turtle movement
* __update__() - when tracer is 0, use this to refresh the screen (show drawing)
* __ontimer__(function, int) - automatically call a function after some interval of time

{% highlight python %}
wn.tracer(0)
wn.update()
wn.ontimer(draw, 30)
{% endhighlight %}
</section>

<section markdown="block">
### Turtle/No Turtle Example

Hide turtle, no trace...

{% highlight python %}
import turtle

t, wn = turtle.Turtle(), turtle.Screen()

# turn animation of turtles off
# t.hideturtle()
# wn.tracer(0)

for i in range(100):
    t.forward(i * 2)
    t.left(45)

# wn.update()
wn.mainloop()
{% endhighlight %}
</section>

<section markdown="block">
### Timer

Create a draw function, call it every 50 milliseconds.

{% highlight python %}
import turtle
t, wn = turtle.Turtle(), turtle.Screen()
t.hideturtle()
wn.tracer(0)

def draw():
    t.up()
    t.forward(5)
    t.down()
    t.circle(20)

    # update screen
    wn.update()
    
    # call again in 50 milliseconds
    wn.ontimer(draw, 50)
draw()
wn.mainloop()
{% endhighlight %}
</section>

<section markdown="block">
### Uh.  Why?

We can sort of see where this is going.  To animate we'll need to:

* hide the turtle
* remove the animation for turtle movement
* continuously draw a new screen
</section>

<section markdown="block">
### Animation

Drawing a new screen at a set interval allows us to mimic frame by frame animation.  A flip book example:

[kind of ridiculous](http://www.youtube.com/watch?v=GTAhvKoF948)

</section>

<section markdown="block">
### Draw a Screen

{% highlight python %}
import turtle

def draw():

    # clear all drawings
    t.clear()
    t.up()
    t.goto(sprite['x'], sprite['y'])
    t.down()
    sprite['y'] -= 1
    t.circle(15)

    # update the screen because trace is off
    wn.update()

    # call this function again to redraw entire screen
    wn.ontimer(draw, 30)
{% endhighlight %}
</section>

<section markdown="block">
### Setup Code

{% highlight python %}
t, wn = turtle.Turtle(), turtle.Screen()

# don't show the turtle
t.hideturtle()

# turn animation of turtles off
wn.tracer(0)

# store x and y values in a mutable global variable
# so that they can be changed from draw function
# (rather than use globals keyword)
sprite = {'x':0, 'y':0}

# start off our draw function!
draw()

wn.mainloop()
{% endhighlight %}
</section>

<section markdown="block">
### And Another (with Acceleration!)
{% highlight python %}
def draw():
    t.clear()
    t.up()
    t.goto(sprite['x'], sprite['y'])
    t.down()
    sprite['y'] += sprite['dy']

    # change velocity based on acceleration
    sprite['dy'] += sprite['acc_y']
    t.circle(15)

    wn.update()
    wn.ontimer(draw, 30)
    
    # bounce!
    if sprite['y'] <= -250:
        sprite['dy'] *= -1
{% endhighlight %}
</section>

<section markdown="block">
### The Setup for Acceleration
{% highlight python %}
        
t, wn = turtle.Turtle(), turtle.Screen()

# don't show the turtle
t.hideturtle()

# turn animation of turtles off
wn.tracer(0)

# store x and y values in a mutable global variable
# so that they can be changed from draw function
# (rather than use globals keyword)
sprite = {'x':0, 'y':0, 'dy':-0.1, 'acc_y':-0.5}

# start off our draw function!
draw()

wn.mainloop()
{% endhighlight %}
</section>

---
layout: slides
title: Material from Homework
---
<section markdown="block" class="title-slide">
# Material from Homework, Homework Solutions
{% include title-slide-footer.html %}
</section>
<section markdown="block">
## Built-In Functions (from Homework)

</section>

<section markdown="block">
### Built-In Functions

Python has a bunch of built in functions that are available for you to use with importing a module. We've seen some of these before:

* __print__
* __bool__
* __str__
* __range__
* ...etc

__In the homework, you were asked to do research on some additional functions.__ In case you were unable to do this, the following slides will give a quick overview of how they work.
</section>

<section markdown="block">
### Built-In Functions Continued

Finding the length of a string and formatting a number:

* __len(sequence)__ - return the length of a sequence (for now, think of it as giving back the number of characters in a string)
	* len("a str") &rarr; 5
	* len("") &rarr; 0
* __format(number, specification)__ - formats a number based on a specification, which is the second argument. It can be used to indicate the number of places:
	* format(5.378, '.2f') &rarr; 5.38
	* format(5.378, '.4f') &rarr; 5.3780
</section>

<section markdown="block">
### Built-In Functions Continued Some More

Rounding and absolute value...

* __round(number, [precision])__ - round a number to a given precision in decimal digits (default is 0 digits). can have one or two arguments (the second representing precision):
	* round(5.32) &rarr; 5
	* round(5.32, 1) &rarr; 5
* __abs(number)__ - returns the absolute value of an argument
	* abs(-2) &rarr; 2 
	* abs(2) &rarr; 2 
</section>

<section markdown="block">
## Selected Homework Solutions

</section>

<section markdown="block">
###  Homework Solutions

__hw1__

* [tree.py](../../resources/code/hw1/tree.py)
* [miles.py](../../resources/code/hw1/miles.py)
* [mad_lib_lyrics.py](../../resources/code/hw1/mad_libs_lyrics.py)

__hw2__

* [days.py](../../resources/code/hw2/days.py)
* [candy_bars.py](../../resources/code/hw2/candy_bars.py)
* [numbers.py](../../resources/code/hw2/numbers.py)

</section>

<section markdown="block">
###  Homework Solutions Continued

__hw3__

* [distance.py](../../resources/code/hw3/distance.py)
* [fortune.py](../../resources/code/hw3/fortune.py)
* [tip.py](../../resources/code/hw3/tip.py)


__hw4__

* [dice.py](../../resources/code/hw4/dice.py)
* [guess.py](../../resources/code/hw4/guess.py)
* [average_word.py](../../resources/code/hw4/average_word.py)


</section>

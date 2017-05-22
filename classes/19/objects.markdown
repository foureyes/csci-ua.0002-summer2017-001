---
layout: slides
title: Objects and Methods 
---
<section markdown="block" class="title-slide">
# Objects and Methods
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Objects and Methods

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
### Examples of Objects

__What are some objects we've seen?__

<div class="incremental" markdown="block">
* essentially, all data that we've seen is an object! 
* int
* float
* str
* Turtle
* Screen
* etc
</div>
</section>

<section markdown="block">
### Objects vs Types

Aren't those just types?  Yes!  But to be more specific:

* a __type__ is a classification of data
* an __object__ is the data itself, referred to by a variable name
* an __object__ is an _instance_ of a type or class
* saying "xxxxx objects" (a _kind_ or _type_ of object) and "types" are interchangeable
</section>

<section markdown="block">
### Examples of Objects

__What are some methods we've seen (for Turtle, str and list objects?)__

<div class="incremental" markdown="block">
* Turtle 
	* forward(int)
	* up()
	* left(int)
	* etc.
* str
	* find(str)
	* upper()
	* isalpha()
	* isdigit()
	* etc.
* list
	* append(object)
	* pop()
	* etc.
</div>
</section>

<section markdown="block">
### Methods vs Functions

Aren't those just functions?  Yes!  Well, sort of:

* a __method__ is a __function__ within the context of an object
* a __method__ is called __on__ an object, so to call it, you must have an object around!
* use the object's name, the dot operator, and then call the method like you would a function
* sometimes methods _mutate_ the original object
* so far, we've only seen this behavior in lists (append, sort, etc.)
* otherwise, they may return a value (or both mutate and return a value, such as pop)
</section>

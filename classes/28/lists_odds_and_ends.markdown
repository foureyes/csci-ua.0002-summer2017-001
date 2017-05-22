---
layout: slides
title: Lists Odds and Ends Review 
---

<section markdown="block" class="title-slide">
# Lists Odds and Ends Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
<h3>Strings to Lists and Back</h3>

There are two useful __string methods__ that are often used with lists:

* __split__ turns a string into a list based on a separator string
* __join__ turns a list into a string based on the string it's called on
* __what would the following code output? &rarr;__

{% highlight python %}
comics = "ranma,maison ikkoku,scott pilgrim"
awesome_comics_list = comics.split(",")
print(awesome_comics_list)
print(" and ".join(awesome_comics_list))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['ranma', 'maison ikkoku', 'scott pilgrim']
ranma and maison ikkoku and scott pilgrim
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Split and Join

__If I have the following list, how do I put together each element with an exclamation point and space between each element? How do I turn the resulting string back to a list? &rarr;__

{% highlight python %}
hello = ["Bill", "Phil", "Gil", "Jill"]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
names = "! ".join(hello)
print(names)
print(names.split("! "))
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Random - Choice, Shuffle

The random module offers some methods that can be used on lists:

* __choice__(my_list): retrieves a random item from the supplied list
* __shuffle__(my_list): randomly changes the order of the elements in the list passed in (_in place_)

__Let's try using a couple of these methods &rarr;__
{% highlight python %}
import random
numbers = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(numbers))
random.shuffle(numbers)
print(numbers)
{% endhighlight %}
</section>

<section markdown="block">
### One Hand of Blackjack

* try implementing a single hand of blackjack
* use a commandline interface:
	* 'h' for hit / draw more cards
	* 's' for stay / stop drawing cards
* create a computer opponent that determines whether or not to keep getting cards

</section>

<section markdown="block">
### Break Down the Problem

* what data do we want to store, and how do we represent it?
* shuffling and distributing cards
* calculating a blackjack hand
* dealing with user input
* playing as the computer
* determining who won
</section>

<section markdown="block">
### Representing Data

__What data do we want to store, and how do we represent it?__

<div class="incremental" markdown="block">
* the card deck
* the player's hand, the computer's hand
* how about a list of strings to represent each card in a deck?
</div>
</section>

<section markdown="block">
### Shuffling and Distributing Cards

__Write a short program that:__ &rarr;

* creates a deck of cards as a list of strings: 1-9, A, K, Q, J (4 x for hearts, clubs, spades, clovers)
* mix up the deck
* distribute two cards to both the player and the computer

<div class="incremental" markdown="block">
{% highlight python %}
# create deck and deal
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)
player_hand = []
computer_hand = []
for i in range(2):
	player_hand.append(deck.pop())
	computer_hand.append(deck.pop())
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Calculating a Blackjack Hand

__Implement a function that takes a list of strings representing cards.  It should calculate the sum of the cards__

* represent cards as a list of strings: 1-9, A, K, Q, J
* face cards count as 10
* aces count as either 1 or 11... choose the value that brings the sum closest to 21
* implement a function that takes a list of strings
* it should return an integer that represents the total of the cards
* write pseudocode to determine how your function would choose 1 or 11
* write assertions (try multiple aces)
</section>

<section markdown="block">
### Let's Think of Some Algorithms

__How about this one?__ &rarr;

<div class="incremental" markdown="block">
* if it's a digit, just add it 
* if it's a face card, add 10
* if it's an ace, add 11
* ... but keep track of the number of aces
* as long as there are aces and the hand is over 21, subtract 10
</div>
</section>

<section markdown="block">
### Calculating a Blackjack Hand

{% highlight python %}
{% include classes/18/current_total.py %}
{% endhighlight %}
<!--  comment_ -->
</section>


<section markdown="block">
### And The Rest

* dealing with user input
* let the computer move
* who won?

</section>

<section markdown="block">
## Mutability Revisited
</section>

<section markdown="block">
### Mutability - Strings and Lists

* __Are strings mutable? &rarr;__
* __Are lists mutable? &rarr;__

<div class="incremental" markdown="block">
* strings __cannot be changed__; they are __immutable__.
* lists __can be changed__; they are mutable
</div>
</section>

<section markdown="block">
### Strings vs Lists... Indexing and Assignment

__What's the output of the following code? &rarr;__

{% highlight python %}
{% include classes/21/indexing_and_assignment.py %}
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
[1, 1, 3]
Traceback (most recent call last):
  File "indexing_and_assignment.py", line 5, in <module>
    b[1] = "1"
TypeError: 'str' object does not support item assignment
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lists, Indexing and Assignment

You can change values in a list!

* index into the list
* use the assignment operator (=)
* example:

{% highlight python %}
really_famous_cats = ["nermal", "felix", "sylvester"]
really_famous_cats[0] = "garfield"
# assignment works just fine!
{% endhighlight %}
</section>

<section markdown="block">
### List Methods vs String Methods

The behavior of the methods in lists and strings are consistent with the mutability of each type:

* string methods __don't change the object they're called on__; they return a new value
* list methods usually __change the object they're called on__; they change the object in place
</section>

<section markdown="block">
### List Methods vs String Methods Example

__What does this code output? &rarr;__
{% highlight python %}
{% include classes/21/list_string_methods.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
one two three
ONE TWO THREE
[1, 2, 3]
None
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Variables 

__What's a variable? &rarr;__

<div class="incremental" markdown="block">
* a __variable__ is a name that __refers__ to a value
* note the wording; it's intentional
	* in other contexts, variables may be thought of as holding values
	* in Python, variables are references (that is, they point to) values
</div>
</section>

<section markdown="block">
### Variables as References

Imagine variables as names that point to objects:

{% highlight python %}
a = [1, 2, 3]
{% endhighlight %}

{% highlight pycon %}
a ------> [1, 2, 3]
{% endhighlight %}
</section>

<section markdown="block">
### Variables as References Continued

Assignment is just pointing a reference.  When a new value is assigned to a name, it's the reference that's being changed.  

In the following reassignment example, notice that there are no more names that reference the initial list, [1, 2, 3].

{% highlight python %}
a = [1, 2, 3]
a = [4, 5, 6]
{% endhighlight %}

{% highlight pycon %}
          [1, 2, 3]

a ------> [4, 5, 6]
{% endhighlight %}
</section>

<section markdown="block">
### Aliasing

When one variable is assigned to another variable, both variables end up referring to the same object:

{% highlight python %}
a = [1, 2, 3]
b = a
{% endhighlight %}

{% highlight pycon %}
a ---+ 
     |--> [1, 2, 3]
b ---+ 
{% endhighlight %}

</section>

<section markdown="block">
### Aliasing Continued

The actual list object, [1, 2, 3], now has two names that refer to it.  Referencing the same object with more than one name is called __aliasing__.  

In the following code, a and b refer to the same object.  __What will the values of a and b be if we append a value to b? &rarr;__

{% highlight python %}
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2, 3, 4]
[1, 2, 3, 4]
{% endhighlight %}
See in [python tutor](http://pythontutor.com/visualize.html#code=a+%3D+%5B1,+2,+3%5D%0Ab+%3D+a%0Ab.append(4)&mode=display&cumulative=false&py=3&curInstr=0)
</div>
</section>

<section markdown="block">
### Aliasing Continued Some More!

__Aliasing causes side effects in mutable objects!__  However, it's a different story with immutable objects, like strings.  __What gets printed out here? &rarr;__

{% highlight python %}
a = "hello" 
b = a
c = b.upper()
print(a)
print(b)
print(c)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
hello
hello
HELLO
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And if Aliasing Was Not the Intention

If you'd like to make a new list rather than refer to the same list (that is have each variable point to a different object - though two equal objects)...

{% highlight pycon %}
a ------> [1, 2, 3]

b ------> [1, 2, 3]
{% endhighlight %}

...you can use list slicing, which always gives back a new list.  Creating a new list that is equivalent to, but a different object from the original, is called __cloning__.
</section>

<section markdown="block">
### Cloning

You can slice out the entire list to clone a list from the start index (0) to end index (len(list_of_elements) - 1):

{% highlight python %}
a = [1, 2, 3]

# cloned!
b = a[0:3]
{% endhighlight %}

Alternatively, there's shortcut to slicing out the whole string (without having to deal with precise start and end indexes)... 

__Just leave out the start and end (m, n) index from the slice.__

{% highlight python %}
b = a[:]
{% endhighlight %}
</section>

<section markdown="block">
### And What About Functions?

When parameters are passed to functions the value is a reference!  __What will this code print out? &rarr;__

{% highlight python %}
{% include classes/21/functions_lists_references.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[1, 2, 3, 1]
{% endhighlight %}
See in [Python tutor](http://pythontutor.com/visualize.html#code=numbers+%3D+%5B1,+2,+3%5D%0A%0Adef+add_four_to_list(a)%3A%0A++++a.append(4)%0A++++%0Aadd_four_to_list(numbers)&mode=display&cumulative=false&py=3&curInstr=0)
</div>
<!--_-->
</section>

<section markdown="block">
### References, Changing Values in Place

This means that functions can be created that change values in place rather than returning a value.  For example, this function removes the last two elements of a list:

{% highlight python %}
def remove_last_two_in_place(list_of_stuff):
	""" removes the last two elements of a list.  if the list is 2 elements 
	or less, removes all elements"""

	for i in range(2):
		if len(list_of_stuff) > 0:
			del list_of_stuff[-1]

{% endhighlight %}


</section>

<section markdown="block">
### References, Changing Values in Place Continued

The function in the previous slide can be used to _mutate_ the argument passed in (similar behavior to the random.shuffle function or the sort method on lists):


{% highlight python %}
numbers = [1, 2, 3, 4, 5]
remove_last_two_in_place(a)
print(numbers)
# prints out [1, 2, 3]
{% endhighlight %}

* __numbers__ actually changed
* but... if a __variable had been set equal to the return value__ of remove_last_two_in_place, __it would have been None__
</section>


<section markdown="block">
## Iterating With Indexes
</section>

<section markdown="block">
### Indexing Into a Sequence

How do we retrieve an element at a specific place from a list or a string?  For example, __to get the second element from the list a = [1, 2, 3], what code would I write? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
a[1]
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Indexes

What are some attributes of list and string __indexes__? That is... when you index into a sequence type... 

* __What date type does the index have to be? &rarr;__
* __Are list indexes sequential and consecutive, or are they unordered? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
* Indexes are ints
* They are sequential and consecutive
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Generating a Sequence of Integers

One way of iterating over every item in a list or a string is to go through each element by indexing.  

__...But how would you generate all of those indexes and go through each one? &rarr;__  

Hint: there are two ways to do this using constructs / statements that we've used before.

<div class="incremental" markdown="block">
* for loop with range
* while loops
</div>
</section>

<section markdown="block">
### For Loops and Indexes

__Use a for loop to print out every element in the list a = ["quill", "qat", "quip"]: &rarr;__

Some hints:

* what parameters should be passed to range?
	* what's the start index?
	* what's the last index?
* how do you access a list element?

<div class="incremental" markdown="block">
{% highlight python %}
a = ["quill", "qat", "quip"]
for i in range(0, len(a)):
	print(a[i])
{% endhighlight %}
</div>
</section>

<section markdown="block">
### While Loops and Indexes

__Use a while loop to print out every element in the list a = ["quill", "qat", "quip"]: &rarr;__

Some hints:

* what index do you start with?
* what's the end condition?
* how do you access a list element?

<div class="incremental" markdown="block">
{% highlight python %}
a = ["quill", "qat", "quip"]
i = 0
while i < len(a):
	print(a[i])
	i += 1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### The "Usual" Way

__Finally, to round things out, use a for loop - without indexes - to print out every element in the list a = ["quill", "qat", "quip"]: &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
a = ["quill", "qat", "quip"]
for word in a:
	print(word)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Reversing a List

__Write a function that takes a list as an input and returns the list in reverse order (btw, there's already a list method that does this) &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/21/reverse_a_list.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Another (More Destructive Way) to Reverse a List

__Can you use pop to do it? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/21/reverse_a_list_with_pop.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### But Wait - What Happened?

__What's the output of the pop() version of the solution? &rarr;__

{% highlight python %}
{% include classes/21/reverse_a_list_with_pop.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
['will', 'soon', 'disappear']
['disappear', 'soon', 'will']
[]
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Nested Loops
</section>

<section markdown="block">
### You Can Loop Within a Loop!

__What does this code output? &rarr;__

{% highlight python %}
for i in range(2):
	for j in range(2):
		print("%s%s" % (i, j))
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
00
01
10
11
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Breaking Down Nested Loops

* the inner most loop must finish iterating before the outer loop goes on to its next iteration
* both loop variables are accessible in the body of the innermost loop
</section>

<section markdown="block">
### Chess Board Squares

__Print out the names of each square on a chess board using nested loops &rarr;__  See [this article on chess notation](http://www.chessstrategiesblog.com/chess-notation/):

* columns are a through h
* rows are 1 through 8
* letter comes first

{% highlight pycon %}
a8 b8 c8 d8 e8 f8 g8 h8 
a7 b7 c7 d7 e7 f7 g7 h7 
a6 b6 c6 d6 e6 f6 g6 h6 
a5 b5 c5 d5 e5 f5 g5 h5 
a4 b4 c4 d4 e4 f4 g4 h4 
a3 b3 c3 d3 e3 f3 g3 h3 
a2 b2 c2 d2 e2 f2 g2 h2 
a1 b1 c1 d1 e1 f1 g1 h1 
{% endhighlight %}

</section>

<section markdown="block">
### Chess Board Squares Solution

{% highlight python %}
{% include classes/21/chess_board_coords.py  %}
{% endhighlight %}
</section>

<!--

<section markdown="block">
### Sieve

[Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity)

__Let's try to figure out a few different ways of doing this &rarr;__
</section>

<section markdown="block">
### Sieve Version 1

{% highlight python %}
{% include classes/21/sieve.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Sieve Version 2

{% highlight python %}
{% include classes/21/sieve_true_false.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Sieve Version 3

{% highlight python %}
{% include classes/21/sieve_with_del.py  %}
{% endhighlight %}
</section>

-->

<section markdown="block">
### Lists in Lists 

You can access an element within a list that's within a list by indexing __twice__!  The first index is the place in the outer list, the second index is the place in the inner list.

{% highlight python %}
a = [['foo', 'bar'],['baz', 'qux']]
print(a[0][1])
# gives back bar
{% endhighlight %}

</section>

<section markdown="block">
### Lists in Lists Example

__What does this code output? &rarr;__

{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(a[0][0])
print(a[0][1])
print(a[1][0])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
1
2
4
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Looping Over Lists in Lists

{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for inner_list in a:
	for number in inner_list:
		print(number)

for i in range(len(a)):
	for j in range(len(a[i])):
		a[i][j] += 10

print(a)
{% endhighlight %}
</section>

<section markdown="block" class="title-slide">
## List Comprehensions
</section>

<section markdown="block">
### Create a List of Squares 

__How would I create a list of numbers that are the square root of 0 through 9?__ &rarr;

{% highlight python %}
""" don't just use the list literal """
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
squares = []
for i in range(10):
	squares.append(i**2)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Create a List of Squares 

__How would I create a list of numbers that are the square root of 0 through 9, but only include squares that are divisible by 2?__ &rarr;

{% highlight python %}
""" don't just use the list literal """
[0, 4, 16, 36, 64]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
squares = []
for i in range(10):
	if i % 2 == 0:
		squares.append(i**2)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Quick Summary

* in each instance, we created a list by starting with an empty list
* ...using a for loop
* ...and appending on each iteration

</section>

<section markdown="block">
### List Comprehensions

__List comprehensions__ are another, more concise way of creating lists.  A list comprehension is __syntactic sugar__ (syntax within a programming language that is designed to make things easier to read or to express) for the code that we created previously. 

List comprehensions __make new lists__.
</section>

<section markdown="block">
### List Comprehension Syntax

* consists of square brackets to make a list
* a for loop-like expression within the brackets
* before the for loop-like expression, an expression that _calculates_ each element of the new list
* after the for loop-like expression, an optional expression that determines if an element should be in the new list
</section>

<section markdown="block">
### Two Examples: Squares, and Squares Divisible by 2

{% highlight python %}
[x * x for x in range(10)]
[x * x for x in range(10) if x % 2 == 0]
{% endhighlight %}
</section>

<section markdown="block">
### Another List Comprehension

__Write a list comprehension that creates a new list by adding exclamation points to every element in an existing list.__ &rarr;

{% highlight python %}
items = ['foo', 'bar', 'baz', 'busy']
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[s + '!' for s in items]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And Another List Comprehension!

__Limit the previous list to strings of length 3.__ &rarr;

{% highlight python %}
"""
filter the list called items (below), so that the resulting list is:
['foo', 'bar', 'baz']
"""
items = ['foo', 'bar', 'baz', 'busy']
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[s for s in items if len(s) == 3]
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Review End
</section>

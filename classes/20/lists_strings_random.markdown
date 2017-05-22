---
layout: slides
title: Lists, Strings, and Random 
---

<section markdown="block" class="title-slide">
# Lists, Strings, and Random
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
	* sum of cards is closest or equal to 21 without going over
	* dealt a hand of two cards, can either keep drawing or stop
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

* creates a deck of cards as a list of strings: 2-9, A, K, Q, J (4 x for hearts, clubs, spades, clovers)
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
### Some Assertions

We can check out all possible combinations of 1's and 11's to see which is the closest combination to 21.

{% highlight python %}
assert 21 == current_total(['A', '9', 'A']), "two aces, one 11 and one 1"
assert 12 == current_total(['A', 'A', '10']), "two aces, both 1"
assert 21 == current_total(['A', 'A', 'A', '8']), "three aces, one 11 and two 1"
assert 12 == current_total(['A', 'A', 'A', '9']), "three aces, three 1"
{% endhighlight %}
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

Maybe for homework?

* dealing with user input
* let the computer move
* who won?

</section>


<!--
<section markdown="block">
## [Mutability Revisited](mutability.html)
</section>
-->

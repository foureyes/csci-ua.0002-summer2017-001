---
layout: slides
title: Homework Solutions 
---
<section markdown="block" class="title-slide">
# Selected Homework Solutions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Selected Homework Solutions

<!-- 1. battleship.py -->
1. unique.py
2. translate.py

</section>

<!--
<section markdown="block">
## [battleship.py](../../../homework/hw9/battleship.py)
</section>

<section markdown="block">
### How Do We "Model" This Game? 

__What kind of data do we need, how is it represented?__ &rarr;

<div class="incremental" markdown="block">
1. the board - a list of lists of strings!
2. ...perhaps the dimension of the board? - an int
3. the location of the ship - maybe two ints, or a list of length 2
4. user input - a comma separated string
5. the actual coordinates - maybe two ints, or a list of length 2
</div>
</section>

<section markdown="block">
### Breaking Down the Problem

__What are the major pieces or components of the game?__ &rarr;

<div class="incremental" markdown="block">
1. setup - creating and printing the board, hiding the ship
2. the main game loop...
	* getting user input and changing it to coordinates
	* checking if the coordinates hit and ending the game
</div>
</section>

<section markdown="block">
### Setup

__Maybe we'll create a couple of functions for this.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
import random

def create_board(size):
	board = []
	for i in range(size):
		board.append(['o'] * size)
	return board
		
def print_board(board):
	for row in board:
		print(' '.join(row))

board_size = 5
board = create_board(board_size)
boat_row, boat_col  = random.randint(0, board_size - 1), random.randint(0, board_size - 1)
player_move = None
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Main Game Loop Pseudocode

__Write a pseudocode version of the main game loop__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
"""
while the player hasn't quit
	print out the board
	ask for coordinates
	check if coordinates hit the boat
	if they did... mark boat with, end the game and print out the board again
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Main Game Loop

{% highlight python %}
print(boat_row, boat_col)

while player_move != 'q':
    print_board(board)
    prompt = 'Enter row and col (each 0-%s) separated by a comma  \n> ' % (board_size)
    player_move = input(prompt)
    if player_move != 'q':
        coords = player_move.split(',')
        row, col = int(coords[0]), int(coords[1])
        board[row][col] = ' '
        if row == boat_row and col == boat_col:
            board[row][col] = "x"
            print("\nThe boat was at row %s and column %s" % (boat_row, boat_col))
            print("YOU WON!!!!\n")
            break
print_board(board)

{% endhighlight %}
</section>
-->

<section markdown="block">
## [unique.py](../../../homework/hw9/unique.py)
</section>

<section markdown="block">
### A Plan to Get Unique Values

__We're writing a function.  Assertions please!__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
print(get_unique_values(['foo', 'foo', 'bar', 'baz', 'bar']))
print(get_unique_values(["just me"]))
print(get_unique_values([]))
print(get_unique_values([1, 1, 1, 1, 1]))
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Unique - Pseudocode

__Let's sketch out how this function should work using pseudocode__ &rarr;


<div class="incremental" markdown="block">
{% highlight python %}
"""
create a new list called unique; it'll be our list with no duplicates
it'll be empty to start
go through every element in the list that's passed in
	if the element isn't already in the unique list...
		add it
	otherwise... don't do anything with it
give back the unique list
"""
{% endhighlight %}

__Let's try implementing this!__
</div>
</section>


<section markdown="block">
## [translate_passage.py](../../../homework/hw8/translate_passage.py)
</section>

<section markdown="block">
### Translate Passage

We can break this down into two components:

1. a function that takes a word and translates it to [pig latin](../../../homework/hw8/pig_latin.py)
2. a function that takes a passage and calls our first function on every word in the passage

__Let's write both functions... starting with assertions and pseudocode, and finally actual implementation__ &rarr;
</section>

<section markdown="block">
### Pig Latin

{% highlight python %}
def to_pig_latin(w):
	"""translates word to pig latin"""

	w = w.lower()

	if not w.isalpha():
		return w

	if w == "" or len(w) == 1:
		return w
	
	if w[0] in 'aeiou':
		return w + 'way'

	first_two = w[0:2]
	if first_two == 'qu' or first_two == 'ch' or first_two == 'sh' or first_two == 'th':
		return w[2:] + first_two + "ay"

	return w[1:] + w[0] + "ay"
{% endhighlight %}

</section>

<section markdown="block">
### Translate Passage

{% highlight python %}
def translate_passage(passage):
	"""translates text into pig latin"""
	translation = ""
	word = ""
	for c in passage:
		if not c.isalpha():
			translation += to_pig_latin(word)
			translation += c
			word = ""
		else:
			word += c
	return translation

assert "ethay estbay imetay!\neverway!" == translate_passage("the best time!\nEVER!"), "translation works"
print(translate_passage(passage))
{% endhighlight %}
</section>

<section markdown="block">
### Additional Solutions

Solutions from homeworks 5 through 9 are on [the materials page for this class](../..//schedule.html#midterm2hw).


</section>

---
layout: slides
title: Nested Loops, Nested Lists 
---
<section markdown="block" class="title-slide">
# Nested Loops, Nested Lists
{% include title-slide-footer.html %}
</section>

<section markdown="block" class="title-slide">
### Nested Loops

Loops can be nested within each other:

* for and while loops can be nested in for and while loops!
* nesting can be done in greater depths than 2 (though, that's not always recommended!)
* the inner loop must complete before the next iteration of the outer loop is executed
</section>

<section markdown="block" class="title-slide">
### A Silly Example

__How many times does this code print "um. what?"__

{% highlight python %}
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                print("um.  what?")
{% endhighlight %}

<div class="incremental" markdown="block">
* 16 times
* there are 4 nested loops
* each loop repeats its body twice
* 2 \* 2 \* 2 \* 2
</div>
</section>

<section markdown="block">
### Another Example (Still Silly)

__How many lines are printed in the following example?  Why?  What are the first two lines printed?__

{% highlight python %}
for i in range(4):
	for j in range(2):
		print("i is %s, j is %s" % (i, j))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# eight lines are printed
# the inner loop results in 2 printed lines, the outer loop does that 4 times

# the first two are...
i is 0, j is 0
i is 0, j is 1

# the last two are...
i is 3, j is 0
i is 3, j is 1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Yet Another Example

__How many lines are printed in the following example?  What are the first four lines printed out?__

{% highlight python %}
while True:
	for i in range(5):
		print(i)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# infinite!
0
1
2
3
4
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Closer Look

* again, the inner-most loop must finish iterating before the next outer loop goes on to its next iteration
* variables outside of an inner loop are accessible to the inner loop
	* ...including regular variables declared outside of the loop
	* and the outer for-loop variables

{% highlight python %}
for i in range(4):
	for j in range(2):
		# the variables i and j can be used in the inner loop!
		print("i is %s, j is %s" % (i, j))
{% endhighlight %}

[See this code execute on pythontutor.com](http://pythontutor.com/visualize.html#code=for+i+in+range(4)%3A%0A++++for+j+in+range(2)%3A%0A++++++++%23+the+variables+i+and+j+can+be+used+in+the+inner+loop!%0A++++++++print(%22i+is+%25s,+j+is+%25s%22+%25+(i,+j))&mode=display&cumulative=false&py=3&curInstr=0)
</section>

<section markdown="block">
### Let's See Some Examples

* draw an x
* finding the first n primes using trial division
* generating the names of the squares on a chess board
</section>

<section markdown="block">
### Draw an X

__Write a function called draw_an_x:__

* it's similar to stars.py in homework #9
* it takes one argument, the length of the arm
* it creates and returns a string representation of an x, with the size based on input
* calling draw_an_x(10) gives: 

{% highlight pycon %}
O        O
 O      O 
  O    O  
   O  O   
    OO    
    OO    
   O  O   
  O    O  
 O      O 
O        O
{% endhighlight %}

* in one diagonal, O's are placed at (0, 0), (1,1), etc.
* in the other diagonal, O's are placed at (0, 9), (1, 8), (2, 7), (3, 6) etc.
* what are the patterns 

</section>

<section markdown="block">
### Draw an X Pseudocode

{% highlight python %}
"""
for the number of rows (that is the length of the X)...
	create a row by...
	for every number of elements in a row (that is, number of columns, or the length of the X)
		if the row and column are equal
		or if their sum is the length of the X minus 1
			add an "O" to the row
		otherwise...
			add a space to the row
"""
{% endhighlight %}
</section>

<section markdown="block">
### Draw an X Solution

{% highlight python %}
{% include classes/26/stripes.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Finding the First n Primes

__Write a function called first_n_primes:__

* it should take one argument, n
* it should return a list with the first n primes (starting with 2)
* find the primes by using trial division
	* count up to - but not including - the candidate from 2
	* if it's divisible by any number, it's not prime
* example output:

{% highlight python %}
print(first_n_primes(2))
[2, 3]

print(first_n_primes(5))
[2, 3, 5, 7, 11]
{% endhighlight %}
</section>

<section markdown="block">
### Finding the First n Primes Pseudocode

{% highlight python %}
"""
keep track of all of the primes that we've fund
set our first possible prime number to 2
while that list of primes is less than n...
	let's assume that our number is prime, until we find out it's not...
	go through every number up to (but not including) our candidate
		if our candidate is divisible by a number
			it's not prime
	if it's prime, add it to our list
"""
{% endhighlight %}
</section>

<section markdown="block">
### First n Primes

{% highlight python %}
{% include classes/26/first_n_primes.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Chess Board Squares

__Print out the names of each square on a chess board using nested loops &rarr;__  See [this article on chess notation](http://www.chessstrategiesblog.com/chess-notation/):

* rows are 8 through 1 from the top
* columns are a through h starting from the left
* the actual name is column letter and row number

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
{% include classes/26/chess.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Strings and Grids

There's a pattern in the past couple of strings and nested loops that we've seen:

* to create a string representation of a grid, we use nested loops
* the outer loop usually represents each row
* the inner loop usually represents an element of each row (or each column)
* generally, we do things in this order because it's easier to append rows to a string than columns
</section>


<section markdown="block">
### Strings and Grids Continued

{% highlight python %}
col = "a8\na7\na6\na5\na4\na3\na2\na1\n"
print(col)
a8   
a7   
a6   
a5   
a4   
a3   
a2   
a1   
{% endhighlight %}

Adding another column isn't quite as easy as...
{% highlight python %}
col = col + "b8\nb7\nb6\nb5\nb4\nb3\nb2\nb1\n"
{% endhighlight %}
</section>

<section markdown="block">
### Values in Lists

__What types of objects can a list hold?__

<div class="incremental" markdown="block">
Any arbitrary value!

* strs
* ints
* floats
* turtles (!)
* __even other lists__... even dictionaries, tuples, etc.
* __even other lists with more lists in them!__
</div>
</section>

<section markdown="block">
### Lists in Lists

So, yes.  You can have a list in yr list ([wikipedia does!](http://en.wikipedia.org/wiki/List_of_lists_of_lists)).  __But why!?  What are some things that you could use nested lists for?__

<div class="incremental" markdown="block">
* any kind of two dimensional grid or collection of elements
	* a game board (chess, scrabble, battleship, tic-tac-toe)
	* an image!
* matrix math
* collecting groups of related types (a list of three dimensional points, which in turn are just lists of of three ints)
* this really extends to tuples as well (which may be more suited for representing some items above)
</div>
</section>

<section markdown="block">
### Creating Nested Lists

Let's take a look at three ways of creating nested lists:

* list literals
* appending lists to an empty list
* using loops 
</section>

<section markdown="block">
### List Literals

We can simply use list literal syntax (lots brackets and commas!).

* create a list with 3 lists in it
* each inner list has 4 elements - 1, 2, 3 and 4  

__What does this look like?__

<div class="incremental" markdown="block">
{% highlight python %}
a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Appending Lists to Lists

Alternatively, you can:

* start with an empty list
* and append lists to it

Again, if we want to create a list with 3 lists in it, each inner list containing 1 through 4... __How would I do that using an empty list and append?__

<div class="incremental" markdown="block">
{% highlight python %}
a = []
a.append([1, 2, 3, 4])
a.append([1, 2, 3, 4])
a.append([1, 2, 3, 4])
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Appending Lists to Lists Continued

Both of the previous solutions get old really fast!  __Can I do the same with less manual repetition?__

* start with an empty list
* and append lists to it repeatedly using a __???__

<div class="incremental" markdown="block">
{% highlight python %}
a = []
for i in range(3):
	a.append([1, 2, 3, 4])
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Chess Board Revisited

Instead of just having a string representation of our chess board, __can we represent it as a list?__

<div class="incremental" markdown="block">
{% highlight python %}
# Yes!
# first two rows...
board = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"], ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]] 
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Chess Board Revisited... 

__How could we create this nested list without using list literals?__ 

* probably nested loops!
* instead of building rows as strings, we'll use lists

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/26/chess_with_lists.py  %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Reading Elements from a Nested List

You can access an element within a list that's within a list by indexing __twice__!  
* the first index is the place in the outer list
* the second index is the place in the inner list

{% highlight python %}
a = [['foo', 'bar'],['baz', 'qux']]
print(a[0][1])
# gives back bar
{% endhighlight %}
</section>

<section markdown="block">
### Lists in Lists Example

Here's a list of lists that represents a tic-tac-toe board.  __What does this code output? &rarr;__

{% highlight python %}
tic_tac_toe = [[" ", " ", " "],[" ", "x", " "],["o", "o", "x"]]
print(tic_tac_toe[2][1])
print(tic_tac_toe[0][0])
print(tic_tac_toe[1][1])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
o
 
x
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Changing Values in Nested Lists

In addition to retrieving values from nested lists, we can also change values.

* use multiple indexes to find the element you want to change
* use the assignment operator 
* list_to_change[index_1][index_2] = "some other value"

{% highlight python %}
a = [[1, 1, 1, 1], [1, 1, 1, 1]]
a[0][3] = "not a one"
print(a)
# results in: 
# [[1, 1, 1, 'not a one'], [1, 1, 1, 1]]
{% endhighlight %}
</section>

<section markdown="block">
### Tic Tac Toe Again

Let's look at our tic tac toe board again.  It's x's turn to go.  __Where should an x be placed to win the game?  In code, how would we change the element at that position from space (" ") to "x"?__ 

{% highlight python %}
tic_tac_toe = [[" ", " ", " "],[" ", "x", " "],["o", "o", "x"]]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# put an x at 0, 0 (the upper left-hand corner)
tic_tac_toe = [[" ", " ", " "],[" ", "x", " "],["o", "o", "x"]]
tic_tac_toe[0][0] = "x"
print(tic_tac_toe)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Looping Over Lists in Lists

We saw how we could use nested loops in various example programs.  We'll also need nested loops if we want to look at every element within a nested list.  First, let's stick to one loop.  __How many times does this loop run?  What's the type of the loop variable called _inner_?  What's the last thing that gets printed out?__

{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for inner in a:
	print(inner)
{% endhighlight %}

<div class="incremental" markdown="block">
* 3 times
* list
* [7, 8 , 9]
</div>
</section>

<section markdown="block">
### Every Single Element

Because each inner element is also a list, we can loop over that as well!  __Print out every number in this list on its own line:__

{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# your code...
# results in
1
2
3
4
.
.
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for inner in a:
  for number in inner:
	print(number)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Changing All Elements in a Nested List 

Let's try changing every element in the previous so that it is twice the amount as the original.  Let's do this __in place__.  That is, we're modifying the list itself.
</section>

<section markdown="block">
### Changing All Elements in a Nested List... 

If I want to change the first element in the first list to twice the amount __what could would I use to do that?__ 

* what about changing the second element of the first list to twice the amount?
* and the third element of the first list
* and the first element of the second list

{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
a[0][0] = a[0][0] * 2
a[0][1] = a[0][1] * 2
a[0][2] = a[0][2] * 2
a[1][0] = a[1][0] * 2
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Pattern for Changing Elements

__Notice the pattern?__

{% highlight python %}
a[0][0] = a[0][0] * 2
a[0][1] = a[0][1] * 2
a[0][2] = a[0][2] * 2
a[1][0] = a[1][0] * 2
{% endhighlight %}

<div class="incremental" markdown="block">
* the inner list index is incremented by one for every element of the inner list
* the outer list index is incremented after all of the inner list indexes have been iterated over
</div>

</section>

<section markdown="block">
### Nested Loops and List Indexes

We've seen similar patterns when we used nested loops:  

* we can use nested loops and range to get index pairs
* using these index pairs, we can modify each list element

{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for i in range(len(a)):
	for j in range(len(a[i])):
		a[i][j] += 10
print(a)
{% endhighlight %}
</section>

<section markdown="block">
### Tic-Tac-Toe, One Last Time

Printing out our tic-tac-toe board

{% highlight python %}
tic_tac_toe = [[" ", " ", " "],[" ", "x", " "],["o", "o", "x"]]
{% endhighlight %}

Gives us

{% highlight python %}
[[" ", " ", " "],[" ", "x", " "],["o", "o", "x"]]
{% endhighlight %}

__Let's try to create a string representation of the board so that when it's printed, it looks like:__

{% highlight python %}

-------
| | | |
-------
| |x| |
-------
|o|o|x|
-------
{% endhighlight %}
</section>

<section markdown="block">
### Tic Tac Toe Printing

{% highlight python %}
{% include classes/26/tic_tac_toe.py  %}
{% endhighlight %}
</section>

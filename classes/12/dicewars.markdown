---
layout: slides
title: Approaching a New Programming Problem 
---
<section markdown="block" class="title-slide">
# Approaching a New Programming Problem
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Don't Just Jump Into Code!
* (obvs!) make sure you understand the stated problem 
	* what are the requirements for the program that you're writing?
	* create supporting materials to help you understand the problem (decision trees, flow charts, etc)
* think about how you would approach solving the problem
	* sketch out how you want your program to work
	* use pseudocode to get a general idea of your program's flow
	* _design_ your program
</section>

<section markdown="block">
### Perfect Squares

* print out all of the __perfect squares__ that are less than a number that's inputted by the user
* a perfect square is an integer that's the result of squaring another integer
* print out the total after all of the squares are printed
* if the user enters a negative number, print "negative numbers aren't allowed".
* example... user enter 30:

{% highlight python %}
1
4
16
25
4 perfect squares found
{% endhighlight %}
</section>

<section markdown="block">
### Potential Solutions

For math heavy problems like this, I'll make sure that there's a reasonable _brute force_ (a simple, usually iterative and not necessarily efficient) solution.  __What are some ways that we can solve this problem? &rarr;__  

<div class="incremental" markdown="block">
1. we could start counting from 1... and square each number until the square is greater than the input
2. count up to the number and check if the square root of that number is a whole number (this seems a little trickier)
</div>
</section>

<section markdown="block">
### Let's Write Up a Plan

* we can create a flow chart
	* rectangle with rounded corner - start, stop
	* rectangles - a generic step in the process
	* diamonds - a decision point (usually yes or no)
* and / or write pseudocode
	* loose, verbose translation of problem into code
	* not syntactically correct
</section>

<section markdown="block">
### A Flow Chart

The utility in this case may be up for debate, but for more complex programs, flow charts are indispensable!  __Let's try it! &rarr;__

<div class="incremental" markdown="block">
<div class="img-container" markdown="block">![Perfect Squares](../../resources/img/perfect_squares.png)
</div>
</div>
</section>

<section markdown="block">
### Pseudocode

__Let's also try writing some pseudocode &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
"""
ask for input
start counting from 1...
while the count squared is less than the input
	print out the count squared
print out the count
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Our First Draft

__Let's get our first version done. &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/13/perfectsquares_draft_1.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Another Version

__Our count was wrong, let's fix it. &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/13/perfectsquares.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Dice Warz!

Let's try a more complicated example.  Write a game:

* the user and the computer both roll six sided dice
* the player that rolls higher gets a point added to their score

__First... are these requirements sufficient?  What additional questions might you ask? &rarr;__

<div class="incremental" markdown="block">
* is it a graphical game or a text game?
* if it's text, how do you roll?
* can you leave the game?
* etc.
</div>

</section>

<section markdown="block">
### Example Output

{% highlight python %}
"""
Enter a command: roll or quit
>roll
Player rolled: 4
Computer rolled: 2
Player won!
Player: 1          Computer: 0

Enter a command: roll or quit
>quit
Bye! The final score was...
Player: 1          Computer: 0
"""
{% endhighlight %}
</section>

<section markdown="block">
### Let's flesh out those requirements:

{% highlight python %}
"""
* It's a text game - print out ASCII art!
* Ask for a command (there are only two possible commands: roll or quit)
* If command is roll, roll random dice for computer and player
* Print out the rolls
* Determine who wins (3 states: computer wins, player wins or tie)
* For each state add scores appropriately, 
* Print out who won and the resulting scores (keep track of scores)
* After each roll, go back to #2 to ask for a command again 
* (keep doing this until the user types in quit)
* If command is quit, print out the score and then exit the game
* If the command is not quit or roll, 
	* say "I don't know that command" and print the score
	* ...continue asking for a command
"""
{% endhighlight %}
</section>

<section markdown="block">
### Design Your Program

__Write some pseudocode.__

<div class="incremental" markdown="block">
{% highlight python %}
keep track of scores
ask the user for input
while the user hasn't quit
	if the user's command was roll
		roll dice for both the computer and the user
		figure out who one and add scores
	otherwise, if the command was quit, quit the game
	otherwise, if it's an unknown command, print unknown command	
	print scores
{% endhighlight %}
</div>
</section>

<section markdown="block">
{% highlight python %}
{% include classes/13/dicewars.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Don't Forget the Banner!

We're probably going to have to stop putting code in slides from here on in.  I skipped on the banner, and it still didn't fit!

{% highlight python %}
banner = """   ------
 /      /|  ~Dice Warz~
 ------| |
 |     | |
 |     |/
 ------
"""
print(banner)
{% endhighlight %}
</section>

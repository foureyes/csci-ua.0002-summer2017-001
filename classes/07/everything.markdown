---
layout: slides
title: Everything 
---

<section markdown="block">
### Number Guessing Game _Forever_

So, we'll finally be able to complete our number guessing game:

* use random to generate a secret number
* ask the user to guess what the number is
* if the user has it wrong, let them know if they should go higher or lower
* keep on asking the user to guess until they get it right
</section>


<section markdown="block">
### Number Guessing Game _Forever_

Some example output:

{% highlight python %}
I'm thinking of a number between 1 and 10; guess what it is!
> 8
Too low!
I'm thinking of a number between 1 and 10; guess what it is!
> 9
Too low!
I'm thinking of a number between 1 and 10; guess what it is!
> 10
I was thinking of 10!.  You got it right!
{% endhighlight %}
</section>

<section markdown="block">
### Number Guessing Game _Forever_ and _Ever_

* what if we want to say that they're really close (within 1), but not say higher or lower in that case? 
* what we want to be nice and ask the user if they want to quit after a wrong guess?
* what if we want to ask the user for a start and end number?
</section>

<section markdown="block">
### Let's Write a Mini Quiz Game!

__Write a program to ask a couple of questions about the book, Dune.__ &rarr;

{% highlight python %}
#  ______            _        _______ 
# (  __  \ |\     /|( (    /|(  ____ \
# | (  \  )| )   ( ||  \  ( || (    \/
# | |   ) || |   | ||   \ | || (__    
# | |   | || |   | || (\ \) ||  __)   
# | |   ) || |   | || | \   || (      
# | (__/  )| (___) || )  \  || (____/\
# (______/ (_______)|/    )_)(_______/
# 
# What is the name of the desert planet that's informally called Dune?
# > Arrakis
# You got it right!
# What valuable resource is only found on Dune?
# > cheese?
# Nope, the answer is: spice
# You got 1 questions right! 
{% endhighlight %}
</section>

<section markdown="block">
### Let's Write a Mini Quiz Game (Continued)!

Let's get some requirements down:

* ask two questions sequentially
* keep track of the number of questions that the player got right
* output the number of questions right
* (optional) keep track of the number of questions wrong, and output that as well
* (optional) ask for the player's name and greet the player
* (optional) ask the player if they want to play again
</section>

<section markdown="block">
### We Don't Have To Jump Right Into Code!

__So, first, what's our plan?__ &rarr;

* flow chart?
* pseudocode?
</section>

<section markdown="block">
### Let's Write a Mini Quiz Game! (Continued Some More)!

What are some ways that we can be more tolerant about capitalization?  That is... what if we wanted to accept these answers:

1. Arrakis / arrakis
2. spice 4 / the spice / the spice melange

Another wrinkle might be to have different output based on which version of the _right_ answer was chosen.  For example, if someone puts in spice, it might say, "oh, you mean, _the spice melange_".
</section>

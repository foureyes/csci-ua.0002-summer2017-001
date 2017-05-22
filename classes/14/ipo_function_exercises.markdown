---
layout: slides
title: Functions - Exercises 
---
<section markdown="block" class="title-slide">
# Functions - Exercises, IPO Charts
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Exercises!

<aside>Writing functions, 3 exercises and 1 demo:</aside>

1. Designing a Function
2. Factorial
3. David Lynch Movies
4. Greatest Common Divisor
5. Euclidean Rhythms

</section>


<section markdown="block">
### A Couple of Tools for Designing Functions

1. Pseudocode (we've seen this before)
2. IPO Charts
</section>

<section markdown="block">
### IPO Charts

<aside>To help with the exercises... let's look at IPO charts</aside>

{{ site.bookq }} describes the use of __IPO Charts__ to help design and document functions.  The chart has three columns, input, processing, output:

* the __input__ column shows a description of data that is passed in to the function
* the __processing__ column describes the process that the function performs
* finally, the __output__ column shows the data that is returned from the function

</section>

<section markdown="block">
### IPO Charts Example

An example IPO chart for our version of absolute value:

{% highlight python %}
"""
+-----------------------------------------------------+
| absolute_value                                      |
+-----------------------------------------------------+
| input            | processing        | output       |
+------------------+-------------------+--------------+
| the number to be | calculate the     | a number     |
| processed        | number's distance | representing |
|                  | from 0, e.g. -5   | the absolute |
|                  | is 5 away from 0  | value        |
+------------------+-------------------+--------------+
"""
{% endhighlight %}
<!--_-->
</section>

<section markdown="block">
## And ... Some Exercises
</section>

<section markdown="block">
### Factorial

<aside>(!!!!!!!!!!!!!!)</aside>

Does anyone remember what the factorial of a number is?  For example, __what is 4!? &rarr;__

<div class="incremental" markdown="block">
24
</div>
</section>

<section markdown="block">
### Factorial Definition


The __factorial__ of a number is the product of all positive integers less than or equal to that number.  

* it's denoted by an exclamation point (__!__)
* the factorial of 0 is 1  

The previous example of 4! is:

{% highlight pycon %}
>>> 4 * 3 * 2 * 1
24
{% endhighlight %}
</section>

<section markdown="block">
### Write a Function That Calculates Factorial

We want a function that takes a number and gives back (not prints out!) the factorial of that number.  

Example usage:

{% highlight pycon %}
>>> result = factorial(4)
>>> print(result)
24
>>> result = factorial(0)
>>> print(result)
1
{% endhighlight %}
</section>

<section markdown="block">
### IPO Chart

__How many arguments will the factorial function take, if any?  What processing will it do?  What will it return, if anything? &rarr;__

<div class="incremental" markdown="block">
Our no frills IPO chart for factorial:

* __input__: a number to calculate the factorial of
* __processing__: calculate the product of all positive numbers less than or equal to the input
* __output__: return the product
</div>
</section>

<section markdown="block">
### How About Some Pseudocode

__In pseudocode, what would the implementation of this function look like? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
define a function that takes one parameter
keep track of the product...
for every number less than or equal to n (up to, but not including 0)
	multiply the product by each number
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Possible Solution

Here's a possible _iterative_ solution:

{% highlight python %}
{% include classes/15/factorial_iterative_version.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Using Our New Factorial Function

__How would I use this function in a program that asks the user for a number... and then prints out the factorial of that number? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/15/factorial_iterative_version_user_input.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Is It a David Lynch Movie?

Write a program that determines whether or not a user inputted movie was made by David Lynch.

<div class="img-container" markdown="block">![Eraserhead](../../resources/img/eraserhead.jpg)
</div>
</section>

<section markdown="block">
### Who?

* American filmmaker and television director
* surrealist style
* you might know him from:
	* Blue Velvet
	* Eraserhead
	* Dune (yes!)
	* Twin Peaks
	* the voice of the bartender in Family Guy (!?)
	* etc.
</section>

<section markdown="block">
### Requirements

* define a function that determines if a string given is the title of a David Lynch movie
* the function will return True or False
* __use the function__ in a program that...
	* __continually__ asks the user: 
	* "Give me a movie title or q to quit"
* if the user types q, end the program
* if it's a David Lynch movie, print out "(movie) is a David Lynch movie!"
* otherwise, print out "There's a fish in the percolator"
</section>

<section markdown="block">
### Example Output

__Go!&rarr;__

{% highlight python %}
Give me a movie title
>Blue Velvet
Blue Velvet a David Lynch movie!
Give me a movie title
>Clueless
There's a fish in the percolator
Give me a movie title
>q
{% endhighlight %}
</section>

<section markdown="block">
### Example Usage of the Function

{% highlight python %}
movie = "Blue Velvet"
result = is_a_david_lynch_movie(movie)
{% endhighlight %}
</section>

<section markdown="block">
### IPO Chart

__How many arguments will it take, if any?  What processing will it do?  What will it return, if anything? &rarr;__

<div class="incremental" markdown="block">
Our no frills IPO chart for is_a_david_lynch_movie:

* __input__: a movie title
* __processing__: determine whether or not a movie title is directed by David Lynch
* __output__: return either True (if it's a David Lynch movie) or False (if it's not)
</div>
</section>


<section markdown="block">
### Possible Solution

{% highlight python %}
{% include classes/15/movie.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Greatest Common Divisor? 

What's the greatest common divisor (GCD) for 12 and 8?

<div class="incremental" markdown="block">
4
</div>
</section>

<section markdown="block">
## How Did You Figure That Out?
</section>

<section markdown="block">
### Maybe This Guy Could Help...

<div class="img-container" markdown="block">![Euclid](../../resources/img/euclid.jpg)
</div>
</section>

<section markdown="block">
### Euclid of Alexandria

Who was that?  That was Euclid (obv!).

* AKA "Father of Geometry"
* was writing algorithms two millennia ago! (about 300 BC)
* wrote a series of book called Euclid's _Elements_
	* one of the most influential works in the history of mathematics
	* was used to teach math up until the 19th or 20th century
</section>

<section markdown="block">
### Euclidean Algorithm

One method for finding the greatest common divisor is using Euclid's Algorithm:

1. start with a pair of positive integers 
2. form a new pair that's made up of the smaller number and the difference between the larger and smaller numbers
3. repeat until the numbers are equal 
4. the resulting number is the GCD
</section>

<section markdown="block">
### The Euclidean Algorithm in Action

__By hand, find the GCD of 12 and 8 using Eclid's Algorithm. &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
Larger of the pair goes in column A

 A | B | delta
___|___|______
12 | 8 | 4  
 8 | 4 | 4      (4 replaced 12) 
 4 | 4 | 0      (Done!)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Another Example

__By hand, find the GCD of 60 and 24 using Eclid's Algorithm. &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
Larger of the pair goes in column A

 A | B | delta
___|___|______
60 | 24| 36
36 | 24| 12     (36 replaced 60) 
24 | 12| 12     (12 replaced 36)
12 | 12| 0
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Requirements

Create a function that calculates the greatest common divisor of two numbers by using Euclid's algorithm.
</section>

<section markdown="block">
### Example Usage of the Function

{% highlight python %}
number_1, number_2 = 24, 144
greatest_common_divisor = gcd(number_1, number_2)
print(greatest_common_divisor)
{% endhighlight %}
</section>

<section markdown="block">
### IPO Chart

__How many arguments will it take, if any?  What processing will it do?  What will it return, if anything? &rarr;__

<div class="incremental" markdown="block">
Our no frills IPO chart for gcd:

* __input__: two numbers to find the greatest common divisor of
* __processing__: use Euclid's algorithm to find the greatest common divisor
* __output__: return the greatest common divisor
</div>
</section>

<section markdown="block">
### Pseudocode

{% highlight python %}
create a function that takes two arguments, a and b

while a and b aren't equal...
	let's make sure that we know which variable is the larger one 
	(we'll always assign it to a)
	if a is larger than b, then swap
	otherwise a gets changed to the difference between itself and b
{% endhighlight %}
</section>

<section markdown="block">
### Possible Solution

{% highlight python %}
# version 1
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
{% endhighlight %}

{% highlight python %}
# version 2
{% include classes/15/gcd_iterative_version.py %}
{% endhighlight %}
</section>

<!--
<section markdown="block">
## Um.  That's cool... but I just wanna dance! (To some algorithmically generated rhythms).  
</section>

<section markdown="block">
### Euclidean Rhythms

Apparently, the Euclidean Algorithm can be used to generate rhythms.  A paper by Godfried Toussaint explores the concept of Euclidean Rhythms.

* Euclid's Algorithm can be used to generate traditional music rhythms
* The rhythms generated cover almost all of the most important World Music rhythms 

</section>

<section markdown="block">
### Euclidean Rhythms Continued

The Euclidean Algorithm can be used to distribute a set number of notes as evenly as possible over a set period of time (where time is divided into equal parts).

* for example, 4 notes in 16 units of time (four notes in one measure of 16 sixteenth notes):
	* (X denotes a _pulse_, . denotes silence)
	* X...X...X...X...
	* [Let's take a listen](http://www.hisschemoller.com/2011/euclidean-rhythms/)
* ...and a less even distribution... 5 notes in 12:
 	* X..X.X..X.X.
	* we'll see how this works next!
	
</section>

<section markdown="block">
### General Algorithm

1. Put all of the _pulses_ in the beginning: XXXXX.......
2. Break into two groups of repeating patterns
3. Evenly distribute 2nd group of patterns to each element in the first group
4. Go back to 2.
</section>

<section markdown="block">
### How It Works

[5 notes in 12](http://mathforum.org/mathimages/index.php/The_Application_of_Euclidean_Algorithm#Euclidean_Rhythms)

1. Put all of the _pulses_ in the beginning: XXXXX.......
2. Move the remaining periods after each X: X.X.X.X.X...
3. (There are 5 pairs of [X.], with two dots remaining)
4. Place the remainder dots after the 1st two pairs of [X.]: X..X..X.X.X.
5. (There are 2 triplets of [X..], with two pairs of [X.] remaining)
6. Place the remainder of [X.] after the 1st two triplets of [X..]: X..X.X..X.X.
7. From here, the replacements become cyclical, so end here
</section>

<section markdown="block">
### How It Works 2

Sometimes it's easier to visualize in columns:

{% highlight python %}
"""
XXXXX....... 5, 12, delta is 7

XXXXX..      5, 2, delta is 3
.....

XXXXX        2, 3, delta is 1
.....
..

XXX          2, 1, stop
...
..
XX
..
"""
{% endhighlight %}

</section>


<section markdown="block">
### What Does That Actually Sound Like?

[Let's take a listen](http://www.hisschemoller.com/2011/euclidean-rhythms/).  Some examples of pulses and intervals:

* 3, 8  - tresillo - the fundamental rhythm in cuban and other latin music (also in  ragga or djembe drumming, etc.)
* 7, 12 - west african bell pattern
* 5, 9 - Arab rhythm called Agsag-Samai
</section>
-->


---
layout: slides
title: While Loops 
---
<section markdown="block" class="title-slide">
# Another Look at While Loops (It's the Sequel!)
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### What's a While Loop Again?

__Describe what a while loop is...__ &rarr;

<div class="incremental" markdown="block">
* it lets you repeat a block of code 
* the block of code continues to repeat as long as a condition is true
* as soon as the condition evaluates to false, the loop ends

__What is the while loop syntax?__ &rarr;

{% highlight python %}
while condition:
	print("execute this block of code")
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Great.  So.  Why Even?

<aside>What's the motivation for using while loops?</aside>

</section>

<section markdown="block">
### Sales Commission Program

{{ site.bookq }} has a program that: 

1. asks for a salesperson's number of sales and their rate
2. ...and then calculates their sales commission.

{% highlight python %}
# get a salesperson's sales and commission rate.
sales = float(input('Enter the amount of sales: '))
rate = float(input('Enter the commission rate: '))

# calculate the commission
commission = sales * rate

# display the commission
print("the commission is $" + str(commission))
{% endhighlight %}
</section>

<section markdown="block">
### Commission for 10, Please?

Is it possible to change the code in the previous slide so that __the program requests data and calculates commissions for 10 salespersons ... WITHOUT USING A WHILE LOOP?__ &rarr;


<div class="incremental" markdown="block">
Of course!  It's tedious, but just write the code 10 times!

{% highlight python %}
sales = float(input('Enter the amount of sales: '))
rate = float(input('Enter the commission rate: '))
commission = sales * rate
print("the commission is $" + str(commission))

sales = float(input('Enter the amount of sales: '))
rate = float(input('Enter the commission rate: '))
commission = sales * rate
print("the commission is $" + str(commission))

# and keep on going...
{% endhighlight %}
</div>
</section>

<section markdown="block">
### What About Counting?

__Can you write a program to count from 1 to 5 by printing out each number on a new line WITHOUT USING A LOOP (we saw this previously)__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
n, delta = 1, 1
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Counting Without a While Loop

* again, very tedious
* there's a repeating pattern of code
* ...but it's totally possible!
</section>


<section markdown="block">
### Last Example for Motivating Loops, I Swear

<div class="img-container" style="border:none" markdown="block">![Game Over](../../resources/img/game-over.png)
</div>
</section>

<section markdown="block">
### Continue? (Yes/No)

__WITHOUT USING A WHILE LOOP, is it possible to write a program that:__ &rarr;

* asks a user if they want to continue
* if they say yes, the program will ask them if they want to continue again
* this goes on until they don't say Yes

{% highlight python %}
Continue? (Yes keeps on going)
> Yes
Continue? (Yes keeps on going)
> Yes
Continue? (Yes keeps on going)
> No
{% endhighlight %}
</section>

<section markdown="block">
### Continue? (Yes/No)

We could try using consecutive nested if statements, __but we don't know how deep the nesting could go__. 

{% highlight python %}
answer = input('Continue? (Yes keeps on going) \n')

if answer == 'Yes':
	answer = input('Continue? (Yes keeps on going) \n')

	if answer == 'Yes':
		answer = input('Continue? (Yes keeps on going) \n')

		if answer == 'Yes':
			answer = input('Continue? (Yes keeps on going) \n')
{% endhighlight %}

</section>

<section markdown="block">
### Functions!?

* There's actually a way to do this using a function definition that calls itself.  
* We'll take a look at __recursion__ later this semester.

{% highlight python %}
def ask():
    answer = input('Continue? (Yes keeps on going) \n')
    if answer != 'Yes':
        ask()

ask()
{% endhighlight %}
</section>

<section markdown="block">
## Loops Will Make All of Those Previous Programs _Easier_ to Write!

<aside>Let's talk about loops a bit...</aside>
</section>

<section markdown="block">
### Iteration and Loops

Some formal definitions:

* __iteration__ - repeated execution of a set of programming statements
* __loop__ (or a _repetition structure_) - the actual __structure__ that allows repeated execution of a statement or a group of statements.  The statements are repeated either:
	* a specific number of times or ...
	* as long as a certain condition is true
</section>

<section markdown="block">
### Two Types of Loops

There are two broad categories of loops:

* __condition controlled__ - condition determines number of repetitions
* __count controlled__ - loop for a specific number of times
	* (it turns out that you can simulate __count controlled loops__ in __condition controlled loops__)
* guess which one a while loops is?

<div class="incremental" markdown="block">
A __while__ loop is a __condition controlled loop__.
</div>
</section>


<section markdown="block">
## While Loops
</section>

<section markdown="block">
### Condition Controlled Loops

* a __condition controlled__ loop causes a set of statements to be repeated as long as a condition is true
* again, in Python, the __while__ statement allows us to write a __condition controlled loop__
* ... or more succinctly: _while a condition is true, do some stuff_
* a __while__ loop consists of two parts:
	* a condition (_a boolean expression_) that is continually tested for a True or False value
	* a block of statements to repeat

</section>

<section markdown="block">
### While Loop Logic

A flow chart representing a while loop:

<div class="img-container" style="border:none" markdown="block">![While Loop Flow](../../resources/img/while-loop-flow.png)
</div>

</section>

<section markdown="block">
### While Loop Logic Continued

What happens if the condition is True?

<div class="incremental">

* one or more statements are executed
* condition is tested again

What happens if the condition is False?

The flow goes to the statements after the while loop
</div>

</section>

<section markdown="block">
### Compared to an If Statement

The flow chart for an if statement looks pretty similar to a while loop.  __What do you think the difference would be from the diagram showing while loop logic?__ &rarr;


</section>

<section markdown="block">
### If Statement Flow Chart

<div class="img-container" style="border:none" markdown="block">![If Statement Flow](../../resources/img/if-statement-flow.png)
</div>
</section>



<section markdown="block">
### While Loop Syntax

A template:

{% highlight python %}
while condition: # the book calls this the while clause
	statement
	statement
{% endhighlight %}

Some _real_ code:

{% highlight python %}
a = 100
while a > -1:
	print(a)
{% endhighlight %}

__What does this output? &rarr;__

<div class="incremental">
{% highlight python %}
100
100
100
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Basic While Loop Examples

<aside>There are lots...</aside>
</section>


<section markdown="block">
### Trivial Cases, Again

__What do these snippets of code print out?&rarr;__
{% highlight python %}
while True:
	print("I'm true!")
{% endhighlight %}
{% highlight python %}
while False:
	print("I'm false!")
{% endhighlight %}

<div class="incremental">
{% highlight python %}
I'm true!
I'm true!
I'm true!
{% endhighlight %}
{% highlight python %}
# nothing printed here
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Let's Step Through True
{% highlight python %}
while True:
	print("I'm true!")
{% endhighlight %}

1. condition is true
2. print "I'm true!"
3. go back to top
4. condition is true
5. print "I'm true!"
6. go back to top
7. you know the _deal_
</section>

<section markdown="block">
### Let's Step Through False
{% highlight python %}
while False:
	print("I'm false!")
{% endhighlight %}

1. condition is false

We never even get into the body of the loop!
</section>

<section markdown="block">
### Slightly More Complicated
<aside>Well, Not This One Exactly, But You'll See</aside>

__What does this print out? &rarr;__

{% highlight python %}
keep_on_going = True
while keep_on_going:
	print("I'm going!)"
{% endhighlight %}

<div class="incremental">
{% highlight python %}
I'm going
I'm going
I'm going
.
.
I'm going
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slightly More Complicated Continued

__Let's add one line.  What does this print out? &rarr;__

{% highlight python %}
keep_on_going = True
while keep_on_going:
	print("I'm going!")
	keep_on_going = False
{% endhighlight %}

<div class="incremental">
{% highlight python %}
I'm going
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slightly More Complicated Continued Continued

Going through each iteration

{% highlight python %}
keep_on_going = True
while keep_on_going:
	print("I'm going!")
	keep_on_going = False
{% endhighlight %}

* condition (keep_on_going) is true 
* print "I'm going!"
* set keep_on_going to false
* condition (keep_on_going) is false

Loop ends after one iteration.
</section>

<section markdown="block">
### What Happened There?

* we had some state __outside__ of the loop
* __within__ the loop we mutated / changed that state to eventually get out of the condition
* consequently, the loop _terminates_
* sometimes we call these kinds of variables __sentinel__ variables
* they only let certain conditions in!
</section>

<section markdown="block">
### Affecting the Outcome of the Condition

To change the outcome of your conditional:

* maintain state 
	* declare a variable __outside__ of the loop!
* mutate that state on loop iteration 
	* change that variable __inside__ the loop!
	* this will eventually cause the conditional to fail
* examples:
	* using operators to change a variable in your condition
	* using input to change a variable in your condition
</section>

<section markdown="block">
## Some Practical While Loop Examples
</section>

<section markdown="block">
###  Handling Input, Continue Again
First an easy one.  Let's go back to the continue program that we discussed earlier: 

* ask a user if they want to continue
* if they say yes, the program will ask them if they want to continue again
* this goes on until they don't say Yes

{% highlight python %}
Continue? (Yes keeps on going)
> Yes
Continue? (Yes keeps on going)
> Yes
Continue? (Yes keeps on going)
> No
{% endhighlight %}
</section>

<section markdown="block">
### Continue Program, Some Questions

* what are we repeating?
* how long are we repeating it, or what's the condition to keep on repeating it?
* is there any data that we're keeping track of?
</section>

<section markdown="block">
### Continue Program Implementation

{% highlight python %}
answer = input('Continue? (Yes keeps on going) \n')

while answer == 'Yes':
	answer = input('Continue? (Yes keeps on going) \n')
{% endhighlight %}

Notice that, like an if statement, variables declared outside of the body of the while loop can be accessed (and even changed) within the body of the while loop.
</section>

<section markdown="block">
### Another Continue Program Implementation 

{% highlight python %}
answer = 'Yes'

while answer == 'Yes':
	answer = input('Continue? (Yes keeps on going) \n')
{% endhighlight %}

* in order to go into the while loop, just start off with something that makes the condition true!
* __what are some benefits to using this pattern?__ &rarr;

<div class="incremental" markdown="block">
* we consolidate the request for input into a single point in the program
* if we want to change the question, just one place

(note that not all programs can fit this pattern)
</div>

</section>

<section markdown="block">
### A More Flexible Continue

Let's modify the previous program slightly so that it accepts either yes or yeah.

* ask a user if they want to continue
* if they say yes or yeah, the program will ask them if they want to continue again
* this goes on until they do not say Yes or Yeah

{% highlight python %}
Continue? (Yes or Yeah will keep going)
Yeah
Continue? (Yes or Yeah will keep going)
Yes
Continue? (Yes or Yeah will keep going)
Nope
{% endhighlight %}
</section>

<section markdown="block">
### Flexible Continue Program, Some Questions

* what are we repeating?
* how long are we repeating it, or what's the condition to keep on repeating it?
* is there any data that we're keeping track of?
</section>

<section markdown="block">
### Flexible Continue Program, Implementation

To implement this, modify the condition appropriately by adding _or answer == 'Yeah'_

{% highlight python %}
answer = input('Continue? (Yes or Yeah will keep going) \n')
while answer == 'Yes' or answer == 'Yeah':
	answer = input('Continue? (Yes or Yeah will keep going) \n')
{% endhighlight %}
</section>

<!--
<section markdown="block">
### 

<div class="incremental" markdown="block">
{% highlight python %}
{% endhighlight %}
</div>
</section>
-->


<!--
<section markdown="block">
### Examples
* back to opposite yes or yeah will make it stop. answer != yes and answer != yeah ... why?
	* what result do you want this to be to make it stop? false
	* yes or yeah makes it stop ... when the input is yes or yeah, this statement should be false
	* is the same as saying not yes and not yeah makes it go
	* we briefly touched on demorgans laws
	* what has to be true about this condition?
not (x and y)  ==  (not x) or (not y)
not (x or y)   ==  (not x) and (not y)
we choose the bottom... because we said that yes or yeah made it go, now werew saying that opposite of that
</section>
-->

<section markdown="block">
## Designing How Your While Loop Works
</section>

<section markdown="block">
### So, I Heard You Want to Repeat Some Code...

If you have some code that requires repetition, __what questions should you ask?__

<div class="incremental" markdown="block">
* first, will this require a while loop?
	* as long as there's repeated code that's based on a condition, yes!
* what's the condition ... which will probably lead to....
* what data is in the program?
* what should the data initially be set to, if anything at all?
* how will the loop terminate?
</div>

</section>

<section markdown="block">
##  We've Seen These Before... Some More Examples
</section>

<section markdown="block">
### Odd Numbers Except 13

__Write a program that... &rarr;__

* prints all of the odd numbers from 1-99
* skips 13

There are a few ways to do this!  __What are some general strategies for solving this problem?&rarr;__

<div markdown="block" class="incremental">

* using modulo
* or incrementing by twos

</div>
</section>

<section markdown="block">
### Possible Solutions for Odd Numbers Except 13
 
[Increment by 2's](http://www.pythontutor.com/visualize.html#code=n+%3D+1%0Awhile+n+%3C%3D+99%3A%0A++++if+n+!%3D+13%3A%0A++++++++print(n)%0A++++n+%3D+n+%2B+2&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)

{% highlight python %}
n = 1
while n <= 99:
    if n != 13:
        print(n)
    n = n + 2
{% endhighlight %}

[Using modulo to determine odds](http://www.pythontutor.com/visualize.html#code=n+%3D+1%0Awhile+n+%3C%3D+99%3A%0A++++if+n+!%3D+13%3A%0A++++++++print(n)%0A++++n+%3D+n+%2B+2&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)

{% highlight python %}
n = 1
while n <= 99:
    if n % 2 == 1 and n != 13:
        print(n)
    n = n + 1
{% endhighlight %}
</section>



<!--
<section markdown="block">
### Do You Want Cake (Again)

__Repeatedy ask if user wants cake until user says yes or yeah.  How would you implement this?&rarr;__

{% highlight python %}
Do you want cake?
> no
Do you want cake?
> No
Do you want cake?
> yeah
Have some cake!
{% endhighlight %}

<div class="incremental">
{% highlight python %}
answer = 'no'
while answer != 'yes' and answer != 'yeah':
	answer = input("Do you want cake?\n> ")
print("Have some cake!")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Stepping Through Cake

Let's make an assumption that the user enters "no" first, and then "yeah" second.

{% highlight python %}
answer = 'no'
while answer != 'yes' and answer != 'yeah':
	answer = input("Do you want cake?\n> ")
print("Have some cake!")
{% endhighlight %}

1. answer is set to no by default
2. condition is true, answer (no) is not 'yes' or 'yeah'
3. answer is set to user input of 'no'
4. condition is true, answer (no) is not 'yes' or 'yeah'
5. answer is set to user input of 'yes'
6. condition is false, answer != 'yeah' is now false!
7. have some cake is printed
</section>
-->

<section markdown="block">
### Accumulating Values

__Write a program that will: &rarr;__ 

* continually ask the user for a number (__forever__)
* add that number to a running total
* print out the running total

{% highlight python %}
Give me a number to add
> 10
Current total is 10
Give me a number to add
> 15
Current total is 25
Give me a number to add
> 5
Current total is 30
Give me a number to add
> 
{% endhighlight %}

</section>

<section markdown="block">
### Potential Solution for Accumulating Values

{% highlight python %}
total = 0
while True:
    n = int(input("Give me a number to add\n> "))
    total = total + n
    print("Current total is " + str(total))
{% endhighlight %}

</section>

<section markdown="block">
### Average of Input

__Write a program that continually asks the user for numbers, and asks them if they'd like to keep going.  In the end, it should output the average of all of the numbers entered&rarr;__

{% highlight python %}
I'll calculate the average for you!
Current total: 0
Numbers summed: 0
Please enter a number to add
> 10
Do you want to continue adding numbers (yes/no)?
> yes
Current total: 10
Numbers summed: 1
Please enter a number to add
> 12
Do you want to continue adding numbers (yes/no)?
> no
The average is 11.0
{% endhighlight %}
</section>

<section markdown="block">
### Some Hints, Please?
Let's try keeping track of multiple variables:

* a user's answer to whether or not the program should continue
* (possibly) the number that the user has just entered
* the total (sum) of the numbers that a user has entered 
* the count of numbers input
</section>

<section markdown="block">
### An Average Solution

{% highlight python %}
total = 0
count = 0
answer = 'yes'
print("I'll calculate the average for you!")
while answer == 'yes':
        print("Current total: " + str(total))
        print("Numbers summed: " + str(count))
        total = total + int(input("Please enter a number to add\n> "))
        count = count + 1
        answer = input("Do you want to continue adding numbers (yes/no)?\n> ")
print("The average is "+ str(total / count))
{% endhighlight %}
</section>

<section markdown="block">
## Syntactic Sugar
</section>

<section markdown="block">
### Increment / Decrement

We've used the following syntax to increment or decrement a variable

{% highlight python %}
n = 0
n = n + 1

n = 100
n = n - 1
{% endhighlight %}

_Slightly_ tedious...
</section>

<section markdown="block">
### Increment / Decrement Continued

There's some _syntactic sugar_ that makes doing this less verbose:  use __+=__ or __-=__

* __n += 1__ is the same as n = n + 1
* __n -= 1__ is the same as n = n - 1

{% highlight python %}
n = 0
# adds one to n and binds the resulting value to n
n +=  1

n = 100
# subtracts one to n and binds the resulting value to n
n -= 1
{% endhighlight %}

</section>

<section markdown="block">
### More Syntactic Sugar

This works for other operators too.   __What does this code print out? &rarr;__

{% highlight python %}
n = 2
n *= 2
n *= 2
print(n)

n = 64
n /= 2
n /= 2
print(n)
{% endhighlight %}
<div class="incremental">
{% highlight python %}
8
16.0
{% endhighlight %}
</div>

</section>

<section markdown="block">
### What About Strings?

Also works with strings....   __What does this code print out? &rarr;__
{% highlight python %}
s = "h"
s += "e"
s += "y"
s *= 3
print(s)
{% endhighlight %}

<div class="incremental">
{% highlight python %}
heyheyhey
{% endhighlight %}
</div>

</section>

<section markdown="block">
## Some More Exercises!
</section>

<section markdown="block">
### Powers of Two

__Continually print out the next power of two, only if you say 'y'__ &rarr;

{% highlight python %}
1
next power?
> y
2
next power?
> y
4
next power?
> n
{% endhighlight %}
</section>

<section markdown="block">
### Squares

__Continually ask for a number, print out the square, and ask to continue__ &rarr;

{% highlight python %}
number
> 5
25
continue?
> y
number
> 2
4
continue?
> n
{% endhighlight %}
</section>

<section markdown="block">
### Other Exercises

* count the number of digits in an int
	* repeatedly use integer division
	* ...until the original number becomes 0
	* keep count of divisions
* continually add exclamation points to a word
	* ask for a word
	* ask for x number of exclamation points
	* print out resulting word and exclamation points
	* continue asking for another word and exclamation points
</section>


<section markdown="block">
## [...And For Loops](for.html)
</section>

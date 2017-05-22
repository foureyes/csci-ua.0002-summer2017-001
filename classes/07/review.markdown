---
layout: slides
title: Review - Conditionals 
---
<section markdown="block" class="title-slide">
# Review Conditionals
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Operator Precedence

__What are the types of operators that we learned about?  List them in order of precedence &rarr;__

<div class="incremental" markdown="block"> 
1. Parentheses
2. Numerical/String operators
3. Comparison operators
4. Logical operators
</div>
</section>

<section markdown="block">
### Logical Operators

__Name the three logical operators that we learned and order them by precedence &rarr;__

<div class="incremental" markdown="block"> 
* not
* and
* or
</div>
</section>

<section markdown="block">
### Logical Operators Continued

__What are the only two values that cause "and" to evaluate True? Under what conditions does "or" evaluate to True?  &rarr;__

<div class="incremental" markdown="block"> 
* __and__ evaluates to True only when both operands are True
* __or__ evaluates to True when either operand is True
</div>
</section>

<section markdown="block">
### Surprise!

__Write a program that asks the user if they want a surprise: &rarr;__

* if the input is yes, Yes or YES, print out 'SURPRISE!'
* otherwise, print out '...'

{% highlight bash %}
Do you want a surprise?
> yes
SURPRISE!
{% endhighlight %}
{% highlight bash %}
Do you want a surprise?
> YES
SURPRISE!
{% endhighlight %}
{% highlight bash %}
Do you want a surprise?
> nope
...
{% endhighlight %}
</section>

<section markdown="block">
### Surprise! Solution 

{% highlight python %}
{% include classes/07/surprise.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Speed Limit

Write a program that:

* asks the user for the speed limit
* asks the user what their current speed is
* depending on the speed that they're going, print out the following:
	* within 5 miles above or below speed limit
		* print out "just right!"
	* more than 5 miles above speed limit
		* print out "too fast!"
	* less than 5 miles below speed limit
		* print out "too slow!"
</section>

<section markdown="block">
### Speed Limit - Example Interaction

{% highlight bash %}
What is the speed limit?
> 55
How fast are you goin'?
> 60
Your speed is just right!
{% endhighlight %}

{% highlight bash %}
What is the speed limit?
> 55
How fast are you goin'?
> 61
You're going too fast!
{% endhighlight %}

{% highlight bash %}
What is the speed limit?
> 55
How fast are you goin'?
> 49
You're going too slow!
{% endhighlight %}
</section>

<section markdown="block">
### Speed Limit

{% highlight python %}
{% include classes/07/going_too_fast.py %}
{% endhighlight %}

</section>

<section markdown="block">
### elif 

__elif__ chains together a series of conditions allowing multiple possible paths of execution.  

* only one path will be executed
* each condition is checked in order
* if the first is false, the next condition is checked
* this continues until the first true condition
* the body of code associated with that condition is executed
* the statement ends even if there are more conditions left
</section>

<section markdown="block">
### Movie Ratings	

The following program asks for your age, and recommends which movie ratings you shouldn't see based on your age:

* __13 or over__: don't watch movies that are rated R
* __17 or over__: watch anything you want!

{% highlight python %}
age = int(input("How old are you?"))
if age >= 13:
	print("don't watch movies that are rated R!")
elif age >= 17:
	print("watch anything you want!")
{% endhighlight %}

__What is the output if someone enters 15... and 23??__ &rarr;

<div class="incremental" markdown="block"> 
* 15 &rarr; "don't watch movies that are rated R!"
* 23 &rarr; same... "don't watch movies that are rated R!"
</div>
</section>

<section markdown="block">
### Movie Ratings Continued	

__What are some ways of fixing this program?__ &rarr;

{% highlight python %}
age = int(input("How old are you?"))
if age >= 13:
	print("don't watch movies that are rated R!")
elif age >= 17:
	print("watch anything you want!")
{% endhighlight %}
</section>

<section markdown="block">
### Movie Ratings Implementations	

Reorder...

{% highlight python %}
age = int(input("How old are you?"))
if age >= 17:
	print("watch anything you want!")
elif age >= 13:
	print("don't watch movies that are rated R!")
{% endhighlight %}

Tighten up conditions...

{% highlight python %}
age = int(input("How old are you?"))
if age >= 13 and age < 17:
	print("don't watch movies that are rated R!")
elif age >= 17:
	print("watch anything you want!")
{% endhighlight %}
</section>

<section markdown="block">
### I'm Late!

__What is the output of this program if the user enters: yes and 10... or just no__? &rarr;

{% highlight python %}
late = "Are you late?\n> "
if late == "yes":
	minutes = int(input("How late are you (in minutes)?\n> "))
	if minutes <= 15:
		print("run!")
	else:
		print("take the subway!")
else:
	print("take your time...")
{% endhighlight %}

<div class="incremental" markdown="block"> 
* yes and 10 &rarr; run!
* no &rarr; take your time
</div>
</section>

<section markdown="block">
### Nesting 

* in the previous example, we saw an if-else statement nested within another if-else
* we can nest if, if-else, and if-elif statements within each other
	* sometimes nesting statements may make logic flow more comprehensible
	* but nesting too deeply may make code uneccessarily complex
</section>

<section markdown="block">
## Aaaand... We're Talking About Cake Again
</section>

<section markdown="block">
### Cake Three Ways

We went through a few different implementations of the following program:

{% highlight python %}
"""
Do you want cake?
> yes
Here, have some cake.

Do you want cake?
> no
No cake for you.

Do you want cake?
> blearghhh
I do not understand.
"""
{% endhighlight %}
</section>

<section markdown="block">
### Cake With Consecutive if Statements

{% highlight python %}
{% include classes/06/cake_consecutive_ifs.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Cake With Nested if Statements

{% highlight python %}
{% include classes/06/cake_nested_ifs.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Cake With elif

{% highlight python %}
{% include classes/06/cake_elif.py %}
{% endhighlight %}

<!--_ -->
</section>



<section markdown="block">
### Old Enough to Vote

__Rewrite the condition in the following program so that it doesn't need the not operator__: &rarr;

{% highlight python %}
age = int(input("How old are you?"))
if not age < 21:
	print("you can vote!")
{% endhighlight %}

<div class="incremental" markdown="block"> 
{% highlight python %}
age = int(input("How old are you?"))
if age >= 21:
	print("you can vote!")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Logical Opposites 

Sometimes there are multiple ways to write equivalent conditions.  For example, a way to get rid of not operators is to use the opposite logical operator and drop the not...

* the logical opposite of &gt; is &lt;=
* the logical opposite of &lt; is &gt;=

The following conditions are equivalent:

* age >= 21, not age < 21
* not score > 5, score <= 5
</section>

<section markdown="block">
## [String Formatting](string-formatting.html)
</section>

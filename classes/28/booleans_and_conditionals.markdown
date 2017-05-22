---
layout: slides
title: Booleans and Comparison Operators 
---
<section markdown="block" class="title-slide">
# Booleans and Comparison Operators
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Comparison Operators

__Name six comparison operators?&rarr;__

<div class="incremental" markdown="block"> 
* __==__ - equals (can be called logical equivalence or equality operator)
* __!=__ - not equal
* __>__ - greater than
* __<__ - less than
* __>=__ - greater than / equal
* __<=__ - less than / equal
</div>
</section>

<section markdown="block">
### Comparison Operators Continued
* again - these operators always return a bool
* these operators do what you would expect 
	* __==__ - returns True if both sides are equal &rarr;
	* __!=__ - returns True if both sides are not equal &rarr;
	* __>__, __<__, __>=__, __<=__ - returns True if value on the left is greater than, less than, greater than / equal, or less than equal to the value on the right &rarr;
* never put equals first on >=, <=
</section>

<section markdown="block">
### Comparison Operators and Different Types
* objects of different types, except different numeric types, are never equal
	* equals (__==__) will always return False for different types &rarr;
	* not equals (__!=__) will always return True for different types &rarr;
* the <, <=, > and >= operators... 
	* will raise a TypeError if the objects are of different types that cannot be compared &rarr;
	* will happily compare numeric types (for example comparing floats and ints works as you'd expect)! &rarr;
</section>

<section markdown="block">
### What are Logical Operators?

__Logical Operators are operators that combine Boolean values.__  

* these operators always return another Boolean value.  
* furthermore, these operators can be used to create more complex Boolean expressions. 
</section>

<section markdown="block">
###  Three Logical Operators:
1. __and__ - 
	* takes two operands, one on each side 
	* to return True, both sides of the operator must be True &rarr;
2. __or__ - 
	* takes two operands, one on each side
	* to return True,at least one side of the operator must be True &rarr;
3. __not__ - 
	* only takes one operand to the right
	* to return True, the original value on the right must evaluate to False &rarr;
	* two nots cancel eachother out (fun!) &rarr;
</section>

<section markdown="block">
###  Logical Operators _in Action_
{% highlight pycon %}
>>> True and False
False
>>> True and True
True
>>> True or False
True
>>> not True
False
>>> not not True
True
{% endhighlight %}
</section>

<section markdown="block">
### Truth Table - AND

__and__ takes two operands.  Each operand can be True or False (or will evaluate to True or False!).  

__Can you guess how many possible combinations ther are for these two operands?__  __What will the Truth Table look like?__ &rarr;

<div class="incremental" markdown="block"> 
{% highlight python %}
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | q | p and q
----------------
 f | f | f
 f | t | f
 t | f | f
 t | t | t
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Truth Table - OR

Let's fill out a truth table for __or__! &rarr;

<div class="incremental" markdown="block"> 
{% highlight python %}
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | q | p and q
----------------
 f | f | f
 f | t | t
 t | f | t
 t | t | t
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### How About Something More Complicated?

Let's fill out a truth table for __p and not q and r__! &rarr;

<div class="incremental" markdown="block"> 
{% highlight python %}
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | q | r | p and not q and r
-----------------------------
 t | t | t | f
 t | t | f | f
 t | f | t | t
 t | f | f | f
 f | t | t | f
 f | t | f | f
 f | f | t | f
 f | f | f | f
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Let's Evaluate Some Simple Boolean Expressions

* True and False &rarr;
* True and not False &rarr;
* True or False &rarr;
* True or not False &rarr;
* False or False &rarr;
* not False and not False &rarr;

</section>

<section markdown="block">
### Chaining Boolean, Comparison, and Other Operators
You can chain together operators to make complex Boolean expressions!  

* Boolean expressions can involve Boolean, comparison, and other operators
* they can be arbitrarily complex!  (don't do that)

__What do you think this evaluates to?__ &rarr;
{% highlight python %}
-10 ** 2 <= -100 or "foo" == "bar" and 100 >= 100
{% endhighlight %}

<div class="incremental" markdown="block"> 
{% highlight python %}
True
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Order of Operations / Operator Precedence

[A summary can be found in the official documentation for Python 3]( http://docs.python.org/py3k/reference/expressions.html#summary), but here's the short version:

* parentheses are evaluated first (obv)
* numeric / string operations (in turn, are also ordered)
* comparison operations (==, !=, >, <, >=, >=)
* not
* and
* or
</section>

<section markdown="block">
## Conditionals
</section>

<section markdown="block">
### Anatomy of an If Statement

__Write an if statement testing if a and b are _not_ equal.  If they're not equal, print the value of a and b twice.__ &rarr;
{% highlight python %}
a, b = "foo", "bar"
{% endhighlight %}

<div class="incremental" markdown="block">
* begin with keyword __if__
* condition
* colon - ends the condition / marks that a block of code is about to come up
* if + condition + colon usually is considered the _if-statement header_
* body of if statement ends when indentation goes back one level
* blank lines don't count as ending a block of code!
</div>
</section>

<section markdown="block">
### Let's See That Again
<aside>Now With More Blank Lines</aside>

{% highlight python %}
a, b = "foo", "bar"
if a != b:
	# totally ok?  yes!
	# but why?
	# perhaps when done more reasonably, readability
	print a
	print a


	print b

	print b
{% endhighlight %}
</section>

<section markdown="block">
### Oh Yeah, Else What?

We can use __else__ to execute code if the original condition was not met

* go back one level of indentation to mark that the previous code block has ended
* keyword __else__
* body - indented, body ends when indentation goes back one level
* not required, obvs
</section>

<section markdown="block">
### What About Multiple Chained Conditions?
What if __else__ is not fine-grained enough?  For example, how about a program that asks for cake and handles a yes, no, or anything other than...

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
### Consecutive Ifs
__One way to do it is consecutive if statements...__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
answer = input("Do you want cake?\n> ")
if answer == 'yes':
        print("Here, have some cake.")
if answer == 'no':
        print("No cake for you.")
if answer != 'yes' and answer != 'no':
        print("I do not understand.")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Else If (elif)

We can use __elif__ to chain a series of conditions, where only one path of code will be executed

* if statement like usual
* go back one level of indentation to mark that the previous code block has ended
* keyword __elif__
* condition
* colon
* body - indented, body ends when indentation goes back one level
* not required obv
* even if more than one true, only the first true executes!
* can add an else at the end
</section>

<section markdown="block">
### elif Example
<aside>Let's have some more cake...</aside>
__How would we redo the cake exercise with elif?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
answer = input("Do you want cake?\n> ")
if answer == 'yes':
        print("Here, have some cake.")
elif answer == 'no':
        print("No cake for you.")
else:
        print("I do not understand.")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### How to Order Conditions

* if more than one condition in a series of elif's is true 
	* only the first true condition is executed!
	* other are skipped, including else
* ordering conditions so that the broadest ones are evaluated last may help avoid this issue
* be careful of conditions that never get evaluated 
	* an above condition may already account for it
	* here's an example...
</section>

<section markdown="block">
### How to Order Conditions Continued!

Here's a contrived exercise:  

* determine whether a number is 101 or if it's greater than 100
* if it's 101, it should only print out that it's "exactly 101" (it shouldn't print out greater than 100)

Here's an implementation.  __What gets printed if n = 200?  What gets printed if n = 101?__   &rarr;

{% highlight python %}
if n > 100:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}
</section>

<section markdown="block">
### Another Gotcha!
<aside>And Back to That Cake Thing</aside>

__Will this code work??__ &rarr;

{% highlight python %}
answer = input("Do you want cake?\n> ")
if answer == 'yes':
        print("Here, have some cake.")

if answer == 'no':
        print("No cake for you.")
else:
        print("I do not understand.")
{% endhighlight %}

<div class="incremental" markdown="block">
It does something unexpected!  If the user enters yes, we get both "Here, have some cake" __and__ "I do not understand."  Be careful when using consecutive __ifs__
</div>
</section>

<section markdown="block">
### Nesting If Statements

* it behaves as you'd expect
* remember to get indentation right
* if there are multiple elif's or else's,  you can use indentation to see which initial if statement they belong to
* this works for any combination of if, elif and else
* note that sometimes nested if statements are equivalent to and
* best to simplify - that is, less nesting, better
</section>

<section markdown="block">
### Nested If Statements and And

__How would you simplify this? &rarr;__

{% highlight python %}
a = 100
if a > 25:
	if a < 200:
		print("I'm in here")
print("We're out there")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
a = 100
if a > 25 and a < 200:
	print("I'm in here")
print("We're out there")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Nested If Statements Example

__We could have impemented the cake exercise  using nested if statements.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/cake_nested_ifs.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Modules
</section>



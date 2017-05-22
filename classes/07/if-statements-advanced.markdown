---
layout: slides
title: More If Statements 
---
<section markdown="block" class="title-slide">
# More If Statements
{% include title-slide-footer.html %}
</section>


<section markdown="block">
### Nesting If Statements

* we saw nested ifs in the cake example
* it behaves as you'd expect
* remember to get indentation right
* if there are multiple elif's or else's,  you can use indentation to see which initial if statement they belong to
* this works for any combination of if, elif and else
* note that sometimes nested if statements are equivalent to and
* best to simplify - that is, less nesting, better
</section>

<section markdown="block">
### Nesting If Statements Example

The coffee shop has a special for half price pastries on Fridays after 4 (16:00... or 16).  __Ask for day and time, and make a recommendation (buy now, wait x hours or don't buy).__ &rarr;

{% highlight python %}
What day is it (ex Thursday, Friday, etc.)?
> Friday
What time is it (in 24 hour time)?
> 17
Go ahead, you deserve a treat

Press ENTER or type command to continue
What day is it (ex Thursday, Friday, etc.)?
> Friday
What time is it (in 24 hour time)?
> 12
Just wait 4 more hours
{% endhighlight %}

</section>

<section markdown="block">
### Pastry Buying Guide

{% highlight python %}
{% include classes/06/pastry_buying_guide.py %}
{% endhighlight %}
</section>


<section markdown="block">
### How to Order Conditions

* if more than one condition in a series of elif's is true 
	* only the first true condition is executed!
	* other are skipped, including else
* be careful of conditions that never get evaluated 
	* an above condition may already account for it
	* here's an example...
</section>

<section markdown="block">
### Ordering Conditions Continued!

The intention of the following code is to:

* determine if a number is 101 or greater than 100
* if it's 101, it should only print out "exactly 101" (it should not print out greater than 100)

__What gets printed if n = 200?  What if n = 101?__   &rarr;

{% highlight python %}
if n > 100:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}

<div class="incremental" markdown="block">
200 &rarr; more than 100, 101 &rarr; more than 100
</div>

</section>

<section markdown="block">
### How to Order Conditions Continued Some More!

__Of course, we could fix this.  There are a few ways...__ &rarr;

<div class="incremental" markdown="block">
* reordering
* using and
{% highlight python %}
if n == 101:
	print("exactly 101")
elif n > 100:
	print("more than 100")

if n > 100 and n != 101:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Equivalent Conditions
</section>

<section markdown="block">
### Logical Opposites 
A way to get rid of not operators is to use the opposite logical operator:

[Logical Opposites from {{ site.bookt }} ](http://openbookproject.net/thinkcs/python/english3e/conditionals.html)

* for example... the logical opposite of &gt; is &lt;=
* the logical opposite of &lt; is &gt;=

</section>

<section markdown="block">
### Logical Opposites Continued
__How can we rewrite this without the not?__&rarr;

{% highlight python %}
# Example from {{ site.bookt }}
if not (age >= 17):
    print("Hey, you're too young to get a driving licence!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
if age < 17:
    print("Hey, you're too young to get a driving licence!")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### De Morgan's Law
* not (x and y)  ==  (not x) or (not y)
* not (x or y)   ==  (not x) and (not y)
* {{ site.bookt }} example
	* uses combination of logical opposites and De Morgan's Law
	* clarity / closeness to original 

</section>

<section markdown="block">
### De Morgan's Law

__Let's try truth tables for these!__ &rarr;

{% highlight bash %}
x | y | not (x and y)   x | y | (not x) or (not y)
=====================   =========================
  |   |                   |   |  
  |   |                   |   |  
  |   |                   |   |  
  |   |                   |   |  

x | y | not (x or y)   x | y | (not x) and (not y)
====================   ===========================
  |   |                  |   |  
  |   |                  |   |  
  |   |                  |   |  
  |   |                  |   |  
{% endhighlight %}
</section>

<section markdown="block">
### De Morgan's Law Truth Tables

{% highlight bash %}
x | y | not (x and y)   x | y | (not x) or (not y)
=====================   =========================
t | t | f               t | t | f
t | f | t               t | f | t
f | t | t               f | t | t
f | f | t               f | f | t

x | y | not (x or y)   x | y | (not x) and (not y)
====================   ===========================
t | t | f              t | t | f
t | f | t              t | f | t
f | t | t              f | t | t
f | f | t              f | f | t
{% endhighlight %}
</section>

<section markdown="block">
### De Morgan's Law 
__How can we rewrite this fragment of code from {{ site.bookt }}?__&rarr; 

{% highlight python %}
# "suppose we can slay the dragon only if our magic lightsabre sword 
# is charged to 90% or higher, and we have 100 or more energy units 
# in our protective shield." 

if not ((sword_charge >= 0.90) and (shield_energy >= 100)):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# first... demorgan's: 
if not (sword_charge >= 0.90) or not (shield_energy >= 100):
	# ...
{% endhighlight %}

{% highlight python %}
# next... logical opposites:
if (sword_charge < 0.90) or (shield_energy < 100):
	# ...
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Truthiness and Style
</section>

<section markdown="block">
### Truthiness

See this [crazy chart](http://docs.python.org/py3k/library/stdtypes.html#truth-value-testing) on the _intrinsic_ boolean value of various types.  The following values are considered false:

* None
* False
* 0 of any numeric type (0.0, 0)
* empty mapping or sequence type (We'll look at these later) - this includes the empty string '', "", etc.
</section>

<section markdown="block">
### Truthiness Examples

{% highlight python %}
a = ""
if a:
	print("true!")

a = 0
if a:
	print("true!")

a = "foo"
if a:
	print("true!")
{% endhighlight %}

</section>

<section markdown="block">
## [Built-In Modules Are Up Next!](modules.html)
</section>

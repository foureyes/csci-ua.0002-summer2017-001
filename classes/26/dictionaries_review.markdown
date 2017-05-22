---
layout: slides
title: Dictionaries 
---
<section markdown="block" class="title-slide">
# Dictionaries
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Dictionaries

__What's a dictionary?__

<div class="incremental" markdown="block">
* a __dictionary__ is an __unordered__ collection of key/value pairs.  
* it's a __mapping type__ - a data type that made of a collection of keys (think of names) and their associated values
</div>
</section>

<section markdown="block">
###  Dictionaries Syntax

__What's the syntax for a dictionary literal?  What delimits dictionaries?  What separates each name value pair?  What joins each name to a value?__

<div class="incremental" markdown="block">
* dictionaries are delimited by curly braces - { and }
* an empty dictionary is {}
* each key value pair in a dictionary is separated by a comma
* keys and values are linked together by a colon, the key before and the value after
* an example: 

{% highlight python %}
{"a":"value one", "b":2}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Retrieving Values at Keys 

__How do you retrieve a value at a key from a dictionary?  What happens if the key doesn't exist?__

<div class="incremental" markdown="block">
{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}
print(pizza["topping"])
print(pizza["extra topping"])

#...
{% endhighlight %}

{% highlight python %}
mushrooms
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'extra topping'
{% endhighlight %}
[btw, pizza!](http://www.pizzabrain.org/about-pizza-brain/)
</div>
</section>


<section markdown="block">
### Using the get Method

You can also retrieve a value from a dictionary without having to worry about KeyErrors by calling the __get__ method with two arguments:

* the key of the element you want to retrieve
* an optional default value in case that key doesn't exist yet

__What does this output?__

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}
print(pizza.get("extra topping", "peppers")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
peppers
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Key/Value Pairs 

So... things are a bit different when _adding_ keys and values to a dictionary.  There is __no error__ if you use a key that doesn't exist in order to assign a value to it (that is... to create a new key/value pair).

{% highlight python %}
# look ma, no keys!
d = {}
# but I can assign with no probz
d["problems"] = None
d["another key"] = "another value"
{% endhighlight %}
</section>

<section markdown="block">
### Key/Value Pairs Continued

If the key already exists... and you use the assignment operator, you are just associating a new value with an existing key.

__What does this code output?__

{% highlight python %}
d = {}
d["another key"] = "another value"
d["problems"] = None
d["another key"] = "something"
print(d["another key"])
print(d["problems"])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
something
None
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Creating New Keys/Values

__So.... how do you create a new key/value pair in a dictionary?__

<div class="incremental" markdown="block">

* you can assign a new value to a new key simply by indexing into a key that doesn't exist!
* this is different from reading from a key that doesn't exist (which gives us a KeyError)
* __for example...__

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}
pizza['sauce'] = 'tomato'
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Setting a New Key or Incrementing an Existing

If you're storing numbers as key values, and you want to increment a value at key or initialize it to 1 if it doesn't exist...

{% highlight python %}
d['a'] += 1
# ...but I don't know if a exists
{% endhighlight %}

You can catch an exception, or use get

{% highlight python %}
try:
	d['a'] += 1
except KeyError:
	d['a'] = 1

d['a'] = d.get('a', 0) + 1
{% endhighlight %}
</section>

<section markdown="block">
### Dictionaries and Mutability

__Are dictionaries mutable or immutable?__

<div class="incremental" markdown="block">
Dictionaries are __mutable__!

{% highlight python %}
d = {}
d["did not exist before"] = "some value"
# ok!
{% endhighlight %}
</div>
</section>

<section markdown="block">
### We Can Iterate Over Dictionaries

__Let's run this code.  What would you expect this to print?  Does it match what actually happens?__

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}
for topping in pizza:
  print(topping)
{% endhighlight %}
<div class="incremental" markdown="block">

{% highlight python %}
sauce
topping
crust
size
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Iterating Over Dictionaries Continued

__What can we conclude about dictionaries and iteration bsed on the output from the previous slides?__ &rarr;

<div class="incremental" markdown="block">
* iterating over a dictionary yields __keys only__
* again, dictionaries are __unordered__!
</div>
</section>

<section markdown="block">
### Iterating Over Every Key and Value

Another common way of iterating over a dictionary is to convert it to a list of tuples using the __items__() method.  It returns a list like object of tuples w/ the first element in each tuple the key, and the second, the value.  __What does the code below output?__

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}
t = pizza.items()
for i in t:
	print(i)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
('topping', 'mushrooms')
('crust', 'thin')
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Iterating Over Dictionaries Continued

__Of course, we can unpack that list of tuples.  How do we rewrite this using tuple unpacking?__

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}
t = pizza.items()
for i in t:
	print(i)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}
t = pizza.items()
for k, v in t:
	print(k, v)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Order!

__Remember that the dictionaries are _unorderd_...__

That means that when you iterate over elements, order isn't guaranteed

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms", "sauce":"tomato"}
t = pizza.items()
for k, v in t:
	print(k, v)

sauce tomato
topping mushrooms
crust thin
{% endhighlight %}
</section>

<section markdown="block">
### sorted

One last thing (that's not unique to dictionaries)...

There's a built-in function called __sorted__:

* it takes an iterable as an argument (dictionary, list, string, tuple)
* and it returns a sorted list version of the original argument
* there's an optional second argument which is the _actual function_ to use on each element for sorting
* the second argument is passed in as a key value pair joined with an equals sign (these are called keyword arguments)

{% highlight python %}
numbers = [4, -1, 1, -2, 2]
print(sorted(numbers))
print(sorted(numbers, key=abs))

[-2, -1, 1, 2, 4]
[-1, 1, -2, 2, 4]
{% endhighlight %}
</section>

<section markdown="block">
### sorted on Dictionary Values

We can use __sorted__ to iterate over a dictionary (which is inherently unordered) by value:

{% highlight python %}
pg = {"Ricky Rubio":12, "Derrick Rose":9, "Steve Nash":15}
for name in sorted(pg, key=pg.get):
	print(name, pg[name])
{% endhighlight %}
</section>

<section markdown="block">
### Summary Questions

* how do we construct a dictionary literal?
* how do we create an empty dictionary?
* are dictionaries mutable or immutable?
* are dictionaries ordered or unordered
* how do we access a value at a key... what happens if they key doesn't exist?
* what's the exception to the above?
* what's another way of accessing a value?
* when we us a regular for loop with a dictionary, what value is in the for loop variable?
* how do we get both keys and values when iterating?
</section>

<section markdown="block">
### Summary Answers

* dictionaries are delimited by curly braces, key value pairs are separated by commas, with each key and value joined by a colon
* {}
* they're __mutable__
* __unordered__ - order cannot be guaranteed
* d["some key"], excepion
* assignment
* get method
* the current key
* convert to a list of tuples using __items__()

</section>


<section markdown="block">
### Dictionaries Exercise

* write a program that asks the user for a word
* the program should output the total number of times each character in the word appears in the word
* example output:

{% highlight python %}
>hello
h 1
e 1
l 2
o 1
{% endhighlight %}
</section>

<section markdown="block">
### Counting Letters Version 1

{% highlight python %}
{% include classes/25/count_v1.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Counting Letters Version 2

{% highlight python %}
{% include classes/25/count_v2.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Counting Letters Version 3

{% highlight python %}
{% include classes/25/count_v3.py %}
{% endhighlight %}
<!--_-->
</section>

<section markdown="block">
### Counting Dice Rolls 

* roll two thee sided dice simultaneously 1000 times
* count the frequency of the results... 2 through 6
* pseudocode
	* generate two random numbers
	* do this 1000 times
	* keep track of the number of times a two is rolled... a three... up through six
	* use multiple assignment for initializing your counts!
</section>

<section markdown="block">
### Dice Rolls Solution 

We've done this before; here's a solution that uses a different variable for each possible number:

{% highlight python %}
import random
twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	if roll == 2:
		twos += 1
	if roll == 3:
		threes += 1
	if roll == 4:
		fours += 1
	if roll == 5:
		fives += 1
	if roll == 6:
		sixes += 1

print("twos: %s, threes: %s, fours: %s, fives: %s, sixes %s" % (twos, threes, fours, fives, sixes)) 
{% endhighlight %}
</section>

<section markdown="block">
### This Could be Less Tedious!

__Try reimplementing our dice program so that it uses a dictionary to store the frequency of rolls (each roll as a key, each value as a count).__  (hint: use the get method or use a try-except to deal with keys that don't exist).

<div class='incremental'>
{% highlight python %}
import random
freq_dice_rolls = {}
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	freq_dice_rolls[roll] = freq_dice_rolls.get(roll, 0) + 1
print(freq_dice_rolls)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Further Exercises

* keeping track of inventory
* phone book
</section>

<section markdown="block">
## [Review](review.html)
</section>






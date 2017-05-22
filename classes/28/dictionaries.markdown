---
layout: slides
title: Dictionaries Review 
---
<section markdown="block" class="title-slide">
# Dictionaries Review
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
###  Dictionary Attributes

Dictionaries are:

* __unordered__ - order cannot be guaranteed when iterating over
* __mutable__ - can be changed
* a __compound type__ - consists of other types
* a __mapping type__ - maps values to arbitrary objects
</section>

<section markdown="block">
###  Dictionary Syntax

* __What delimits dictionaries?__ &rarr;  
* __What separates each key/value pair?__ &rarr;  
* __What separates a key from a value?__ &rarr;

<div class="incremental" markdown="block">
* dictionaries are delimited by curly braces - __{__ and __}__
* each key value pair in a dictionary is separated by a __comma__
* keys and values are linked together by a __colon__, the key before and the value after
* {"key":"value"}
</div>
</section>

<section markdown="block">
###  Dictionary Syntax

In the following dictionary: 

* __What are the two keys - and their types?__ &rarr;
* __What are the two values - and their types?--__ &rarr;

{% highlight python %}
{(1, 2):"hello", 100:['other', 'types']}
{% endhighlight %}

<div class="incremental" markdown="block">
* keys
	* (1, 2) - tuple
	* 100 - int
* values
	* "hello" - str
	* ['other', 'types'] - list
</div>
</section>

<section markdown="block">
### Keys and Values

* List indexes can only be ints  __What kind of values can dictionary keys be?__ &rarr;
* __What about dictionary values?__ &rarr;

<div class="incremental" markdown="block">
* __keys__ - any immutable type, such as strings or tuples (or even ints)
* __values__ - can be any value... including other dictionaries!
</div>
</section>

<section markdown="block">
### Retrieving Values at Keys 

How do you retrieve a value at a key from a dictionary? __Here's a dictionary; get the value 4__ &rarr;

{% highlight python %}
vehicle = {"name":"car", "wheels":4}
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
vehicle['wheels']
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Non-Existent Keys

What happens if the key doesn't exist? __What happens in the following code?__ &rarr;

{% highlight python %}
vehicle = {"name":"car", "wheels":4}
vehicle['can fly']
{% endhighlight %}

<div class="incremental" markdown="block">
A __KeyError__ occurs!

{% highlight python %}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'can fly'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### However!  Non-Existent Keys Continued...

How do you add a new key/value pair to an existing dictionary? __Add the key 'can fly' to this dictionary, and set its value to the boolean value, False__ &rarr;

{% highlight python %}
vehicle = {"name":"car", "wheels":4}
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
vehicle['can fly'] = True
{% endhighlight %}
</div>
</section>

<section markdown="block">
### If the Key Does Exist

If the key already exists, using the assignment operator overwrites the existing value at that key. 

__What does this code output?__&rarr;

{% highlight python %}
vehicle = {"name":"car", "wheels":4}
vehicle['name'] = 'wagon'
print(vehicle)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
{'wheels': 4, 'name': 'wagon'}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Quick Summary on Keys

* dictionary __keys__ must be immutable
* you can use __indexing__ to retrieve values with keys - d['key']
* __retrieving__ an element at a key that doesn't exist __causes an error__
* __assigning__ a value to an element that doesn't exist __creates a new key/value pair__
</section>

<section markdown="block">
### Some Other Dictionary Operations

There are some familiar operations and functions that we can use on dictionaries:

* __del__ - removes a key value pair
{% highlight python %}
del d['some key']
{% endhighlight %}

* __in__ - checks if a key exists in a dictionary
{% highlight python %}
if 'some key' in d:
{% endhighlight %}

* __len__ - finds the number of key/value pairs in a dictionary 
{% highlight python %}
len(d)
{% endhighlight %}
</section>

<section markdown="block">
### Dictionary Methods

__Name the two dictionary methods that we learned, and describe what they do__ &rarr;

<div class="incremental" markdown="block">
* __get__(key, default) - retrieves an element at key; returns default if key doesn't exist
* __items__() - returns key/value pairs as list of tuples
</div>
</section>

<section markdown="block">
### get

Soooo... __what does the get method do again, what are its arguments, and what does it return?__ &rarr;

<div class="incremental" markdown="block">
* __key__ - the key that you're trying to retrieve
* __default__ - the default value that you get if the key doesn't exist
* __get__ either returns the value at __key__ or returns __default__ if key doesn't exist
* useful for avoiding a __KeyError__ 
</div>

</section>

<section markdown="block">
### Using the get Method

__What does this output?__

{% highlight python %}
vehicle = {"name":"hovercraft"}
number_of_wheels = vehicle.get('wheels', 0)
name_of_vehicle = vehicle.get('name', 'bathysphere') 
print(number_of_wheels)
print(name_of_vehicle)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
0
hovercraft
{% endhighlight %}
</div>
</section>

<section markdown="block">
### More Dictionary Methods

By the way, here are a few more dictionary methods:

* __values__() - get all values as a list-like structure
* __keys__() - get all keys as a list-like structure (
* __pop__(k, [d]) - removes element at key, _k_, and returns it (returns _d_ if _k_ doesn't exist)
* __popitem__() - removes and returns _some_ name/value pair as tuple
* __update__(dictionary) - overwrites all values at keys in original with values at keys from dictionary passed in
</section>

<section markdown="block">
### values, keys

__values__ and __keys__ give back _dictionary views_ (they essentially act like lists) of either all values or all keys of the dictionary that they're called on.  __What does this output?__ &rarr;

{% highlight python %}
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
print(vehicle.keys())
print(vehicle.values())
{% endhighlight %}

<div class="incremental" markdown="block">
Note that the __order of the keys and values cannot be guaranteed!__
{% highlight python %}
dict_keys(['can fly', 'wheels', 'name'])
dict_values([False, 0, 'bathysphere'])
{% endhighlight %}
</div>
</section>

<section markdown="block">
### pop

__pop__ removes and returns the item at the key specified.  __What does this output?__&rarr;

{% highlight python %}
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
result1 = vehicle.pop('can fly')
result2 = vehicle.pop('floats', False)
print(result1)
print(result2) 
print(vehicle)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
False
False
{'wheels': 0, 'name': 'bathysphere'}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### popitem

__popitem__ removes and returns an _arbitrary_ key/value pair.  __What does this output?__&rarr;

{% highlight python %}
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
result1 = vehicle.popitem()
print(result1)
print(vehicle)
{% endhighlight %}

<div class="incremental" markdown="block">
Note that the key/value pair removed and returned __will not always be the same!__

{% highlight python %}
('can fly', False)
{'wheels': 0, 'name': 'bathysphere'}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### update

__update__ adds key/value pairs (or updates values if keys already exist) from another dictionary to the dictionary that update is called on.  __What does this output?__&rarr;

{% highlight python %}
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
another_vehicle = {'can float':True, 'name':'boat'}
vehicle.update(another_vehicle)
print(vehicle)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
{'can fly': False, 'wheels': 0, 'name': 'boat', 'can float': True}
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Changing a Value Based on the Existing Value

To change a value base on an existing value, such as incrementing a number, you can simply do something like this (adds one to the current value at fga):

{% highlight python %}
d = {'fgm':1, 'fga':2}
d['fga'] = d['fga'] + 1
{% endhighlight %}

</section>

<section markdown="block">
### Changing a Value Based on the Existing Value

But what if it doesn't exist yet?  __What happens here?__ &rarr;

{% highlight python %}
d = {'fgm':1 }
d['fga'] = d['fga'] + 1
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'fga'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Avoiding KeyError

__What are a couple of ways of working around incrementing a value at a key when there may be keys that don't exist?__ &rarr;

<div class="incremental" markdown="block">
Use __exception handling__ or use __get__ and take advantage of assignment using keys that don't exist.

{% highlight python %}
try:
	d['a'] += 1
except KeyError:
	d['a'] = 1

d['a'] = d.get('a', 0) + 1
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Dictionaries and Mutability

__Dictionaries are mutable!__

* assignment works for changing values at keys
* keys/values can be added and removed
* note that many dictionary methods actually change the dictionary in place

__What are some dictionary methods that change the dictionary in place?__ &rarr;

<div class="incremental" markdown="block">

* pop
* popitem
* update
</div>
</section>

<section markdown="block">
### Iterating Over Dictionaries

__What does this code print out?__ &rarr;

{% highlight python %}
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
for attribute in vehicle:
  print(attribute)
{% endhighlight %}
<div class="incremental" markdown="block">

Note that __same order cannot be guaranteed__
{% highlight python %}
can fly
wheels
name
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Iterating Over Dictionaries Continued

We can see that iterating over a dictionary gives back keys.  Additionally, the keys are unordered. __How would be get every key *and* value using the dictionary below?__ &rarr;

{% highlight python %}
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
{% endhighlight %}

<div class="incremental" markdown="block">
Use the key that you get from looping key to index into the dictionary, or use get.

{% highlight python %}
for attribute in vehicle:
  print('%s, %s' % (attribute, vehicle[attribute]))
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Back to the items Method!

A dictionary can be converted to a list of tuples using the __items__() method.  

* it returns a list like object of tuples 
* each tuple has two elements
* the first element is the key, and the second, the value  

__What does the code below output?__ &rarr;

{% highlight python %}
vehicle = {"name":"hovercraft", "wheels":0}
pairs = vehicle.items()
for pair in pairs:
	print(pair)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
('wheels', 0)
('name', 'hovercraft')
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Iterating Over Dictionaries Continued

__What's another way of looping over a dictionary to get keys and values without having to index into the original dictionary?__ &rarr;

{% highlight python %}
vehicle = {"name":"hovercraft", "wheels":0}
{% endhighlight %}

<div class="incremental" markdown="block">
Use __tuple unpacking__! within your for-loop.

{% highlight python %}
pairs = vehicle.items()
for k, v in pairs:
	print('%s, %s' % (k, v))
{% endhighlight %}
</div>
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
### Some Quick Questions

* name as many dictionary methods as you can!
* name two ways of accessing a value at a key
* how do you create an empty dictionary?
* are dictionaries mutable or immutable?
* are dictionaries ordered or unordered
* how do you add a new key/value pair to an existing dictionary?
* name 3 ways of removing items from a dictionary
</section>

<section markdown="block">
### And Their Answers

* pop, popitem, get, keys, values, update, etc.
* __indexing__ with a __key__ or using __get__
* and empty dictionary is __{}__
* dictionaries are __mutable__
* dictionaries are __unordered__
* use assignment on key that doesn't exist
* use __del__, __pop__ or __popitem__

</section>

<section markdown="block">
## Some Dictionary Exercises
</section>

<section markdown="block">
### Counting Letters

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
### An Implementation Using Dictionaries


{% highlight python %}
import random
freq_dice_rolls = {}
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	freq_dice_rolls[roll] = freq_dice_rolls.get(roll, 0) + 1
print(freq_dice_rolls)
{% endhighlight %}
</section>

<section markdown="block">
### Dice Rolls Without Dictionaries  

Let's compare that to our previous solution without dictionaries!

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
### A List of Contacts

__Create a text-base contact list that allows you that stores first name, last name and room #__ &rarr;

It should support the following functionality:

* (a)dd contact
* (p)rint all contacts
* (f)ind contact by first name
* (q)uit

The primary interface will be a prompt that will continually ask the user for a letter (a, p, f or q)...
</section>

<section markdown="block">
### Add a Contact Example Interaction

* adding will ask for further input...
* first, last and room #

{% highlight bash %}
(a)dd contact, (p)rint all contacts, (f)ind contact, (q)uit 
>a
first name plz 
>tim
last name plz 
>test
room # plz 
>200
{% endhighlight %}
</section>

<section markdown="block">
### Find a Contact Example Interaction

Finding a contact:

* asks for more input - the first name of the person to find
* and prints out the contact

{% highlight bash %}
(a)dd contact, (p)rint all contacts, (f)ind contact, (q)uit 
>f
what's the firs name of the person you'd like to find? 
>tim
last name - test
first name - tim
room - 200
{% endhighlight %}
</section>

<section markdown="block">
### Print All Contacts Example Interaction

{% highlight bash %}
(a)dd contact, (p)rint all contacts, (f)ind contact, (q)uit 
>p
last name - test
first name - tabitha
room - 100

last name - test
first name - tim
room - 200
{% endhighlight %}
</section>

<section markdown="block">
### Before Diving In...

* how do we want to represent the data?
* can we break down the program into smaller chunks
* diagram if necessary (flow charts, sequence diagrams, etc.)
* write some pseudocode
</section>

<section markdown="block">
## One Possible Solution...
</section>

<section markdown="block">
### Storage

How about using a __list of dictionaries__ to store contacts?

Here's an example with one contact:

{% highlight python %}
[{'first name': 'tabitha', 'last name': 'test', 'room': 100}]
{% endhighlight %}
</section>

<section markdown="block">
### Some Functions

We can break down the code into smaller chunks of functionality:

{% highlight python %}

def contact_as_string(contact):
	s = ''
	for attribute, value in contact.items():
		s += '%s - %s\n' % (attribute, value)
	return s

def print_all_contacts(contact_list):
	for c in contact_list:
		print(contact_as_string(c))
{% endhighlight %}
</section>

<section markdown="block">
### And More Functions

{% highlight python %}
def find_contact(contact_list, attribute, value):
	for c in contact_list:	
		if c[attribute] == value:
			return c
	return None

def find_contact_by_first(contact_list, first):
	return find_contact(contact_list, 'first name', first)
{% endhighlight %}

</section>
<section markdown="block">
### The Main Loop...

We can use the previous functions in a while loop that drives the interaction with the user:

{% highlight python %}

contacts = [{'first name': 'tabitha', 'last name': 'test', 'room': 100}]
while True:
	command = input('(a)dd contact, (p)rint all contacts, (f)ind contact, (q)uit \n>')
	if command == 'a':
		first = input('first name plz \n>')
		last = input('last name plz \n>')
		room = input('room # plz \n>')
		contacts.append({'first name': first, 'last name': last, 'room': room})
	elif command == 'p':
		print_all_contacts(contacts)
	# continued in next slide...
{% endhighlight %}
</section>

<section markdown="block">
### The Main Loop Continued

{% highlight python %}
	elif command == 'f':
		name_to_find = input('what\'s the firs name of the person you\'d like to find? \n>')
		c = find_contact_by_first(contacts, name_to_find)
		if c != None:
			print(contact_as_string(c))
		else:
			print('Contact not found')
	elif command == 'q':
		break
{% endhighlight %}
</section>

<section markdown="block">
## Review End
</section>

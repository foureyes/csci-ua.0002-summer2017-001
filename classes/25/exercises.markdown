---
layout: slides
title: Exercises 
---

<section markdown="block" class="title-slide">
# Exercises
{% include title-slide-footer.html %}
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
### Dice Rolls Solution 

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

__Create a text-based contact list that allows you to store first name, last name and room #__ &rarr;

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

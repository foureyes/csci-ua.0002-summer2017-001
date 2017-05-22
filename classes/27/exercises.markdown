---
layout: slides
title: Review 
---
<section markdown="block" class="title-slide">
# Exercises
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Dictionary Exercises

First, check out some dictionary exercises from the [previous class](../26/exercises.html).
</section>

<section markdown="block">
## State Abbreviations
</section>

<section markdown="block">
### State Abbreviations

Create a program that quizzes the user on state abbreviations using the dictionary below:

{% highlight python %}
states = {'New York':'NY', 'New Jersey':'NJ', 'Connecticut':'CT'}
{% endhighlight %}

Example output is:

{% highlight bash %}
What is the abbreviation for New Jersey?
>NJ
You're right!  NJ is the abbreviation for New Jersey
-----
What is the abbreviation for New York?
>NY
You're right!  NY is the abbreviation for New York
-----
What is the abbreviation for Connecticut?
>CC
Nope!  CT is the abbreviation for Connecticut
-----
You got 2 right out of 3 questions!
{% endhighlight %}
</section>

<section markdown="block">
###  State Abbreviations

Starting with the following dictionary:

{% highlight python %}
states = {'New York':'NY', 'New Jersey':'NJ', 'Connecticut':'CT'}
{% endhighlight %}

Write a program that:

* continuously asks for an abbreviation based on a state name ('What's the abbreviation for New York?')
* end when all of the states in the dictionary have been asked
* display 'wrong' or 'right' depending on if user typed in the appropriate abbreviation
* keep track of the number of right answers
* at the end of the program, print out the number of right answers compared to the total
</section>
<section markdown="block">
### State Abbreviations

Pseudocode:

* go through every name/value pair
	* ask the user for input
	* if the input matches the value, 
		* increment # right 
		* display 'right' message
	* otherwise, display 'wrong' message
* print out the number right and the number total
</section>

<section markdown="block">
### State Abbreviations

{% highlight python %}
states = {'New York':'NY', 'New Jersey':'NJ', 'Connecticut':'CT'}

right = 0
for name, abbreviation in states.items():
	answer = input('What is the abbreviation for %s?\n>' % name)
	if answer == states[name]:
		print('You\'re right!  %s is the abbreviation for %s' % (abbreviation, name))
		right += 1
	else:
		print('Nope!  %s is the abbreviation for %s' % (abbreviation, name))
	print('-----')
print('You got %s right out of %s questions!' % (right, len(states)))
{% endhighlight %}
</section>

<section markdown="block">
## Run Length Decoding
</section>

<section markdown="block">
### Run Length Decoding

Imagine that you have a list of tuples...

* the list represents a word
* each tuple in the list is two elements
* the first element is a letter in the word
* the second element is the number of times that letter appears consecutively

For example:

* [('E', 4), ('K', 1)] &rarr; "EEEEK"
* [('V', 1), ('O', 2), ('D', 1), ('O', 2)] &rarr; "VOODOO"
</section>

<section markdown="block">
### Run Length Decoding

Write a function called run_length_decode:

* it takes a __list__ of two-element tuples as an argument
* it gives back a string

Example usage:

{% highlight python %}
compressed = [('E', 4), ('K', 1)]
print(run_length_decode(compressed))
# prints out EEEEK

compressed = [('V', 1), ('O', 2), ('D', 1), ('O', 2)]
print(run_length_decode(compressed))
# prints out VOODOO
{% endhighlight %}
</section>

<section markdown="block">
### Run Length Decoding

{% highlight python %}
def run_length_decode(coded):
	s = ''
	for letter, frequency in coded:
		s += letter * frequency
	return s
{% endhighlight %}
</section>


<section markdown="block">
## Every Third
</section>

<section markdown="block">
### Every Third

Write a function called every_third_name:

* it should take a list of names as an argument
* it will give back a new list composed of every third name in the original list

For example:

{% highlight python %}
names = ['Bob', 'Alice', 'Carol', 'Dan', 'Eve', 'Frank', 'Gus', 'Heidi', 'Ivan']
print(every_third_name(names))
# prints out ['Carol', 'Frank', 'Ivan']
{% endhighlight %}
</section>

<section markdown="block">
### Every Third

A few ways to approach this:

* use enumerate to get the index 
* use a count variable to keep track of index
* use range to generate a series of indexes
* use a list comprehension
</section>

<section markdown="block">
### Every Third

With enumerate ...

{% highlight python %}
names = ['Bob', 'Alice', 'Carol', 'Dan', 'Eve', 'Frank', 'Gus', 'Heidi', 'Ivan']

def every_third_v1(names):
	new_list = []
	for number, name in enumerate(names):
		if (number + 1) % 3 == 0:
			new_list.append(name.lower())
	return new_list

print(every_third_v1(names))
{% endhighlight %}
</section>

<section markdown="block">
### Every Third

Incrementing a _counter_ variable (called number) ...
{% highlight python %}
names = ['Bob', 'Alice', 'Carol', 'Dan', 'Eve', 'Frank', 'Gus', 'Heidi', 'Ivan']

def every_third_v2(names):
	new_list = []
	number = 1
	for name in names:
		if (number) % 3 == 0:
			new_list.append(name.lower())
		number += 1
	return new_list

print(every_third_v2(names))
{% endhighlight %}
</section>

<section markdown="block">
### Every Third

Using range ...

{% highlight python %}
names = ['Bob', 'Alice', 'Carol', 'Dan', 'Eve', 'Frank', 'Gus', 'Heidi', 'Ivan']

def every_third_v3(names):
	new_list = []
	for i in range(len(names)):
		if (i + 1) % 3 == 0:
			new_list.append(names[i].lower())
	return new_list
	
print(every_third_v3(names))
{% endhighlight %}
</section>

<section markdown="block">
### Every Third

List comprehension ...

{% highlight python %}
names = ['Bob', 'Alice', 'Carol', 'Dan', 'Eve', 'Frank', 'Gus', 'Heidi', 'Ivan']
print([name.lower() for number, name in enumerate(names) if (number + 1) % 3 == 0])
{% endhighlight %}
</section>

<section markdown="block">
## Synonyms
</section>

<section markdown="block">
### Synonyms

Write a program that:

* loads a [text file](synonyms.txt) of words and synonyms
	* each line in the file will be word:synonym
	* tranquil:peaceful
* continually asks a user for a word
* prints out that word's synonym if it exists
* otherwise, prints out an appropriate 'does not exist' message
* lastly, pressing q stops the loop

{% highlight bash %}
Give me a word or (q)uit
> quick
fast
Give me a word or (q)uit
> slow
No synonyms for slow!
Give me a word or (q)uit
> q
{% endhighlight %}
</section>

<section markdown="block">
### Synonyms

What are the main steps for this program?

<div class="incremental" markdown="block">
* load data from file
	* open a file
	* read its contents into some data structure
* continually ask the user for a word
	* display the synonym if the word exists
	* display a default message if the word doesn't exist
	* quit if the user typed in q
</div>
</section>

<section markdown="block">
### Synonyms

Let's start with part 1.  

* download the file [synonyms.txt](synonyms.txt) 
* read it into a dictionary, with the original word as the key, and the synonym as the value
* note that the format for each line is word:synonym

<div class="incremental" markdown="block">
{% highlight python %}
d = {}
f = open('synonyms.txt', 'r')
for line in f:
	line 
	parts = line.strip().split(':')
	d[parts[0]] = parts[1]
print(d)
f.close()
{% endhighlight %}
</div>
</section>
<section markdown="block">
### Synonyms

Now that we've built our dictionary, ask the user for a word, and print out the appropriate response:

<div class="incremental" markdown="block">
{% highlight python %}
d = {}
f = open('synonyms.txt', 'r')
for line in f:
	line 
	parts = line.strip().split(':')
	d[parts[0]] = parts[1]
f.close()

while True:
	word = input('Give me a word or (q)uit\n> ')
	if word == 'q':
		break
	synonym = d.get(word, 'No synonyms for %s!' % word)
	print(synonym)
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Half
</section>

<section markdown="block">
### Half (New List)

Write a function half_value_v1 that takes a list of numbers and returns a __new list__ with all of the numbers halved.  Here's some example output:

{% highlight python %}
result = half_value_v1(my_numbers)
print('Function returned %s' % (result))
print('my_numbers is still %s' % (my_numbers))
{% endhighlight %}

Output:

{% highlight bash %}
Function returned [5.0, 4.0, 3.0]
my_numbers is still [10, 8, 6]
{% endhighlight %}
</section>

<section markdown="block">
### Half (New List)

{% highlight python %}
my_numbers = [10, 8, 6]
def half_value_v1(numbers):
	new_numbers = []
	for n in numbers:
		new_numbers.append(n / 2)
	return new_numbers

result = half_value_v1(my_numbers)
print('Function returned %s' % (result))
print('my_numbers is still %s' % (my_numbers))
{% endhighlight %}
</section>

<section markdown="block">
### Half (In Place)

Write a function half_value_v2 that takes a list of numbers and __modifies the list passed in__.  It should not return a value!

{% highlight python %}
result = half_value_v1(my_numbers)
print('Function returned %s' % (result))
print('my_numbers is still %s' % (my_numbers))
{% endhighlight %}

Output:

{% highlight bash %}
Function returned None
my_numbers is now [5.0, 4.0, 3.0]
{% endhighlight %}
</section>


<section markdown="block">
### Half (In Place)

{% highlight python %}
my_numbers = [10, 8, 6]
def half_value_v2(numbers):
	for i, n in enumerate(numbers):
		numbers[i] = n / 2

result = half_value_v2(my_numbers)
print('Function returned %s' % (result))
print('my_numbers is now %s' % (my_numbers))
{% endhighlight %}
</section>

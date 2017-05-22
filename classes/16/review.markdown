---
layout: slides
title: Strings as a Compound Data Type - Review 
---
<section markdown="block" class="title-slide">
# Strings as a Compound Data Type - Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Indexing

__What is the index of the following characters in these strings? &rarr;__

1. 'h' in "hi bob!"
2. '!' in "hi bob!"
3. ' ' in "hi bob!"

<div class="incremental" markdown="block">
{% highlight python %}
1. 0
{% endhighlight %}
{% highlight python %}
2. 6
{% endhighlight %}
{% highlight python %}
3. 2
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Indexing Continued

__What's the output of the following code? &rarr;__

{% highlight python %}
idx, animal = -2, "tiger"
print(animal[-1])
print(animal[idx])
print("animal"[2])
print(animal[idx + 2])
print(animal[idx + 100])
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
r
{% endhighlight %}
{% highlight python %}
e
{% endhighlight %}
{% highlight python %}
i
{% endhighlight %}
{% highlight python %}
t
{% endhighlight %}
{% highlight python %}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Summary for Indexing

* a __string__ is an __ordered sequence__ of characters
* an __index__ is the numeric position of an element within a collection of elements
* in the case of __strings__, __index__ is the position of the char within a string
* the __first element__ is at __index 0__, and it increments from there
* __last element__ is at index __length - 1__ (len(s) - 1) 
* also, __last element__ is at index __-1__
* __second to last element__ is at index __-2__
* you can retrieve a specific character from a string by indexing into it
* if index doesn't exist, you will get an error
</section>

<section markdown="block">
### Indexing Syntax

The __indexing__ syntax is as follows:

* value (as variable or literal or even function call)
* open square bracket
* index of desired char (an integer)
* close square bracket
</section>

<section markdown="block">
### Indexing Examples

{% highlight python %}
# index into string that's bound to a variable name
a = "foo"
a[0]
# index into a string literal
"foo"[0]
# index into the return result of a function
def give_back_foo():
	return "foo"

give_back_foo()[0]
{% endhighlight %}
</section>

<section markdown="block">
### Are Strings Mutable?

__What happens if I try to change the string "pugs" into "hugs" using inexing and the assignment operator? &rarr;__

{% highlight pycon %}
"hugs"[0] = 'p'
{% endhighlight %}

<div class="incremental" markdown="block">
* strings are __not mutable__
* you can read values by indexing into a string
* however, you can't change characters in a string
{% highlight pycon %}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
{% endhighlight %}
</div>
</section>

<section markdown="block">
### An Index That Doesn't Exist

__What happens if I try to access an index that doesn't exist? &rarr;__

{% highlight python %}
word = "pugs"
print(word[50])
{% endhighlight %}

<div class="incremental" markdown="block">
* accessing an index that doesn't exist causes an error
* specifically, an IndexError
{% highlight python %}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of ranges
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Using Every Character in a String

What if we want to do something to each character in a string? 

* count the number of exclamation points I used in my slides!?
	* by going through every character 
	* and incremting a count variable
* take a word and create a new word by changing all vowels into numbers for a variant of "L33T SP34K"
	* construct a new string
	* go through every character of the original string
	* add a number for cerain characters... or the original character
</section>

<section markdown="block">
### Looping Over Each Character

We can iterate over every character that's in a string.  

* we've used a construct that lets us iterate over every element in an ordered sequence
* __what was that construct?&rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
# for loops!
for c in "hello":
  print(c)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### For Loops and Strings

{% highlight python %}
my_crazy_string = "oh my!"
for c in my_crazy_string:
  print(c)
{% endhighlight %}

* for loops allow us to iterate over every char in a string.  
* similar to looping over a sequence of #'s
* variable specified in loop represents the current char
* the loop continues until there are no letters left
* the above code prints out:

{% highlight python %}
o
h
 
m
y
!
{% endhighlight %}
</section>

<section markdown="block">
### Another Example

The following code:

* uses a for loop to go over every letter in "jetpack"
* for each letter, prints out the letter with a suffix of "am" appended it

{% highlight python %}
word = "jetpack"
suffix = "am"
for c in word:
	print(c + suffix)
{% endhighlight %}
</section>


<section markdown="block">
### A Quick Aside on Assert 

{% highlight python %}
assert <some expression that results in a bool>, <a string>
{% endhighlight %}

* __assert__ statements consist of the __keyword assert__
* followed by _any_ expressions that results in a bool
* followed by a string
* causes an error if condition is not True
* we use asserts to test expected and actual values of functions
* goal is to get __no output__ (though you can print something after saying that tests passed)
* __try writing your tests first!__

{% highlight python %}
assert expected == actual, "describe test"
{% endhighlight %}
</section>

<section markdown="block">
### A Quick Aside on Break 

The __break__ statement immediately stops the execution of a loop. __What does the following code print out? &rarr;__

{% highlight python %}
for letter in "challenge":
	if letter == 'a':
		break
	print(letter + "at")
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
cat
hat
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Quick Aside on Docstrings 

A __docstring__ is a triple-quoted string immediately following the header of a function definition.

* it describes what the function does
* it's essentially an inline comment / documentation
* some tools pick up on this documentation (like the help function in the interactive shell)

<div class="incremental" markdown="block">
{% highlight python %}
def foo()
	"""gives back a greeting"""
	return "hi"
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Letter in Word (v1)

__Try implementing this function!__ 

* create an ipo chart
* write assertion statements (how many?)
* write a doc string
* implement a function called letter_in_word
* it should take two arguments, a letter and a word
* it should return True if the letter is in the word, otherwise, return False
* use assert on a True case and on a False case
* implement using __two return statements__

</section>


<section markdown="block">
### Letter in Word (v1) Continued

{% highlight python %}
{% include classes/17/letter_in_word.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Letter in Word (v2)

Here's another way of doing it using __break__.

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/16/letter_in_word.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Letter in Word Revisited

There are actually a couple of much easier ways to do this rather than writing our own function. __What are two ways of determining whether or not a string is a substring of another string?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
# use the in operator:
'a' in 'aardvark'

# use the find method:
'aardvark'.find('a')
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Looping Over Strings Summary / Syntax

* for loops allow us to iterate over every character in a string.  
* it's similar to looping over a sequence of #'s
* the variable in the loop head represents the current character
* the loop continues until there are no letters left

</section>


<!--
<section markdown="block">
### Letter in Word (v1)

Using loops, we can implement a function that determines whether a letter is in a word (there's actually already a construct in Python that does this...).

* we'll use assert to test a True case and a False case
* this particular implementation uses two __return__ statements

{% highlight python %}
{% include classes/17/letter_in_word.py %}
{% endhighlight %}
</section>
-->


<section markdown="block">
### How Many A's Are in Aardvark?

__Write a function that counts how many times a letter occurs in a word. &rarr;__

* create a function called __count\_letters__
* use assert on at least two cases to test, and write a docstring
* create an ipo chart
	* it should take __two arguments__: a letter and a word
	* it should __return an integer__

{% highlight python %}
>>> print(count_letters('a', 'aardvark'))
3
{% endhighlight %}

<!--_end bold-->
</section>

<section markdown="block">
### How Many A's Are in Aardvark? Solution

{% highlight python %}
{% include classes/17/count.py %}
{% endhighlight %}

</section>

<section markdown="block">
### Counting letters Revisited

Just like finding a substring, there's a much easier way to find the number of times a substring occurs inside another string. __What is the method that let's us do this?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
# it's just count!
"banana".count('an')
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Construct a String With Spaces After Every Letter

__Let's write a function that takes a string and puts a space after every character. &rarr;__

* create a function called __insert\_spaces__
* use assert on at least two cases to test (a good one might be empty string), write a doc string
* create an ipo chart
	* it should take two one argument: a string
	* it should return a string

{% highlight python %}
>>> print(insert_spaces('aaaah!'))
a a a a h ! 
{% endhighlight %}

<!--_end bold-->
</section>

<section markdown="block">
### Construct a String With Spaces After Every Letter Solution

{% highlight python %}
{% include classes/17/space.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Slicing

You can also retrieve a __substring__ from another string.  

* you can get a section of consecutive characters from a string
* example: "ana" is a substring in the string "banana"

This is done using slicing.  Slicing syntax works as follows:

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> "placate"[3:6]
'cat'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Slicing Syntax

Looking at the slicing code again:

{% highlight pycon %}
>>> "placate"[3:6]
'cat'
{% endhighlight %}

The general case is:

{% highlight pycon %}
some_long_string[m:n]
{% endhighlight %}
 
* __m__ is the start index and __n__ is the end index.
* the resulting substring starts at __m__, and goes up to, but does __not__ include __n__
</section>


<section markdown="block">
### Substring Exercises 

Write the slice to pick out the following substring from the original string:

{% highlight python %}
s = "gone!"
#    01234
{% endhighlight %}

1. go
2. on
3. one
4. one!

<div class="incremental" markdown="block">
{% highlight python %}
s[0:2]
{% endhighlight %}
{% highlight python %}
s[1:3]
{% endhighlight %}
{% highlight python %}
s[1:4]
{% endhighlight %}
{% highlight python %}
s[1:5]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Some Slicing Tricks

* leaving out the first index (before the colon - m) starts at the beginning of the string
* leaving out the second index (after the colon - n), ends at the end of the string 
* if the second index, n is greater than the length of the string, up to the end is sliced

{% highlight python %}
"eggs and ham"[:4] #eggs
"eggs and ham"[9:] #ham
"eggs and ham"[9:100] #ham
{% endhighlight %}
</section>

<section markdown="block">
###  An Easier Way to Tell if a Letter is in a Word

Use the __in__ operator!

* __in__ tests for membership
* it takes two operands, one on each side
* if the operand on the left is in the operand on the right, __in__ returns True
* in the case of strings, __in__ tests if one string is a substring of the other 

</section>

<section markdown="block">
### In Examples

{% highlight pycon %}
>>> word = "ice cream"
>>> letter = "a"
>>> letter in word
True
>>> "cat" in "vacation"
True
>>> "cat" in "work"
False
>>> 
{% endhighlight %}
</section>

<section markdown="block">
###  In / Not In 

Some other things to note:

A string is always a substring of itself.
{% highlight pycon %}
>>> "vacation" in "vacation"
True
{% endhighlight %}

Empty string is always a substring of any other string.
{% highlight pycon %}
>>> "" in "vacation"
True
{% endhighlight %}

__not in__ is the logical opposite of the __in__ operator
{% highlight pycon %}
>>> "cat" not in "vacation"
False
{% endhighlight %}
</section>

<section markdown="block">
### First Word in a Sentence

Create a function that returns the first word in a sentence.

* assume that spaces separate words
* use assert to test with a sentence 
	* 0 words
	* 1 word
	* &gt; 1 words
	* only spaces
* it should take one argument, a string
* it should return a string
* if the original string is only one word, return that word
* if the original string is empty, return an empty string
* if the original string is only white space, return an empty string
* __hint__: substring may be helpful
* __hint__: how do you find the end index of substring?

</section>

<section markdown="block">
### First Word in a Sentence Potential Solution

{% highlight python %}
{% include classes/17/get_first_word.py %}
{% endhighlight %}
</section>


<section markdown="block">
### Is Digit?

Create a function that determines whether or not a string only has numbers (0-9) in it.

* use assert to test a string composed of
	* only digits
	* digits and other characters
	* only non numeric characters
	* empty string
* it should take one argument, a string
* it should return a True only if the only characters in it are 0 through 9
* if the original string is empty, return False
* __hint__: __not in__ may be useful
</section>

<section markdown="block">
### Is Digit? Potential Solution
{% highlight python %}
{% include classes/17/is_digit.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Is Digit Revisited

And of course, there's already a couple of methods that do this. __What are they?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
"123".isdigit()
"123".isnumeric()
"abc".isdigit()
"abc".isnumeric()
{% endhighlight %}
</div>

</section>


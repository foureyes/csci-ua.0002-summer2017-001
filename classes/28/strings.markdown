---
layout: slides
title: Strings 
---
<section markdown="block" class="title-slide">
# Strings
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
2. 6
3. 2
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Indexing Continued

__What's the output of the following code? &rarr;__

{% highlight python %}
idx = -2
animal = "tiger"
print(animal[-1])
print(animal[idx])
print("animal"[2])
print(animal[idx + 2])
print(animal[idx + 3])
print(animal[idx + 100])
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
r
e
i
t
i
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
* the first element has index 0, and it increments from there
* in the case of __strings__, __index__ is the position of the char within a string
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

{% highlight python %}
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
### Iterating Over Characters in a String

Here's a program that prints out every letter in "jalopy" with 'eer' appended to it.

<div class="incremental" markdown="block">
{% highlight python %}
word = "jalopy"
for c in word:
	print(c + 'eer')
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Looping Over Strings Summary / Syntax

* for loops allow us to iterate over every character in a string.  
* it's similar to looping over a sequence of #'s
* the variable in the loop head represents the current charecter
* the loop continues until there are no letters left

</section>

<section markdown="block">
### Letter in Word Example

Using loops, we can implement a function that determines whether a letter is in a word (there's actually already a construct in Python that does this... ).
</section>

<section markdown="block">
### Letter in Word (v1)

* we'll use assert to test a True case and a False case
* this particular implementation uses two __return__ statements

{% highlight python %}
{% include classes/17/letter_in_word.py %}
{% endhighlight %}
</section>

<section markdown="block">
### The break Statement

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
### Letter in Word (v2)

Here's another way of implementing letter_in_word using __break__.

{% highlight python %}
{% include classes/16/letter_in_word.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Slicing

Python allows you to carve out a smaller string (a __substring__) from another string by using __slicing__.

* example: "sand" is a substring in the string "sandwich"
* slicing syntax:

{% highlight python %}
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
{% endhighlight %}

1. go
2. on
3. one
3. one!

<div class="incremental" markdown="block">
{% highlight python %}
s[0:2]
s[1:3]
s[1:4]
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
* it takes to operands, one on each side
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
### Strings as Objects

Some methods that can be called on string objects:

1. __upper__() 
2. __lower__()
3. __isdigit__()
4. __isalpha__()
5. __find__(sub[, start[, end]])
6. __format__(...)
7. __strip__([chars])
8. __split__(str) turns a string into a list based on a separator string
9. __join__(list) turns a list into a string based on the string it's called on

</section>

<section markdown="block">
### upper() and lower()

__upper__() and __lower__() return the string that the method was called on in either all uppercase or all lowercase.  __What would the following print out? &rarr;__

{% highlight python %}
print("this should be uppercase".upper())
print("THIS SHOULD BE LOWERCASE".lower())
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
THIS SHOULD BE UPPERCASE
this should be lowercase
{% endhighlight %}
</div>
</section>

<section markdown="block">
### isdigit() and isalpha()

__isdigit__() and __isalpha__() test whether a string is only numbers or letters (both return False if empty string).  __What would the following print out? &rarr;__

{% highlight python %}
print("123".isdigit())
print("1.23".isdigit())
print("one two three".isdigit())
print("onetwothree".isalpha())
print("one two three".isalpha())
print("one!".isalpha())
print("1".isalpha())
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
True
False
False
True
False
False
False
{% endhighlight %}
</div>
</section>



<section markdown="block">
### find()

__find__() returns the first index where the argument (a character or substring) is found.  It returns -1 if the substring is not in the original string.

{% highlight pycon %}
print("hello".find("h"))
print("hello".find("x"))
print("hello".find("lo"))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight pycon %}
0
-1
3
{% endhighlight %}
</div>
</section>

<section markdown="block">
### strip()

__strip__() removes leading and trailing whitespace (it can also remove other leading and trailing characters).  What do you think this results 

{% highlight python %}
print("  spaces all around   ".strip())
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
spaces all around
{% endhighlight %}
</div>
</section>

<section markdown="block">
### format()

Format is like string interpolation, but possibly easier?! 

* instead of %s, use curly braces and the number of the argument as a placeholder {0}, {1}
* numer corrseponds to each argument in the call, 0 being the first
* __What do you think the following returns? &rarr;__

{% highlight python %}
"{0} elephants".format("twenty")
"{0} elephants".format(20)
"{0} elephants".format(20, 100)
"{1} elephants".format(20, 100)
"{0} elephants and {1} peanuts".format(20, 100)
{% endhighlight %}
</section>

<section markdown="block">
### format() results

{% highlight pycon %}
twenty elephants
20 elephants
20 elephants
100 elephants
20 elephants and 100 peanuts
{% endhighlight %}
</section>

<section markdown="block">
### The Built-In len() Function

__len__ is a built-in function that Returns the length of a sequence

* it is __not a method__, so you do not call it on an object
* however, you can pass a value to it, and it will return its length
* for strings, it will return the number of characters
* last index is the len(s) - 1

{% highlight python %}
print(len("cat"))
# gives 3
{% endhighlight %}
</section>


<section markdown="block">
### Example Question #1

__Let's write a function that counts how many letters are in a word. &rarr;__

* use assert on at least two cases to test
* it should take two arguments: a letter and a word
* it should return an integer

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/17/count.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Example Question #2

__Let's write a function that takes a string and puts a space after every character. &rarr;__

* use assert on at least two cases to test (a good one might be empty string)
* it should take two one argument: a string
* it should return a string
* write at least one assertion

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/17/space.py %}
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Example Question #3

Create a function that returns the first word in a sentence.

* assume that spaces separate words
* it should take one argument, a string
* it should return a string
* if the original string is only one word, return that word
* if the original string is empty, return an empty string
* if the original string is only white space, return an empty string
* __hint__: substring may be helpful
* __hint__: how do you find the end index of substring?
</section>

<section markdown="block">
### Example Question #3 Potential Solution

{% highlight python %}
# version 1:
{% include classes/17/get_first_word.py %}
{% endhighlight %}

</section>

<section markdown="block">
### Example Question #3 Potential Solution

{% highlight python %}
# version 2 with split:
def get_first_word(s):
	if len(s) == 0:
		return ""
	else:
		return s.split()[0]
{% endhighlight %}

</section>

<section markdown="block">
### Example Question #4 

__Write four test cases for get_first_word using: &rarr;__

* 0 words
* 1 word
* &gt; 1 words
* only spaces

<div class="incremental" markdown="block">

{% highlight python %}
assert "foo" == get_first_word("foo bar baz"), "returns first word in space separated string"
assert "" == get_first_word(""), "returns first word in space separated string"
# etc...
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Example Question #5

Create a function called _is_digit_ that determines whether or not a string only has numbers (0-9) in it.

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
### Example Question #5 Potential Solution

(General strategy is iterating over a sequence of characters, and changing a value outside of the loop based on characters)

{% highlight python %}
{% include classes/17/is_digit.py %}
{% endhighlight %}
</section>

<section markdown="block">
### Some More Potential Questions

* use upper or lower to check for permutations for input
	* for example, loop forever
	* ask the user if they want the loop to stop
	* accept "Yes", "YES", "yes", etc.
	* use upper or lower to normalize
* rewrite get_first_word, but use __find__() instead of a loop
* reverse a string
</section>

---
layout: slides
title: Strings as a Compound Data Type
---
<section markdown="block" class="title-slide">
# Strings as a Compound Data Type
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Strings as a Sequence of Characters

* we can treat a string as a sequence of characters
* each character can be referred to by its place in the string
* this place is a numeric value called an __index__
* an __index__ specifies the position of an item in an ordered collection (in the context of strings, a sequence of characters)
* __indexes start at 0__, not at 1
* consequently, the first character of a string is at index 0
* for example, in the string "hi", h is at index 0, i is at index 1
</section>

<section markdown="block">
### String Indexes

Let's take the string "cool cat!".  __What is the index of the first 'c'? What character is at index 1.  How about index 4? &rarr;__
{% highlight python %}
"""+---+---+---+---+---+---+---+---+---+
   | c | o | o | l |   | c | a | t | ! |
   +---+---+---+---+---+---+---+---+---+"""
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
"""+---+---+---+---+---+---+---+---+---+
   | c | o | o | l |   | c | a | t | ! |
   +---+---+---+---+---+---+---+---+---+
   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
   +---+---+---+---+---+---+---+---+---+"""
{% endhighlight %}
* the first 'c' is at index 0
* the first 'o' is at index 1
* space (' ') is at index 4
</div>
</section>

<section markdown="block">
### The Last Index
__What index is the last character of each of these strings? &rarr;__

1. "foo"
2. "hi"
3. "!"

<div class="incremental" markdown="block">

The last index is the length of the string - 1

1. 2
2. 1
3. 0
</div>
</section>

<section markdown="block">
### Some More Index Exercises
1. What's the index of '__h__' in "__hello__"?
2. What's the index of '__o__' in "__hello__"?
3. What's the index of the second '__l__' in "__hello__"?
4. What's the letter at index __0__ in "__hi there.__"?
5. What's the letter at index __2__ in "__hi there.__"?

<div class="incremental" markdown="block">

1. 'h' is index 0 in "hello"
2. 'o' is index 4 in "hello"
3. the second 'l' is index 3 in "hello"
4. 'h' is index 0 in "hi there."
5. ' ' (space) is index 2 in "hi there"

</div>
</section>

<section markdown="block">
### Indexing Into a String

You can reference a specific character in a string (__indexing__) by: 

* using the index (an integer)
* enclosed by square brackets 
* immediately following the string
* returns a __new string__ consisting of only that one character
* __note that the index or string can be variables or expressions!__

{% highlight python %}
a_string[an_index]
{% endhighlight %}

</section>

<section markdown="block">
### Indexing Examples

{% highlight python %}
>>> "hello"[0]
'h'
>>> animal = "aardvark"
>>> animal[4]
'v'
>>> idx = 7
>>> animal[idx]
'k'
>>> 
{% endhighlight %}
</section>

<section markdown="block">
### Indexing Exercises

__What does the following code output.  Let's walk through it line by line. &rarr;__

{% highlight python %}
idx = 3
animal = "moose"
print(animal[idx])
print(animal[idx - 3])
print("animal"[1])
print("animal"[5])
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
s
m
n
l
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Negative Indexes Also Work

-1 is the index of the last letter, -2, second to last, etc. ...__What does the following program output?  Let's go through it line by line. &rarr;__

{% highlight python %}
idx = -3
animal = "cow"
print(animal[-1])
print(animal[idx])
print(animal[idx + 3])
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
w
c
c
{% endhighlight %}
</div>
</section>

<section markdown="block">
### One Last Note About Indexing

* strings are __not__ _mutable_
	* you can read values by indexing into a string
	* however, you can't change values
	* consequently, you can't set an index equal to another character
* __let's see what happens when we try to change a character at an index using the assignment (=) operator &rarr;__

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> "hello"[0] = 'c'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>  
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Using Every Character in a String

What if we want to do something to each character in a string?  Manually and explicitly using indexes would be time consuming!  What if I wanted to:

* count the number of exclamation points I used in my slides!?
* recombine letters, but change vowels into numbers for a variant of "L33T SP34K"
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
my_crazy_string = "oh, my!"
for c in my_crazy_string:
  print(c)
{% endhighlight %}

* for loops allow us to iterate over every char in a string.  
* similar to looping over a sequence of #'s
* variable specified in loop represents the current char
* the loop continues until there are no letters left
* __what would the above code print out? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
o
h
,
m
y
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Write a Program That Iterates Over a String

__Try implementing this program:__

* use a for loop to go over every letter in "jetpack"
* for each letter, print out the letter with a suffix of "am" appended it

<div class="incremental" markdown="block">
{% highlight python %}
word = "jetpack"
suffix = "am"
for c in word:
	print(c + suffix)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Letter in Word

__Try implementing this function!__ (there's something that's built-in to Python that does this, and we'll see it later)

* implement a function called letter_in_word
* it should take two arguments, a letter and a word
* it should return True if the letter is in the word, otherwise, return False
* use assert on a True case and on a False case

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/16/letter_in_word.py %}
{% endhighlight %}
</div>
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
 
* m is the start index and n is the end index.
* the resulting substring starts at m, and goes up to, __but does not include__ n
</section>

<section markdown="block">
### Substring Exercises 

Write the slice to pick out the following substring from the original string:

{% highlight python %}
sentence = "hi bob!"
#           0123456
{% endhighlight %}

1. hi
2. bob!
3. bob

<div class="incremental" markdown="block">
{% highlight python %}
sentence[0:2]
sentence[3:7]
sentence[3:6]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Some Slicing Tricks

* leaving out the first index (before the colon - m) starts at the beginning of the string
* leaving out the second index (after the colon - n), ends at the end  of the string 
* if the second index, if n is bigger than the length of the string, up to the end is sliced

{% highlight python %}
"eggs and ham"[:4] #eggs
"eggs and ham"[9:] #ham
"eggs and ham"[9:100] #ham
{% endhighlight %}
</section>

<section markdown="block">
###  An Easier Way to Tell if a Letter is in a Word
__in__ and __not in__ or operators that each take two arguments.  They will test the membership of an element in a collection/sequence.  

* in the case of strings, that's character in word
* __in__
	* returns True if element on left is in element in right
	* False otherwise
* __not in__
	* returns True if element on left is __not__ in element in right
	* False otherwise
</section>

<section markdown="block">
###  In / Not In Examples

{% highlight pycon %}
>>> 'c' in "cat"
True
>>> 'c' not in "cat"
False
{% endhighlight %}
</section>

<section markdown="block">
### Some Potential Exercises 

* is_digit
	* accepts a string
	* returns True if every character in a string is numeric (0 through 9)
	* hint: use in and or not in... and the string "0123456789"
* remove_vowels
	* accepts a string
	* returns a string without any vowels in it
	* hint: build a string by accumulating characters
</section>


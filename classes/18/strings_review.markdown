---
layout: slides
title: Strings Review 
---
<section markdown="block" class="title-slide">
# Strings - Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Indexing

__What is the output of the following code? &rarr;__

{% highlight python %}
""" +---+---+---+---+
    | w | h | o | ? |
    +---+---+---+---+ """
question = "who?"
idx = 4
print(question[0])
print(question[-1])
print(question[-2])
print(question[idx])
print(question[idx - 1])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
print(question[0]) # --> w
{% endhighlight %}
{% highlight python %}
print(question[-1]) # --> ?
{% endhighlight %}
{% highlight python %}
print(question[-2]) # --> o
{% endhighlight %}
{% highlight python %}
print(question[4]) # --> error
{% endhighlight %}
{% highlight python %}
print(question[3]) # --> q
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Summary for Indexing

* an __index__ is the numeric position of an element within a collection of elements
* the __first character__ in a string is at __index 0__
* the __last character__ is at index __length - 1__ (len(s) - 1) 
* also, the __last element__ is at index __-1__
* the __second to last element__ is at index __-2__
* if the index doesn't exist, you will get an __IndexError__
* you can __index into__ (retrieve a character) from a string using brackets - __[]__'s.
</section>

<section markdown="block">
### Mutability

__What is the output of the following code? &rarr;__

{% highlight pycon %}
word = "mile"
word[1] = 'o'
{% endhighlight %}

<div class="incremental" markdown="block">
* strings are __not mutable__; they cannot be changed
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
## Strings are Immutable
</section>


<section markdown="block">
### Looping Over Each Character

__Write a function that takes a string and returns a new string with all of the spaces taken out.__ &rarr;

* __start with an empty string__ and build it out
* __use a for loop__ 
* __conditionally add__ characters based on whether or not the character is a space
* write at least __one assertion__ for this function


{% highlight python %}
s = remove_all_spaces("I want to go to there")
print(s)
# should give back: 
# Iwanttogotothere
{% endhighlight %}
</section>

<section markdown="block">
### Looping Over Each Character Continued

{% highlight python %}
def remove_space(s):
	result = ""
	for character in s:
		if character != " ":
			result += character
	return result

assert "Iwanttogotothere" == remove_space("I want to go to there"), "test removal of spaces"
{% endhighlight %}
</section>

<section markdown="block">
## You can go over every character in a string with a for loop!
</section>

<div class="incremental" markdown="block">
</div>

<section markdown="block">
### Looping Over Strings Summary / Syntax

* __for loops allow us to iterate over every character in a string__  
* it's similar to looping over a sequence of #'s
* the variable in the loop head represents the current character
* the loop continues until there are no letters left

</section>

<section markdown="block">
### Slicing

Write the slice to pick out the following substring from the original string:

{% highlight python %}
s = "chew"
#    0123
{% endhighlight %}

1. hew (2 ways)
2. che (2 ways)
3. chew (2 ways)

<div class="incremental" markdown="block">
{% highlight python %}
s[1:3]
s[1:]
{% endhighlight %}
{% highlight python %}
s[0:3]
s[:3]
{% endhighlight %}
{% highlight python %}
s[1:5]
s[:]
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Slicing Syntax


{% highlight pycon %}
some_long_string[m:n]
{% endhighlight %}
 
* __m__ is the start index and __n__ is the end index.
* the resulting substring starts at __m__, and goes up to, but does __not__ include __n__
</section>


<section markdown="block">
### Slicing Shortcuts

* leaving out the first index (before the colon - m) starts at the beginning of the string
* leaving out the second index (after the colon - n), ends at the end of the string 
* leaving out both gives back the whole string
* if the second index, n is greater than the length of the string, up to the end is sliced

{% highlight python %}
"jam"[:2] #ja
"jam"[1:] #am
"jam"[1:100] #am
"jam"[:] #jam
"jam"[9:100] #ham
{% endhighlight %}
</section>

<section markdown="block">
### In and Not In 

__What is the output of the following code?__ &rarr;

{% highlight python %}
word = "ice cream"
letter = "a"
print(letter in word)
print("cat" in "vacation")
print("cat" in "work")
print("cat" not in "work")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
print(letter in word)      # True
print("cat" in "vacation") # True
print("cat" in "work")     # False
print("cat" not in "work") # Tru
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  In / Not In 

Use the __in__ operator!

* __in__ tests for membership
* it takes two operands, one on each side
* if the operand on the left is in the operand on the right, __in__ returns True
* in the case of strings, __in__ tests if one string is a substring of the other 
* evaluation results in __a boolean__!
* __not in__ is the logical opposite of the __in__ operator

</section>


<section markdown="block">
###  In / Not In Notes

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

</section>


<section markdown="block">
### Functions vs Methods

__What's the difference between a function and a method?__ &rarr;

<div class="incremental" markdown="block">
* a __function__ is a named sequence of statements that can be called to perform some useful action
* a __method__ is a function called in the context of an object (it's an action that the object can perform)
* ...so, the difference is, a method must be called with an object
</div>
</section>

<section markdown="block">
### String Methods

__Name as many string methods as you can...__ &rarr;

* give the method's name
* what the method does
* parameters (if any)
* return value (if any)

</section>

<section markdown="block">
### String Methods

1. __upper__() 
2. __lower__()
3. __isdigit__()
4. __isalpha__()
5. __find__(sub[, start[, end]])
6. __format__(...)
7. __strip__([chars])
8. __isupper__()
9. __islower__()
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

{% highlight python %}
print("hello".find("h"))
print("hello".find("x"))
print("hello".find("lo"))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
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

Format is like the string formatting operator, but possibly easier?! 

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

{% highlight python %}
twenty elephants
20 elephants
20 elephants
100 elephants
20 elephants and 100 peanuts
{% endhighlight %}
</section>

<section markdown="block">
### isupper() and islower()

__isupper__() and __islower__() return True if the string that is called on is the case specified.  __What does the following output?__ &rarr;

{% highlight python %}
print("this should be uppercase".isupper())
print("THIS SHOULD BE LOWERCASE".isupper())
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
False
True
{% endhighlight %}
</div>
</section>

<section markdown="block">
### More About Mutability...

String methods can't change the string object that they're called on.  __For example... what does the following print out?__ &rarr;

{% highlight python %}
s = "beep"
new_s = s.upper()
print(s)
print(new_s)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
beep
BEEP
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Strings are Immutable!

__String methods can't change the string object that they're called on.  Instead, they usually just give back a new string.__
</section>

<section markdown="block">
### String Functions

__Name as many built-in string functions as you can.  What do they do, what are their parameters, and what do they return?__ &rarr;

<div class="incremental" markdown="block">
* __len__(s) - the length of a string (gives back an int)
* __ord__(s) - the _code point_ of the character supplied (gives back an int)
* __chr__(i) - the character represented by the supplied _code point_ (gives back a string)
</div>
</section>



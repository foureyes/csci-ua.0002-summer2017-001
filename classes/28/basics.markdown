---
layout: slides
title: Variables, Statements, Expressions, Types, Operators 
---
<section markdown="block" class="title-slide">
# Variables, Statements, Expressions, Types, Operators
{% include title-slide-footer.html %}
</section>


<section markdown="block">
## Values and Types
</section>

<section markdown="block">
### What are Values?
* __values__ are just data
	* it can be stored in a variable 
	* it can be computed in an expression
	* it can't be _evaluated_ further (2 + 3 is not a value, because it can be evaluated further)
* some examples of values:
	* -123456
	* "a string is a value"
	* 1.00000001 
	* True, False
</section>

<section markdown="block">
### Literals

The representation of a bare value in code is sometimes called a __literal__.

* "a string " a __string literal__
* 254 - an __integer literal__
* False - a __bool literal__
</section>

<section markdown="block">
### Values can be Classified by Data Type
A __data type__ is a set of values.  The type of a value determines how it can be used in expressions.  Sometimes __data type__ is also referred to as just __type__... or __class__.  

1. __str__ (string) - "yup, a string"
2. __bool__ (boolean value) - True
3. __int__ (integer) - 12
4. __float__ (floating point) - 12.121212
5. __complex__ (complex numbers) - 1j * 1j (just know that this is a type; these won't be in the exam)

The last 3 are  __numeric types__.
</section>

<section markdown="block">
## Strings, Integers and Floating Point Numbers
</section>

<section markdown="block">
### Strings
* a __string__ is a sequence of characters (any characters).
* including spaces and punctuation
	* and by spaces, I mean spaces, tabs, newlines, etc
	* for example " " is a string!
	* so is "" (this, however, is an _empty_ string)
* are __delimited__ by quotation marks - must __start and end__ with quotes!
* (btw, a __delimiter__ is just a character or characters that marks a boundary... or distinguishes a value from other values)
* for example "foo", 'bar', and """baz""" are all strings
</section>


<section markdown="block">
### Unbalanced Quotes
__What happens if you have an extra quote or a missing quote. &rarr;__ 

<div class="incremental" markdown="block">
{% highlight pycon %}
>>> "oops " I quoted again"
SyntaxError: invalid syntax
{% endhighlight %}

* if you don't have matching start and end quotes (__unbalanced quotes__)
* if you forget to close your quotes (you have a start quote, but no end)
* ... you'll also get a syntax error
</div>
</section>

<section markdown="block">
### There Are Three Ways to Quote Strings

__What are the three ways to quote strings?__

<div class="incremental" markdown="block">
1. double quotes - "
2. single quotes - '
3. triple double quotes __for multiline strings__ - """

{% highlight python %}
"double quoted string"
'single quoted string'
"""more than
one line.  omg!"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### When Would You Use One Over the Other?

* single or double quotes allow you to put in single or double quotes into a string without needing to __escape__ them
	* "I'm"
	* 'use a " to delimit a string'
* triple double quotes allow you to span multiple lines (you can't span multiple lines with single or double quotes)
</section>

<section markdown="block">
### Constructing Strings / String Operators

There are two ways to put strings together.  They correspond to two string operators.

1. String __concatenation__ - adding two strings together using the __+__ symbol
2. String __interpolation__ - constructing a string by using placeholders and substituting values in for those placeholders... uses the __%__ symbol as the operator, but __%s__ as the placeholder

__both operators return strings__
</section>


<section markdown="block">
### String Operators at a Glance

These are the string operators that we learned (note - they all return strings, but the types of arguments may vary depending on operator).  __What were they again? &rarr;__

<div class="incremental" markdown="block">
1. __+__ - concatenation - takes two strings (error otherwise) &rarr; returns a string
2. __%__ - interpolation - takes a string with placeholders on the right, and values, variables or expressions (separated by commas) in parentheses on the left &rarr; returns a string
3. __*__ - multiplication - takes a string and int (error otherwise, even if it's another numeric type), repeats the string that number of times &rarr; returns a string
</div>
</section>

<section markdown="block">
### Newlines and Escaping Characters 
If we need a character that has special meaning in a string, such as a single or double quote...

* we can use the backslash character before the special character
* for quotes, we can use mixed quotes (embed single quotes in a double quoted string)!
* we can also create newlines using __\n__

{% highlight python %}
print("escaping using \"backslash\"")
print("single  quotes ''''") 
print("""some "double quotes"""")
{% endhighlight %}

</section>



<section markdown="block">
### ints and floats

Integers and floating point numbers are both numeric types.

* ints and floats are just numbers 
* (no quotes needed... though a decimal point will automatically make a value into a float)
*  __however - Don't use commas!  They don't mean what you expect.__ &rarr;
* sometimes ints and floats can be expressed with scientific notation (though we won't cover this in the exam)
</section>

<section markdown="block">
### Integers

__int__ - integers

* whole number - negative or positive
* examples: 1751, -95
* "unlimited" (arbitrarily high)
</section>

<section markdown="block">
### Floating Point Numbers

__float__  - floating point numbers

* real number - contains decimal point
* 10.00, 491.545532111
* may overflow
* small and large numbers expressed in scientific notation (though we won't cover this in the exam)
</section>

<section markdown="block">
### Operators
* addition, multiplication and subtraction: __+__, __\*__, and __-__
* division: __/__ (results in a float even if two integers - ex 10 / 2 &rarr; 5.0)
* integer division: __//__ (next integer to the left - ex -23 // 3 &rarr; -8)
* modulo: __%__ (ex 10 % 7 &rarr; 3)
* exponentiation: __**__ (ex 2 ** 3 &rarr; 8)
</section>

<section markdown="block">
### Numeric Operator Precedence

__What order are these numeric operators evaluated in? &rarr;__

<div class="incremental" markdown="block">
* as you would expect - follows PEMDAS 
* (parentheses, exponentiation, multiplication, division, addition, subtraciton)
* __what would (5 + 15) * 2 ** 2 + 20 result in? &rarr;__

{% highlight pycon %}
>>> (5 + 15) * 2 ** 2 + 20
100
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Numeric Operators and Type Compatibility

* most of these numeric operators will only work with numeric types (float, int)
* if you try to add, subtract, divide with an numeric type and a string, you will get an error
* always use __int()__ or __float()__ to convert your string to a numeric type if you're going to do calculations 
</section>

<section markdown="block">
### Results of the Following Operations

__What are the resulting values and types after evaluating the following expressions? &rarr;__

* 28 / 7
* 28 // 10
* 28 % 10
* 28 / "7"

<div class="incremental" markdown="block">
* 4.0 - float
* 2 - int
* 8 - int
* Error
</div>
</section>

<section markdown="block">
### Implementing a Formula

An obvious use case for these numeric operations is implementing a formula.  

For example: __find the hypotenuse of a right triangle using this formula... h = &radic;(x&sup2; + y&sup2;), where x is 8 and y is 6 &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
import math
x, y = 8, 6
# you can also use (some value) ** 0.5
h = math.sqrt(x ** 2 + y ** 2)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### A Shortcut

We've used this in class... there's a shortcut to add a value to an existing variable (the same exists for subtraction as well).  __-=__ and __+=__ are shortcuts for decrementing or incrementing a variable...

{% highlight python %}
a = 0

# increment a by one... just set the variable, a, equal to a + 1
a = a + 1

# or... alternatively, use a shortcut +=:
a += 1

# you can add any value, not just 1
a += 20
{% endhighlight %}
</section>


<section markdown="block">
### The bool Type
Python has a __bool__ type to represent Boolean values

* True or False
* note the uppercase 'T' and 'F'
* just like other values, can be assigned to variables
* bools can be combined into expressions using __logical operators__
* we'll review those later...
</section>

<section markdown="block">
###A Guessing Game
<aside>What type is it?</aside>

1. __1__
2. __1.0__
3. __"1"__
4. __"""1.0"""__
5. __1.111__
6. __'1,111'__
7. True
8. __1 + 5__
9. __"%s my friends!!!" % ("hello")__

</section>

<section markdown="block">
###A Guessing Game (Answers)
<aside>What type is it?</aside>

1. __1__ - int
2. __1.0__ - float
3. __"1"__ - str
4. __"""1.0"""__ - str
5. __1.111__ - float
6. __'1,111'__ - str
7. True - bool
8. __1 + 5__ - int
9. __"%s my friends!!!" % ("hello")__ - str

</section>

<section markdown="block">
### Conversion Functions

For each type that we learned, there's a function with the same name that will convert a value into that type.  They __always__ return their associated type!

* __int()__
* __str()__
* __float()__
* __bool()__

</section>

<section markdown="block">
### Conversion Functions Continued

* note that __int()__ and __float()__ will only accept int and float _"like"_ values... "5" will be converted (even with spaces), but "five" will cause an error
* these can be used to avoid errors when using numeric or string operators 
{% highlight python %}
num = 99
print(str(num) + " red balloons")
{% endhighlight %}
* remember - you don't have to convert if your value is already the type you're converting to
{% highlight python %}
num = "99" # no need to convert
print(num + " red balloons")
{% endhighlight %}

</section>

<section markdown="block">
### Other Built-In Functions
* __print__ - outputs value to screen; returns nothing
* __input__ - prompts user for input; returns a str
* __type__ - returns the type of the value passed in; returns a type object
* __round__ - rounds a number; returns an int (when called with one argument) ...(we used this in a homework)
* obv, all of the conversion functions
</section>

<section markdown="block">
### A Word About input

* it takes one argument... which is what gets displayed to the user
* the program will wait until the user provides input
* input returns a string that represents the user's input
* even if the input looks numeric (say 234)
* __it still returns a string__ (in the previous case "234")
</section>

<section markdown="block">
### Variables

* __variable__ - name that refers to a value
* this terminology is important; very specific... __name__ and __value__
* we can now use that name instead of the explicit value
* the equals sign, __=__ is the __assignment token__ or __assignment operator__ that we use to bind a name to a value
	* name on left
	* value on right

{% highlight python %}
some_variable_name = "a value"
{% endhighlight %}

</section>

<section markdown="block">
### Assignment vs Equality

__Don't confuse the assignment operator with the equality operator!__

{% highlight pycon %}
# one equal sign is assignment
a = 1  

# two equal signs mean test for equality
a == 1
{% endhighlight %}
</section>

<section markdown="block">
### Reassignment / Rebinding

* you can reassign or rebind
* __let's see that in action__ &rarr;

{% highlight pycon %}
>>> a = 23
>>> a
23
>>> a = "foo"
{% endhighlight %}
</section>

<section markdown="block">
### While We're on the Subject... Multiple Assignment

You can assign multiple variables in one line. (Yes... tuples)

{% highlight pycon %}
>>> a, b = 50, 60
>>> a
50
>>> b
60
{% endhighlight %}
</section>


<section markdown="block">
### Naming Variables
* names can only be alphanumeric (numbers and letters) or the underscore
* the first character has to be a letter
* __case sensitive__ - case matters
* the name can't be a keyword or reserved word
</section>

<section markdown="block">
### Am I a Valid Name?

__Are these valid variable names? &rarr;__

* _foo
* 1_foo
* foo
* 1foo
* $foo
* foo$
</section>

<section markdown="block">
### Am I a Valid Name (Answers)?

__Are these valid variable names? &rarr;__

* _foo - yes
* 1_foo - no
* foo - yes
* 1foo - no
* $foo - no
* foo$ - no
</section>



<section markdown="block">
### Some Exercises
* input that affects range
	* ask for number
	* say hello that many times
* revisit fizz buzz
* sentinel - keep on going until input 
* 21 / Blackjack 
	* type 'hit' to get random value between 1 and 11
	* bust if you're over 21
* 21 / Blackjack automated
	* continually sum random values between 1 and 11
	* stop after sum goes over 21
	* add an if to stop at a certain value lesser than 21
</section>

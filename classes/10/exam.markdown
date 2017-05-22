---
layout: slides
title: About the Exam 
---
<section markdown="block" class="title-slide">
# About the Exam
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Some Logistics

* if you miss it, you get a 0
* the best indication of the types of questions you'll see is the list of sample exam questions
* expect the exam to to be similar to the _easier_ homework (questions.py and some of the basic programming problems...) and handouts
* expect about 15 questions (give or take a couple) total
* you'll have the entire class period for the exam
</section>

<section markdown="block">
## Types of Questions
</section>

<section markdown="block">
### Short Answer

* What's a while loop?
* Name some built-in functions and what they do?
</section>

<section markdown="block">
### Guided Programming Questions 

Instructions step you through each statement, you write it...

* create a variable named noun, set it equal to "aardvark"
* create a variable named adjective, set it equal to "agitated"
* use string interpolation to put the two together in a sentence "the agitated aardvark acted awkwardly"
</section>

<section markdown="block">
### Answer Questions About a Small Sample of Code 

(We've seen this before in our quiz.) Some examples:

What's the output... or is there an error?
{% highlight python %}
s = "foo" +  int("5")
print(s * 2)
{% endhighlight %}

What type is a?

{% highlight python %}
a = input("enter a number")
print(a)
{% endhighlight %}

</section>

<section markdown="block">
### Questions About Sample Code Continued

What will make the loop run/not run

{% highlight python %}
response = input()
while response == 'go':
	print("going")
{% endhighlight %}

__Is there an error? How do you fix the error?&rarr;__
{% highlight python %}
s = "10"
n = 20 + s
print(n)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
n = 20 + int(s)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Questions About Sample Code Continued Some More

__What's the output of...&rarr;__

{% highlight python %}
for i in range(50, 59, 2)
	if i == 56:
		print("foo")
	else:
		print("bar")
	print("baz " + str(i))
{% endhighlight %}
</section>

<section markdown="block">
### Fill in the Blanks

Use a while loop to count backwards from 10 to 0 by 2's
{% highlight python %}
count = 
while               :
   print(         )    
   #what else goes here?
{% endhighlight %}
</section>

<section markdown="block">
### Obviously, Write Some Code

Expect to write...

* if / elif / else
* while and for loops (including counting, summing and sentinel variables)
* modules
* strings, ints, floats, bools and associated operations
* all of that nested within each other (if statements in while loops, for example)
* user input, for example: __keep adding numbers that a user inputs, until the user enters quit__ 
</section>

<section markdown="block">
### There Are _X_ Errors in This Code

Read over a few lines of code; find and fix the syntax and logical errors.

{% highlight python %}
# We're just counting from 1 through 10
for num in range(10)
	print("we're just counting " + i)
{% endhighlight %}
</section>

<section markdown="block">
### Evaluate Boolean Expressions / Truth Tables

* __truth tables__ for more complex expressions, such as __p or q or r__
* True and False or not False
* 10 % 5 == 1 or 1 != "hello"
* etc.
</section>

<section markdown="block">
## Exam Topics
</section>

<section markdown="block">
### Materials Covered

* the exam content __is from__:
	* the __slides__ 
	* the __modules__ 
	* the __homework__ 
	* ... the corresponding __readings__ from {{ site.bookq }}
* if it was not covered in class, homework, or the modules/quizzes, it will not be in the exam
</section>

<section markdown="block">
### Topics from Slides

* all topics in the slides from classes __1__ through __10__
* check out the __definitions__ in the slides (they're usually __bolded__)
* check out the __sample problems__ in the slides
* the built-in functions that were in the homework (and that appeared in slides that we did not go over) __may be in the exam__
* the following topics from the slides (and modules) __will not__ be in the exam:
    * turtle (was only in the online modules)
    * demorgan's laws
	* nested loops (we never had a chance to cover this)
</section>

<section markdown="block">
## Topics from Modules

Review the online modules that we've gone over:

* everything up through for loops
* again, no nested loops
* no turtle
</section>

<section markdown="block">
### Topics from the Book

__The exam will cover material from Chapters 1 through 4 in the book.__

* Ch. 1 - Introduction to Computers and Programming - all sections
* Ch. 2 - Input, Processing, and Output 
	* __except__ 70 through 72 on formatting output
</section>

<section markdown="block">

### Topics from the Book Continued

* Ch. 3 - Decision Structures and Boolean Logic - all sections
* Ch. 4 - Repetition Structures 
	* __except__ 4.7 on nested loops
</section>

<section markdown="block">
## Test-Taking Strategies
</section>

<section markdown="block">
### General Strategies

* don't get bogged down on a single problem, jot down a potential answer and __go back to it later__
* __partial credit is given__; don't leave a question blank, even if it's just notes or half an attempt
* __double check your work__
</section>

<section markdown="block">
### Sample Code

* go through the code line by line
* write down the values you suspect will be in the variables
* if there's something that requires user input, try going through the code with sample input
</section>

<section markdown="block">
### Code from Scratch

* plan out what your going to do first
* ask yourself questions, like - will there be data stored, are there repeated actions, etc.
* if there is example output, run through your finished code with the sample data to make sure it works
</section>

<section markdown="block">
## Any Questions About Material or Exam Format?

<aside>If not, let's figure out how we want to review...</aside>
</section>

<section markdown="block">
###  Review

We have a few options.  __Which one do you want to do first?__

* suggest topics?
* alternate working on sample exam questions and going over answers
* go over review slides
	* variables, expressions, statements
	* operators and types (int, bool, etc)
	* boolean logic
	* conditionals / if statements
	* loops / while and for
	* functions
</section>

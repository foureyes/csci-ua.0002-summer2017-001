---
layout: slides
title: About Class #21 
---
<section markdown="block" class="title-slide">
# About Class #21
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Midterm #2

* it's on Wednesday, 11/18
</section>

<section markdown="block">
### Topics

For the review... we can go over (your choice):

* list / _in class_ exercises?
* _difficult_ topics
	* consecutive application of list methods
	* nested lists / loops
	* scope 
	* mutability
	* function arguments
* homework solutions
* specific requests for topics
* review slides
	* I'm open to reviewing topics in any order
	* will default to chronological to re-familiarize with older material
</section>

<section markdown="block">
### Major Topics Covered in Midterm #2

Topics in the Exam

1. Nested Loops
2. Creating Functions 
	* (including testing functions with assertions)
3. Strings
4. Lists

Potentially Extra Credit

1. Turtle (Objects and Methods)
2. Recursion
</section>

<!--
<section markdown="block">
### Homework #6, #7



* [nerd_talk.py](../../resources/code/hw7/nerd_talk.py)
	* lots of creative solutions, solution above uses conditionals and string concatenation
	* here's one [wrong way with the replace method](http://www.pythontutor.com/visualize.html#code=def+convert(words)%3A%0A+++++%23+partial+implementation%0A+++++words.replace('A',+'4')%0A+++++words.replace('a',+'4')%0A++%0A++++++++++++++++++++++++++++++++++++++++++++++++++++++++++%0Aprint(convert('hay'))&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0), and one [right way with the replace method](http://www.pythontutor.com/visualize.html#code=def+convert(words)%3A%0A+++++%23+partial+implementation%0A+++++words+%3D+words.replace('A',+'4')%0A+++++words+%3D+words.replace('a',+'4')%0A+++++return+words%0A++%0A++++++++++++++++++++++++++++++++++++++++++++++++++++++++++%0Aprint(convert('hay'))&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)
	* here's an [interesting one...](http://www.pythontutor.com/visualize.html#code=def+convert(words)%3A%0A+++++a+%3D+''%0A+++++for+num+in+range(0,len(words))%3A%0A++++++++++if+words%5Bnum%5D+%3D%3D+'a'+or+words%5Bnum%5D+%3D%3D+'A'%3A%0A+++++++++++++++a+%2B%3D+str(4)%0A++++++++++elif+words%5Bnum%5D+%3D%3D+'e'+or+words%5Bnum%5D+%3D%3D+'E'%3A%0A+++++++++++++++a+%2B%3D+str(3)%0A++++++++++elif+words%5Bnum%5D+%3D%3D+'i'+or+words%5Bnum%5D+%3D%3D+'I'%3A%0A+++++++++++++++a+%2B%3D+str(1)%0A++++++++++elif+words%5Bnum%5D+%3D%3D+'o'+or+words%5Bnum%5D+%3D%3D+'O'%3A%0A+++++++++++++++a+%2B%3D+str(0)%0A++++++++++else%3A%0A+++++++++++++++a+%2B%3D+words%5Bnum%5D%0A+++++return+a%0A++++++++++++++++++++++++++++++++%0A++++++++++++++++++++++++++++++++%0Aprint(convert('aeioAEIO'))&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)
</section>

<section markdown="block">
### Homework #6 
* [prime.py](../../resources/code/hw7/prime.py)
	* [a common error with prime.py](http://www.pythontutor.com/visualize.html#code=def+is_prime(n)%3A%0A++++for+i+in+range(2,+n)%3A%0A++++++++if+n+%25+i+%3D%3D+0%3A%0A++++++++++++return+False%0A++++++++else%3A%0A++++++++++++return+True%0A%0Aprint('Is+9+prime%3F+'+%2B+str(is_prime(9)))&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)
	* placement of break or return
	* btw, can we make this algorithm slightly more efficient?
* [recursive_power.py](../../resources/code/hw7/recursive_power.py)
	* what's the base case?
	* how do we define power in terms of itself?
	* [step_by_step](http://www.pythontutor.com/visualize.html#code=def+recursive_power(n,+p)%3A%0A++++if+p+%3D%3D+0%3A%0A++++++++return+1%0A++++else%3A%0A++++++++return+n+*+recursive_power(n,+p+-+1)%0A%0Aassert+1+%3D%3D+recursive_power(2,+0),+'base+case,+power+of+0+is+1'%0Aassert+81+%3D%3D+recursive_power(3,+4),+'returns+n+raised+to+power+p'&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)
</section>
-->


<section markdown="block">
### Course Materials for Review

* __modules__ #5 through #8 (nested loops through lists)
* __slides__
	* slides from classes __#12__ through class __#20__
	* should be comfortable with topics prior to #12 (loops, conditionals...)
* __homework__ __#5__ through __#8__ (again, turtle is extra credit)
* __practice questions__ - posted
</section>

<section markdown="block">
### Readings 

{{ site.bookq }}

* Chapter 4 - Loops
	* Section 4.7 on Nested Loops
* Chapter 5 - Functions
* Chapter 7 - Lists
* Chapter 8 - More About Strings 
* Chapter 12 - Recursion (Extra Credit)


</section>

<section markdown="block">
### Additional Readings from _How to Think Like a Computer Scientist_
 
* [Chapter 3 Hello, little turtles!](http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html) (Extra Credit)
* [Chapter 4 Functions](http://openbookproject.net/thinkcs/python/english3e/functions.html)
* [Chapter 6 Fruitful functions](http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html)
* [Chapter 8 Strings](http://openbookproject.net/thinkcs/python/english3e/strings.html)
* [Chapter 11 Lists](http://openbookproject.net/thinkcs/python/english3e/lists.html)
* (be familiar with loops - [Chapter 7](http://openbookproject.net/thinkcs/python/english3e/iteration.html))
</section>


<section markdown="block">
### Kinds of Questions

* 3 or 5 code from scratch 
	* mostly derived from concepts in homework or slides
	* for example, _accumulating_ characters or _reducing_ a list to a single value (average, max/min, etc.)
* complete the missing parts of this code
* find what's wrong with this code and correct it
* short answer questions (name two string methods and their parameters)
* what will this code output?
* what is the value of this variable at (after x iterations, after calling methods, etc.)...
* what will this function return (what value, what type)...
</section>

<section markdown="block">
### Additional Review Session

<aside>And if you haven't had enough, yet...</aside>

In addition to the in class review... I will be running another session:

* Tuesday, __11/17__
* 7:05pm to 8:00pm, WWH 517
</section>

<section markdown="block">
### About Your Midterm #2 Score


* if you score 10% points more than your midterm 1...
* I will count your 2nd midterm twice
* (and drop the score from your first midterm)
* (or a small extra credit assignment if you did not qualify for the previous)

</section>

---
layout: slides
title: Meta 
---
<section markdown="block" class="title-slide">
#  About Class #9
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Topics

* for loops
* while vs for
* all exercises, _all the time_
</section>

<section markdown="block">
###  Homework

* Grades for homework 1 and 2 already posted
* Grades for homework 3 posted this evening

Homework #4 is due on Wednesday!
</section>


{% comment %}
<section markdown="block">
##  Speaking of Homework #2 ...

<aside>Let's check out a few solutions.</aside>

</section>


<section markdown="block">
###  days.py

{% highlight python %}
"""
Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to 
Saturday. Write a program that asks the user for a number.  The program 
will print out the corresponding day.

1. Create a file called days.py
2. Ask the user for a number
3. Print out the appropriate day
4. You can get away with only using if-statements and the equality operator.
5. Don't worry about input outside of the range of numbers from 0 up-to
 and including 6.

Example Output - Everything after the greater than sign (>) is user input:

Please enter the number of your day
> 4
4 is... 
Thursday
"""
{% endhighlight %}
</section>

<section markdown="block">
###  days.py solution

{% highlight python %}
n = int(input("Please enter the number of your day\n> "))
print("%s is... " % n)
if n == 0:
	print("Sunday")
if n == 1:
	print("Monday")
if n == 2:
	print("Tuesday")
if n == 3:
	print("Wednesday")
if n == 4:
	print("Thursday")
if n == 5:
	print("Friday")
if n == 6:
	print("Saturday")

{% endhighlight %}
</section>

<section markdown="block">
###  days.py notes

* easier to call int once at the beginning than multiple times during each compare
* this could have been done with elif
* someone even used nested ifs (!?)
</section>

<section markdown="block">
###  numbers.py

{% highlight python %}
"""
Write a program that outputs the number in the thousands, hundreds, 
tens and ones places of a number. 

1. Create a file called numbers.py
2. Ask the user for a number
3. Calculate the numbers in the thousands, hundreds, tens and ones places
4. Output each place
5. One solution is to use some numeric operators to determine each 
place (maybe % and // may help)
6. You may have to calculate each place separately
7. Don't worry about input that's not a positive whole # below 10,000

Example Output - Everything after the greater than sign (>) is user input:

Please enter a number
> 256

0 thousands
2 hundreds
5 tens
6 ones
"""
{% endhighlight %}
</section>

<section markdown="block">
###  numbers.py solution

{% highlight python %}
while True:
    n = int(input("Please enter a number\n> "))
    ones = n % 10
    tens = n % 100 // 10
    hundreds = n % 1000 // 100
    thousands = n % 10000 // 1000
    print("""
    %s thousands
    %s hundreds
    %s tens
    %s ones
    """ % (thousands, hundreds, tens, ones))
{% endhighlight %}

</section>

<section markdown="block">
###  numbers.py notes

* this was a bit _difficult_
* common strategy was to use a combination of modulo and integer division
* modulo would shave off the next place, while integer division rounds down
* some solutions used features that we haven't seen yet, like string slicing
</section>

<section markdown="block">
###  stadium.py

{% highlight python %}
"""
There are three seating categories at a stadium.  For a softball game,
Class A seats cost $15, Class B seats cost $12, and Class C seats cost 
$9.  Write a program that asks how many tickets for each class of seats 
were sold, and then displays the amount of income generated from tickets.

For this exercise:
* create a function called display_total_cost; it should take three 
  arguments: the number of class A, B, and C tickets sold
* the function should calculate the total cost of all of the tickets 
  and displays the value
* create a function called main; the main function will take no parameters
* the main function will ask for input and call the display_total_cost 
  function that you created
  
Example Output - Everything after the greater than sign (>) is user input:

How many Class A tickets ($15) were sold?
> 10
How many Class B tickets ($12) were sold?
> 10
How many Class C tickets ($9) were sold?
> 10
The total income is: $360!
"""
{% endhighlight %}
</section>

<section markdown="block">
###  stadium.py solution

{% highlight python %}
def display_total_cost(a, b, c):
	total_cost = a * 15 + b * 12 + c * 9
	print('The total income is: $' + str(total_cost) + "!")

def main():
	print("Hi.  Let's see how much money the softball game made!")
	print("==========\n")
	num_a = int(input('How many Class A tickets ($15) were sold?\n> '))
	num_b = int(input('How many Class B tickets ($12) were sold?\n> '))
	num_c = int(input('How many Class C tickets ($9) were sold?\n> '))
	display_total_cost(num_a, num_b, num_c)
	
main()
{% endhighlight %}
</section>

<section markdown="block">
###  stadium.py notes

* instructions for stadium asked for both a _main_ function and another function called _display_total_cost_
* the display_total_cost function takes three parameters!
* defining functions in functions is valid syntax, but generally, we won't be doing that in this class, as it has subtle effects on what variables can be accssed and when they can be accessed
</section>

{% endcomment %}


<section markdown="block">
###  Midterm #1

Coming up soon!

* The __first midterm__ is on, __February 28th!__
	* __THAT'S IN A WEEK!__
* We'll have a review instead of a workshop for our next class
</section>



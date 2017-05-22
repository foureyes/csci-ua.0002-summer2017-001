---
layout: slides
title: Exceptions Review 
---
<section markdown="block" class="title-slide">
# Exceptions Review 
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Exceptions!

__What are some types/names of exceptions that we've seen and what are examples of each?__ &rarr;

<div class="incremental" markdown="block">
* ValueError - type is correct, value is not: int("foo")
* TypeError - operator or function doesn't support type: 5 + "foo"
* IndexError  - index out of range: a = [1, 2] ... a[3452]
* ZeroDivisionError - divide by zero: 5/0
* NameError - name (variable, function, etc) doesn't exist / not yet declared
</div>
</section>

<section markdown="block">
### Exception Handling

__What construct do we use to handle exceptions.  What is its syntax?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
try:
  # do some stuff
except:
  # if there's an error, do stuff here
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Exception Handling Continued

__What if your code could generate two errors - and you want to deal with them differently?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
try:
  # do some stuff
except SomeError1:
  # if there's an error, do stuff here
except SomeError2:
  # if there's another error, do other stuff here
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Revisiting Pizza Party

A program that calculates how many slices each person gets at a pizza party. 

* ask for number of people
* respond according to input, even input that is not valid (such as zero or non numeric strings)

{% highlight python %}
people = input("how many people are eating pizza?\n>")
try:
    print("Each person can have %s slices" % (8/int(people)))
except ZeroDivisionError:
    print("More for me!")
except ValueError:
    print("That's not a number!")
{% endhighlight %}
</section>

<section markdown="block">
### An Additional Clause

An additional __else__ clause can be added to the end of try-except:

* statements within an __else__ clause are only executed if __no__ exceptions are raised
* if an exception occurs, the __else__ clause is skipped

{% highlight python %}
try:
	"""do something that could cause an error"""
except: 
	"""only executed if an error occurs"""
else: 
	"""only executed if NO error occurs"""
{% endhighlight %}
</section>

<section markdown="block">
### Try, Except, Else...

__What is the output of the following code?__ &rarr;

{% highlight python %}
n = 5
try:
	result = 20/n
except ZeroDivisionError: 
	print("can't divide by zero!")
else: 
	print(result)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
4.0
{% endhighlight %}
</div>
</section>

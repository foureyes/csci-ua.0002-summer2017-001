---
layout: slides
title: If Statements - Advanced 
---
<section markdown="block" class="title-slide">
# Truthiness
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Truthiness

See this [crazy chart](http://docs.python.org/py3k/library/stdtypes.html#truth-value-testing) on the _intrinsic_ boolean value of various types.  The following values are considered false:

* None
* False
* 0 of any numeric type (0.0, 0)
* empty mapping or sequence type (We'll look at these later) - this includes the empty string '', "", etc.
* some instances of user defined types based on __bool__ method
</section>

<section markdown="block">
### Truthiness Examples

{% highlight python %}
a = ""
if a:
	print("true!")

a = 0
if a:
	print("true!")

a = "foo"
if a:
	print("true!")
{% endhighlight %}

</section>

<section markdown="block">
### Another Note About Style
* remember idioms?
* [testing for truth values, python idioms](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#testing-for-truth-values)
* more elegant to test intrinsic truth values than using equality operator
{% highlight python %}
b = True
# instead of if b == True
if b:
	print("b")

s = "catz!"
# to test if the string exists
if s:
	print(s)

{% endhighlight %}
</section>

<section markdown="block">
## [And Finally... Loops](while.html)
</section>

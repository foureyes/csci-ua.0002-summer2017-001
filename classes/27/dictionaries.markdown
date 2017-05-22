---
layout: slides
title: Dictionaries 
---
<section markdown="block" class="title-slide">
# Dictionaries
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Dictionaries

__A dictionary maps values to names.  Is a dictionary mutable/immutable, ordered/unordered, compound/not compound?__

<div class="incremental" markdown="block">
* mutable
* ordered
* compound
</div>
</section>

<section markdown="block">
###  Dictionaries Syntax

__What's exact syntax for a dictionary?  What does an empty dictionary look like?__

<div class="incremental" markdown="block">
* a dictionary starts and ends with an opening and closing curly brace
* an empty dictionary is {}
* each key value pair in a dictionary is separated by a comma
* keys and values are linked together by a colon, the key before and the value after

{% highlight python %}
{'key1':'value1', 'key2':'value2'}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Retrieving Values at Keys 

__Name two ways to retrieve a value at a key from a dictionary.  How are they different?__

<div class="incremental" markdown="block">
{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}

# brackets and key
print(pizza["topping"])

# get method
print(pizza.get('topping'))

# using brackets and the key will give a KeyError if the key doesn't exist!
{% endhighlight %}
</div>
</section>


<section markdown="block">
### The get Method

__Describe what the get method does.  How many arguments does it take?  What does it return?  Does it change the original dictionary?__ &rarr;

<div class="incremental" markdown="block">
* 2 arguments:
	* the key of the element you want to retrieve
	* an optional default value in case that key doesn't exist yet (None if no second argument)
* returns default value if key doesn't exist, otherwise returns value at specified key
* the dictionary itself is not changed

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}
print(pizza.get('second topping', 'more cheese'))
# prints out more cheese
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Adding a New Key and Value

__How do you add a new key and value to a dictionary?__

<div class="incremental" markdown="block">
Use the key that doesn't exist... and assign a value...

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms"}
pizza['size'] = 'medium
print(pizza)
# shows that size:medium was added
# note that if size existed, its value would have been updated
{% endhighlight %}
</div>
</section>




<section markdown="block">
### Dictionaries and Iteration

__What are some ways of looping over a dictionary?  What will the loop variable represent?__ &rarr;

<div class="incremental" markdown="block">

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}
# keys only...
for k in pizza:
  print(k)

# using items and tuple unpacking
for k in pizza:
  print(k, pizza[k])

# using items and tuple unpacking
for k, v in pizza.items():
  print(k, v)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Deleting Keys/Values

__Name three ways to delete key/value pairs in a dictionary__ &rarr;

<div class="incremental" markdown="block">

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}
# del
del pizza['crust']

# pop method (removes key/value using key passed in, returns value)
result = pizza.pop('topping')
print(result)
print(pizza)

# popitem method (removes arbitrary key/value, returns two-element tuple)
result = pizza.popitem()
print(result)
print(pizza)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### BTW, in and len()

__The in and not in operators work with dictionary keys; len() gives back the number of key/value pairs__ &rarr;

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}
print(len(pizza))
# prints out 4

result = 'crust' in pizza
print(result)
# prints out True
{% endhighlight %}
</section>

<section markdown="block">
### Other Methods?

__Are there any other dictionary methods that learned?__ &rarr;

<div class="incremental" markdown="block">

{% highlight python %}
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}

# update adds or updates key values based on dictionary passed in
pizza.update({'price':18})
print(pizza)

# keys and values returns a list-like structure with only keys or only values
print(pizza.keys())
print(pizza.values())
{% endhighlight %}
</div>
</section>

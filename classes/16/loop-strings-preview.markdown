---
layout: slides
title: Looping Over Strings 
---
<section markdown="block" class="title-slide">
# Looping Over Strings
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Strings

__What's a string again?__ &rarr;

<div class="incremental" markdown="block">
* a __string__ is an ordered sequence of characters (any character, even punctuation and white space)
* it's an __iterable object__ (like a range), which means...
</div>

</section>

<section markdown="block">
### Strings and For Loops

Strings can _give back_ each character one-at-a-time when used in a for loop:

{% highlight python %}
word = "great!"
for character in word:
	print(word)
{% endhighlight %}

* note that the loop variable, character, represents the current character that _the loop is on_.
* similar to the current number in a range!
</section>

<section markdown="block">
## This will be useful for homework #7
</section>


<section markdown="block">
## [Functions Handout](handout.html)
</section>

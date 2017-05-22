---
layout: slides
title:  Addendum to List Methods 
---

<section markdown="block" class="title-slide">
# Addendum to List Methods
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Questions

1. can __remove__() remove the last occurrence?
2. can __pop__() take an argument?
3. is there a way to __pop__() the first element from a list?
</section>

<section markdown="block">
### Remove the Last Occurrence

Unfortunately, there's no way to do it with remove().

With the features and types that we know, how can we do this?

* iterate over the list in reverse order (we'll see this later)
* reverse the list and then use remove (but that changes the list ordering permanently)
</section>

<section markdown="block">
### Remove the Last Occurrence

__pop()__ can actually take an optional argument - the index that you want removed!  __What does this print out? &rarr;__

{% highlight python %}
a = [1, 2, 3, 4]
a.pop(0)
print(a)

a = [1, 2, 3, 4]
a.pop(2)
print(a)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
[2, 3, 4]
[1, 2, 4]
{% endhighlight %}
</div>
</section>

<section markdown="block">
### By the Way...

There are a few other list [methods in the documentation](http://docs.python.org/3.2/library/stdtypes.html#mutable-sequence-types). 

* reverse - reverses list in place
* index(value) - returns index of value
* insert(index, value) - inserts value at index

I won't cover these in the exam or homework; you can use them if you like...
</section>

<section markdown="block">
## [Iteration Over Sequences Using Indexes](iteration-indexes.html)
</section>

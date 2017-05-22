---
layout: slides
title: Euclidean Rhythms
---
<section markdown="block" class="title-slide">
# Euclidean Rhythms
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Oh, A Brief Diversion

__How did Euclid's algorithm work again? Let's try it with 90 and 36.__

<div class="incremental" markdown="block">
{% highlight python %}
"""
while a != b # as long as a and b aren't equal
  if a < b   # make sure we know which is larger
    swap
  else        # form a new pair (retain the smaller, b)
    a = a - b # a becomes the difference of original a and b
give back either a or b!

 a | b
--------------
90 | 36
54 | 36
36 | 18
18 | 18
--------------
Done: 18
"""
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Same But Different

That was the _original_ version of Euclid's algorithm. There are a couple of other variants. Here's one using the remainder (modulo).

<div class="incremental" markdown="block">
{% highlight python %}
"""
while b != 0 # as long as b isn't 0
  temp = a   
  a = b      # a becomes b
  b = a % b  # b is the remainder of original a / b
return a     # a is the gcd

 a | b
--------------
90 | 36
36 | 18
18 | 0
--------------
Done: 18
"""
{% endhighlight %}
</div>

</section>

<section markdown="block">
### One More

__How about 8 and 5?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
 a | b
--------------
 8 | 5
 5 | 3
 3 | 2
 2 | 1
 1 | 0
--------------
Done: 1
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Distributing Items Evenly

Easy if 4 items in 8 slots. 

1. imagine that 1 represents a slot with something in it, 0 represents an empty slot
2. what would the resulting pattern look like for an even distribution?
3. (clearly it wouldn't be 11110000)


<div class="incremental" markdown="block">
{% highlight python %}
"""
1 1 1 1, 0 0 0 0
10 10 10 10
10101010
(pretty evenly distributed, eh?)
"""
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Another One?

__What if we have 13 slots, and we want to distribute 5 items into those thirteen slots evenly?__ &rarr;


<div class="incremental" markdown="block">
1. 1 1 1 1 1, 0 0 0 0 0 0 0 0
2. 10 10 10 10 10,  0 0 0 
3. 100 100 100, 10 10
4. 10010 10010, 100
5. Done! 1001010010100
</div>
</section>

<section markdown="block">
### A Little Like Euclid's Algorithm, Right?

* We try to divide the right hand side into the left evenly.
* We end up with a remainder
* (We can even try to match up the numbers)

</section>

<section markdown="block">
### And. I Just Want to Dance.

What if we used that distribution method to place beats in a series of steps... to generate a rhythm?


<div class="incremental" markdown="block">

Apparently, the Euclidean Algorithm can be used to generate rhythms.  A paper by Godfried Toussaint explores the concept of Euclidean Rhythms. See [http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf](http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf).

* Euclid's Algorithm can be used to generate traditional music rhythms
* The rhythms generated cover a large number of world music rhythms 
* __Let's take a listen!__ &rarr;

</div>
</section>

<section markdown="block">
## [Functions / Odds and Ends ](functions.html)
</section>

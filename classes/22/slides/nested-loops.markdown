---
layout: slides
title: Nested Loops
---
<section markdown="block" class="title-slide">
# Nested Loops
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### You Can Loop Within a Loop!

__What does this code output? &rarr;__

{% highlight python %}
for i in range(2):
	for j in range(2):
		print("%s%s" % (i, j))
{% endhighlight %}
<div class="incremental" markdown="block">
{% highlight python %}
00
01
10
11
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Breaking Down Nested Loops

* the inner most loop must finish iterating before the outer loop goes on to its next iteration
* both loop variables are accessible in the body of the innermost loop
</section>

<section markdown="block">
### Chess Board Squares

__Print out the names of each square on a chess board using nested loops &rarr;__  See [this article on chess notation](http://www.chessstrategiesblog.com/chess-notation/):

* columns are a through h
* rows are 1 through 8
* letter comes first

{% highlight pycon %}
a8 b8 c8 d8 e8 f8 g8 h8 
a7 b7 c7 d7 e7 f7 g7 h7 
a6 b6 c6 d6 e6 f6 g6 h6 
a5 b5 c5 d5 e5 f5 g5 h5 
a4 b4 c4 d4 e4 f4 g4 h4 
a3 b3 c3 d3 e3 f3 g3 h3 
a2 b2 c2 d2 e2 f2 g2 h2 
a1 b1 c1 d1 e1 f1 g1 h1 
{% endhighlight %}

</section>

<section markdown="block">
### Chess Board Squares Solution

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/21/chess_board_coords.py  %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Sieve

[Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity)

__Let's try to figure out a few different ways of doing this &rarr;__
</section>

<section markdown="block">
### Sieve Version 1

{% highlight python %}
{% include classes/21/sieve.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Sieve Version 2

{% highlight python %}
{% include classes/21/sieve_true_false.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Sieve Version 3

{% highlight python %}
{% include classes/21/sieve_with_del.py  %}
{% endhighlight %}
</section>

<section markdown="block">
### Lists in Lists 

You can access an element within a list that's within a list by indexing __twice__!  The first index is the place in the outer list, the second index is the place in the inner list.

{% highlight python %}
a = [['foo', 'bar'],['baz', 'qux']]
print(a[0][1])
# gives back bar
{% endhighlight %}

</section>

<section markdown="block">
### Lists in Lists Example

__What does this code output? &rarr;__

{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(a[0][0])
print(a[0][1])
print(a[1][0])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
1
2
4
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Looping Over Lists in Lists

{% highlight python %}
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for inner_list in a:
	for number in inner_list:
		print(number)

for i in range(len(a)):
	for j in range(len(a[i])):
		a[i][j] += 10

print(a)
{% endhighlight %}
</section>


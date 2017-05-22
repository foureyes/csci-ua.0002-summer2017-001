---
layout: slides
title: Warm-up for #18 
---
<section markdown="block" class="title-slide">
# About Class #18
{% include title-slide-footer.html %}
</section>


<section markdown="block">
### Swap First and Second

Write a function called __swappy__:

* it has one parameter, a list
* it'll create an entirely new list (how?) that's copied from the list passed in
* it'll swap the first and second element of the new list
* if the list is less than two elements, it'll just give back the original list
* finally, its return value is the new list with the first and second element swapped

{% highlight python %}
print(swappy(['a', 'b', 'c']))
# prints ['b', 'c', 'a']
{% endhighlight %}
</section>


<section markdown="block">
### Swap First and Second 

Here's one way to do it...

{% highlight python %}
def swappy(my_list):
	# create a copy of the original list
	new_list = my_list[:]
	if len(new_list) >= 2:
		new_list[0], new_list[1] = new_list[1], new_list[0]
    return new_list

{% endhighlight %}
</section>

<section markdown="block">
### An Average Point

Write a function called __average_point__:

* it has one parameter, a list of lists
* each sub list represents a point on the coordinate plain, so each will be composed of two elements
* for example: [[0, 0], [5, 10]] ... is a list of two points (0, 0) and (5, 10)
* it'll create a new single point where the x value is the average of all of the x's and the y value is average of all of the y's
* finally, it'll return this new single point

{% highlight python %}
print(average_point([[2, 2], [3, 1], [4, 0]]))
# prints out [3.0, 1.0]
{% endhighlight %}
</section>

<section markdown="block">
### An Average Point Solution

Nested lists can be tricky sometimes, but here's a solution that could work:

{% highlight python %}
def average_point(points):
	x_total = 0
	y_total = 0
	for p in points:
		x_total += p[0]
		y_total += p[1]
	return [x_total / len(points), y_total / len(points)]
	
{% endhighlight %}
</section>

<section markdown="block">
### All Y

Using the same list of points (a list of lists) as the previous example, write a function called __all_y__:

* it should take a list of points as one parameter
* it should return a new list with only points where the y value is greater than the x value

{% highlight python %}
print(all_y([[2, 200], [3, 1], [4, 9]])) # --> [[2, 200], [4, 99]]
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
def all_y(points):
	new_points = []
	for point in points:
		if point[1] > point[0]:
			new_points.append(point)
	return new_points
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Sorting an List Without Sort!

1. go through each position in the list and look at that element
2. compare the value of the current element with the value of the next element
3. if the value of the current element goes after the value of th next element, swap elements
4. remember, the idiomatic way of swapping in python is a, b = b, a 
5. of course, once you're at the last element, there's no next element to check
6. once you've gone through all of the elements... REPEAT the whole process if you've swapped at least once

</section>
{% comment %}
<section markdown="block">
### 
</section>
<div class="incremental" markdown="block">
{% highlight python %}
{% endhighlight %}
</div>

{% endcomment %}



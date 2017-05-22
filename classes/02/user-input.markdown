---
layout: slides
title: User Input 
---

<section markdown="block" class="title-slide">
# User Input
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Getting Input From the Shell

* we can prompt the user through the console / terminal / shell / command prompt
* the user enters input through the same mechanism
</section>

<section markdown="block">
### The input() Function

There's a built-in function in Python called __input__ ...

* __what does it do? does it have parameter(s)?__ &rarr;
* __(how can we find out through IDLE?)__ &rarr;
* __what does it return?__ &rarr;
* __what if the user input is a number?__ &rarr;

<div class="incremental" markdown="block">
* __input__ takes one parameter - the prompt that is displayed (think of it as print plus retrieving user input!) 
* use __help__! or check the docs...
* it returns a string representing the user's input
* it will __always return a string__ - even if the user inputs a number
</div>
</section>

<section markdown="block">
### Let's Try Some Examples of input()
{% highlight python %}
>>> s = input(">")
>foo
>>> type(s)
<class 'str'>
>>> x = input(">")
>5
>>> type(x)
<class 'str'>
>>> x = int(input(">"))
>5
>>> type(x)
<class 'int'>
{% endhighlight %}

</section>

<section markdown="block">
## The input function does two things: 

* __prints__ out the prompt
* __returns__ the value typed in by the user back to your program

</section>

<section markdown="block">
### Write a Program That Asks For a Name
... and then says "hi".  Here's the sample output; the text after the &gt; is user input.

{% highlight python %}
What's your name?
>Joe
Hi Joe
{% endhighlight %}
<div class="incremental" markdown="block">
__A potential solution...__ &rarr;

{% highlight python %}
print("What's your name?")
name = input(">\n")
print("Hi " + name)
{% endhighlight %}

(note that we used __newline__, __\n__, to create a line break for the prompt that's printed out)
</div>
</section>

<section markdown="block">
### Write a Program That Adds Exclamation Points
Here's the sample output; the text after the &gt; is user input.

{% highlight python %}
How loudly?
>4
This is really loud!!!!
{% endhighlight %}
<div class="incremental" markdown="block">
__A potential solution...__ &rarr;

{% highlight python %}
loudly = input("How loudly?\n>")
print("This is really loud" + "!" * int(loudly))
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Review
* how do we get user input?
* when we get input, what's the type of the value that's returned?
</section>

<section markdown="block">
## [Design, Input, Processing, and Output](design-input-output.html)
</section>

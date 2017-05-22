---
layout: slides
title: File I/O Review 
---
<section markdown="block" class="title-slide">
# File I/O Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### A Quick Aside on Main Memory / RAM

Your computer stores data for your running programs in __main memory__ or __RAM__ (random access memory).  Ram is an example of __volatile memory__.

* __volatile memory__ - memory that requires an electrical current to maintain state
* __non-volatile memory__ - memory that can maintain state without power

Some examples of non-volatile memory include:

* hard drives, 
* flash drives (SSDs, USB drives, etc)
* CDs and DVDs
</section>

<section markdown="block">
### Storing Data in Main Memory

__What are the consequences of your data being stored in your computer's main memory?__ &rarr;

<div class="incremental" markdown="block">
* data may go away at the end of the program, or when the computer gets turned off
* if you're working with large amounts of data, you may run out of RAM (which is typically less than the amount of non-volatile memory that you have)!
</div>
</section>

<section markdown="block">
### Storing Data Elsewhere...

__What if we want to persist our data beyond the lifetime of the running program... or through on-off cycles?__ &rarr;

<div class="incremental" markdown="block">
* store data on non-volatile media!
* ... maybe as a file on your hard drive or SSD...
</div>
</section>

<section markdown="block">
### File Input and Output

* we can store data in files!
* Python can handle file input and output - __file I/O__

</section>

<section markdown="block">
### open

Python has a __built-in__ function called __open__.  

* __open__ opens a file!
* it can be used for reading or writing
* it takes two arguments: a __filename__ and a __mode__
	* __filename__
		* the absolute path... 
		* or relative (to the script that your writing) path
	* __mode__ ... for now, we only care about:
		* __'w'__ - write
		* __'r'__ - read
		* __'a'__ - append
* it returns a __file handle__ object
</section>

<section markdown="block">
### File Handles

A __handle__ is:

* an object in your program that represents an underlying resource, such as a file
* connected to the actual resource, and can consequently manipulate it

A __file handle__ is:

* an object that allows your program to manipulate/read/write/close an actual file on disk
</section>

<section markdown="block">
### File Handles Continued

Again, __file handle__ object allows you to read and write to a file.  Think of it as representing a file.  The general program flow for file input and output is as follows:

1. open a file
2. either read or write to the file
3. close the file
</section>

<section markdown="block">
### Writing to a File

{% highlight python %}
f = open("test.txt", "w")
f.write("I'm in yr filez!\n")
f.write("Writin' some bits!\n")
f.write("...\n")
f.close()
{% endhighlight %}

* call __open__ ...
	* with the name of the file to open, 'test.txt'
	* and the mode, 'w' to specify that we're writing to it
* use the __write__() method to write strings to a file
* you must always call __close__() on  file when you're done with it
</section>

<section markdown="block">
### Using open to Write to a File

Let's look at __open__ and __write__ in more detail:

__open(filename, mode)__

* filename is the file to be opened
* a mode of 'w' means that the file will be opened for writing
* if the file doesn't exist, 'w' will __create__ it
* if the file exists, 'w' will __overwrite__ it!

__write(s)__

* does not automatically add new lines
* takes a string as an argument (non-string arguments result in an error)
</section>


<section markdown="block">
### Reading a File

To open a file in read mode, use "r" as the second argument:

{% highlight python %}
f = open("test.txt", "r")
{% endhighlight %}

</section>

<section markdown="block">
### Methods for Reading a File

Once you have a __file handle__, you can read the contents of a file by using one of the following methods on your __file handle object__:

* __readline__() - read one line at a time
* __read__() - reads the entire contents of a file into memory

__Why would you use one method over another?__

<div class="incremental" markdown="block">
* you may want to use readline if you want to preserve the structure of a file (that is, you don't want to deal with new line characters)
* you may want to use readline if you're working with a very large file
</div>
</section>

<section markdown="block">
### Using readline

__readline__() takes no arguments, and it returns a string.

* it always returns a string, even if it's just a new line character ("\n")
* if it returns an empty string, then we've reached the end of the file

</section>

<section markdown="block">
### Using readline Continued

__To use readline to read the contents of a file, loop forever (or at least until we know that we're at the end of a file! ...__

<div class="incremental" markdown="block">
{% highlight python %}
f = open("test.txt", "r")
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print(line)
f.close()
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Using readline() Continued More!

__What is the first line that will be printed?  What is the actual string representation? How many times will the loop run?__
{% highlight python %}
f = open("test.txt", "r")
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print(line)
f.close()
{% endhighlight %}

<div class="incremental" markdown="block">
* I'm in yr filez!
* "I'm in yr filez!\n"
* 3 times
</div>
</section>

<section markdown="block">
### Reading a File in All At Once

Use the __read__() method on your file handle object to read the file in all at once.  __read__() returns the entire contents of a file (including newlines) as a string.

{% highlight python %}
f = open("test.txt", "r")
contents = f.read()
print(contents)
{% endhighlight %}

</section>

<section markdown="block">
### Memory Efficiency

__When you use read or readline, which do you think uses more of your computer's main memory... and why?__ &rarr;

<div class='incremental' markdown='block'>
* read consumes more memory because it reads the entire file at once!
* similarly, in our previous exercises... we had solutions that either used up a lot of memory... or were expensive computationally
</div>
</section>

<section markdown="block">
## File Exercises
</section>

<section markdown="block">
### Names in Alphabetical Order

* read the contents of a file called names.txt
* the file will have first names in it
* sort the names by alphabetical order
* write the newly sorted names to another file
* the original file should remain unchanged

The contents of names.txt will be:

{% highlight python %}
Erin
Charles 
Bob
David
Alice
{% endhighlight %}

</section>

<section markdown="block">
### A Potential Solution

{% highlight python %}
f = open("names.txt", "r")
contents = f.read()
names = contents.split("\n")
names.sort()
f = open("names_sorted.txt", "w")
for name in names:
        f.write(name + "\n")
{% endhighlight %}
</section>

<section markdown="block">
### Lottery Ticket

Write a function that creates a lottery ticket.  The lottery ticket should:

* have the words "Lucky Numbers" on the first line
* contain 5 __unique__ numbers between 1 through 59
* each number printed from __lowest to highest__
* each number printed on its own line
* be saved to a file named lotto.txt

{% highlight bash %}
Lucky Number
3
28
33
50
51
{% endhighlight %}
</section>

<section markdown="block">
### Pseudocode #1

{% highlight python %}
"""
create a list of numbers
mix up the numbers
open a file
write out 'lucky numbers' to file
get the last 5 numbers from list
sort them
for each number in list
	write it the number
"""
{% endhighlight %}
</section>

<section markdown="block">
### Pseudocode #2

{% highlight python %}
"""
create an empty list to store numbers
while length of list < 5
	generate a random number
	if the number isn't in the list of stored numbers
		add it
sort numbers
open a file
write out 'lucky numbers' to file
for every number in the list
	write it to the file
"""
{% endhighlight %}
</section>

<section markdown="block">
### Potential Solution

{% highlight python %}
import random

# generate list of sorted unique random numbers
random_number_list = []
while len(random_number_list) < 5:
    n = random.randint(1, 59) 
    if n not in random_number_list:
        random_number_list.append(n)
random_number_list.sort()

# write out the list of numbers to a file
file_handle = open('lotto.txt', 'w')        
file_handle.write('Lucky Numbers\n')
for n in random_number_list:
    file_handle.write('%s\n' % n)
{% endhighlight %}
</section>

<section markdown="block">
### How About Some Tidying Up

__Can we abstract out some of this code into a reusable function?__ &rarr;
</section>

<section markdown="block">
### Another Version

{% highlight python %}
import random
def unique_random_list(sample_size, a, b):
    """ 
    sample_size is the number of random numbers to return
    a is the start of the pool of numbers to choose from
    b is the end of the pool of numbers to choose from
    """
    numbers = []
    while len(numbers) < sample_size:
        n = random.randint(a, b)
        if n not in numbers:
            numbers.append(n)
    return numbers 

observed = unique_random_list(3, 1, 5)
assert 3 == len(observed)
for n in observed:
    assert 1 == observed.count(n)

{% endhighlight %}
</section>

<section markdown="block">
### Another Version Continued

{% highlight python %}
random_number_list = unique_random_list(5, 1, 59)
random_number_list.sort()
file_handle = open('lotto.txt', 'w')
file_handle.write('Lucky Numbers\n')
for n in random_number_list:
    file_handle.write('%s\n' % n)
{% endhighlight %}
</section>



<section markdown="block">
### BTDubz (re random)

By the way... (of course) there's already a function in the random module that does this: 

* random.__sample__(population, k)
	* __population__ - a sequence or set (think list) containing the elements to sample from
	* __k__ - the number of elements to retrieve
* example output:

{% highlight pycon %}
>>> print(random.sample([1, 2, 3, 4, 5, 6, 7], 4))
[7, 3, 1, 6]
>>> print(random.sample([1, 2, 3, 4, 5, 6, 7], 4))
[7, 5, 4, 6]
>>> print(random.sample([1, 2, 3, 4, 5, 6, 7], 4))
[5, 6, 3, 4]
{% endhighlight %}
</section>

<section markdown="block">
### Jane Austen

You can download a text version of [Pride and Prejudice](http://www.gutenberg.org/cache/epub/1342/pg1342.txt) from Project Gutenberg

__Using that file with our pig_latin and translate_passage functions... can you write out a pig latin version of Pride and Prejudice?__

Also... these are [sort](http://en.wikipedia.org/wiki/Sense_and_Sensibility_and_Sea_Monsters) [of](http://en.wikipedia.org/wiki/Pride_and_Prejudice_and_Zombies) from Jane Austen....

</section>

<section markdown="block">
### Downloading the File

Save the text version of [Pride and Prejudice](http://www.gutenberg.org/cache/epub/1342/pg1342.txt) in the same folder that your program is in.

</section>

<section markdown="block">
### Pig Latin

{% highlight python %}
def to_pig_latin(w):
    """translates word to pig latin"""

    w = w.lower()

    if not w.isalpha():
        return w

    if w == '' or len(w) == 1:
        return w

    if w[0] in 'aeiou':
        return w + 'way'

    first_two = w[0:2]
    if first_two == 'qu' or first_two == 'ch' or first_two == 'sh' or first_two == 'th':
        return w[2:] + first_two + 'ay'

    return w[1:] + w[0] + 'ay'
{% endhighlight %}
</section>

<section markdown="block">
### Translate Passage

{% highlight python %}
def translate_passage(passage):
    """translates text into pig latin"""
    translation = ""
    word = ""
    for c in passage:
        if not c.isalpha():
            translation += to_pig_latin(word)
            translation += c
            word = ""
        else:
            word += c
    return translation
{% endhighlight %}
</section>

<section markdown="block">
### Putting it All Together

{% highlight python %}
# open file for reading
fh_in = open('pg1342.txt', 'r')
s = fh_in.read()
fh_in.close()

# translate and write
fh_out = open('pg1342_translated.txt', 'w')
fh_out.write(translate_passage(s))
fh_out.close()
{% endhighlight %}
</section>

<section markdown="block">
## Review End
</section>

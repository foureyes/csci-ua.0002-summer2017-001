---
layout: slides
title: Creating Modules 
---
<section markdown="block" class="title-slide">
# Creating Modules
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Modules

__What's a module again?__ &rarr;

<div class="incremental" markdown="block">
* it's just a file that contains Python code!
* use __import__ to bring in a module
* the name of the module is the file name without extension
* for example - import mymodule _brings in_ the file named mymodule.py
* ...or importing random may bring in this file (varies depending on your system and installation of Python):
{% highlight python %}
/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/random.py
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Where Does Python Find Modules?

* it checks the __list of directories of directories in variable called sys.path__ &rarr;
* __the current directory (where your program is located) is always at the beginning of this list__


</section>

<section markdown="block">
All Together Now...
</section>

<section markdown="block">
### Let's Try Creating and Using Our Own Module

__Create a Python file; call it stringtools.py__ &rarr;  

* save a file as  __stringtools.py__
* it should have a single function, called pluralize
* the function should take a single argument, a string
* it should return the original string with an s appended to it 

<div class="incremental" markdown="block">
{% highlight python %}
# in stringtools.py:
def pluralize(word):
    return word + 's'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### ...And Using It

Use the pluralize function in your stringtools module...__Create a new file; call it myprogram.py__ &rarr;

* create __myprogram.py__ - make sure it's in the same directory as your module
* ask the user for a word
* print out the plural of the word using your module

<div class="incremental" markdown="block">
{% highlight python %}
# in myprogram.py
import stringtools
user_response = input('Word plz>\n')
plural_w = stringtools.pluralize(user_response)
print(plural_w)
{% endhighlight %}
</div>
</section>

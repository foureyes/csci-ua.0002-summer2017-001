---
layout: default
title: Software
nav-state: software
---

Installing Python 3 and IDLE
====

You'll need to install a Python for this class (because, you know, that's what we're programming in)!

&#128013;&#128013;&#128013;&#128013;

* __we'll be using Python 3.x__
* it comes with a text editor called __Idle__
* instructions for installation can be found on the departmental syllabus: [http://cs.nyu.edu/courses/fall15/CSCI-UA.0002-002/common_syllabus/#software](http://cs.nyu.edu/courses/fall15/CSCI-UA.0002-002/common_syllabus/#software)

<a name="text"></a> <a name="text_editor"></a> <a name="pycharm"></a>

<br />

Alternatives to IDLE (Other Text Editors)
====

<a name="alternate"></a>
<br />
<a name="pycharm"></a>

PyCharm
----
* [Download the Free _Community Edition_ of PyCharm](https://www.jetbrains.com/pycharm/download/) 
* Install PyCharm 
	* If you're on OSX, Yosemite, you may have to trick PyCharm into working with your system...
		* After moving PyCharm into your Applications folder...
		* Open the Applications folder (/Applications) in finder
		* Right-click on the PyCharm icon
		* Click on Show Contents
		* Right-click on info.plist
		* Choose "Open With"
		* Choose "Other..."
		* Choose "TextEdit"
		* Find JVMVersion
		* In the line underneath,  &lt;string&gt;1.6*&lt;/string&gt;
		* ...change 1.6* to 1.8*
		* [See the animated gif](resources/img/pycharm.gif))
* Configure PyCharm to use Python 3
	* Go to PyCharm (in menu bar) 
	* Choose "Preferences"
	* Click on "Default Project" on the left sidebar
	* Click on "Interpreter"
	* Choose Python 3 from the dropdown labeled "Project Interpeter" on the right
	* [See the animated gif](resources/img/pycharm2.gif))
* Create a new program...
	* Create a new project
	* Click on project name on left side bar
	* Go to File in the menu bar
	* Choose "New..."
	* Choose "File"



<a name="sublime"></a>

Using Sublime Text 2 with Python 3
----

__Overview__

Sublime text uses "build systems" to let you run files through external commandline applications.  One use for this is to run your code through the Python interpreter!

Sublime Text 2 already comes with a Python build, but it uses your system's Python, which is most likely 2.x.  If you've installed Python 3 side-by-side with your system Python, you can create a build specifically for Python 3.

__Instructions__

(note that these instructions are osx specific; you may not need the "path" line in the configuration for windows)

* [Download](http://www.sublimetext.com/2) and install Sublime Text 2
* Start Sublime Text 2 
* Go to Tools &rarr; Build System &rarr; New Build System...

![sublime1](resources/img/sublime1.png)



* Add this code to untitled.sublime.build:

{% highlight bash %}
{
	"cmd": ["python3", "-u", "$file"],
	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
	"selector": "source.python",
	"path": "/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin"
}
{% endhighlight %}

* Save this file as Python3.sublime.build (put it in /Users/yourusername/Library/Application Support/Sublime Text 2/Packages/User, which is the default directory that sublime drops you in)
* Go to Tools &rarr; Build System 
* You should now see Python3 as a build option
* Select Python3 as your build system:

![sublime2](resources/img/sublime2.png)



__Usage__

From here on, you can use &#8984; + b (or Tools &rarr; Build) to run your Python 3 programs

__Verification__

* Create a new file and save it as test_python3_build.py
* In this file, put in the following lines of code:

{% highlight python %}
import sys
print(sys.version)
{% endhighlight %}

* Run your program: &#8984; + b
* It should print out something similar to:

{% highlight bash %}
3.2.3 (v3.2.3:3d0686d90f55, Apr 10 2012, 11:25:50) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
[Finished in 0.1s]
{% endhighlight %}




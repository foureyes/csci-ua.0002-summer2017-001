---
layout: default
title: Home 
nav-state: index
---

<a name="course-info"></a>




Course Information
====

__Course Details__

* __Course Number:__ {{ site.course_number }}
* __Section:__ {{ site.course_section }} {% if site.course_section_2 %} and {{ site.course_section_2 }} {% endif %}
* __Semester:__ {{ site.course_semester }}
* __Instructor:__ Joe Versoza {% if site.course_section_2 %} 
* __Section {{ site.course_section }}__
    * __Meeting Time:__ {{ site.course_time }}
    * __Room:__ {{ site.course_room }}
* __Section {{ site.course_section_2 }}__
    * __Meeting Time:__ {{ site.course_time_2 }}
    * __Room:__ {{ site.course_room_2 }}
{% else %}
* __Meeting Time:__ {{ site.course_time }}
* __Room:__ {{ site.course_room }}
{% endif %}

<a name="contact-info"></a>
__Contact Information__

* __Email:__ jversoza at cs dot nyu dot edu
* __Office Hours:__  {{ site.office_hours }}
* __Office Hours Room:__ {{ site.office_hours_room }}

<a name="topics"></a>

Topics
====
* Introduction to Programming Languages
* Python Basics
* Working with variables and operations
* Control Structures
* Repetition Structures
* Working with Text
* Functions and Modules
* Lists
* File Input & Output
* Dictionaries
* Additional topics, such as graphics, may be covered at the instructor's discretion and time-permitting.

<a name="grading"></a>

Grading
====

* __35%__ - Final Exam
* __5%__ - Quizzes
* __5%__ - In-class Activities and Quizzes / Attendance
* __25%__ - Assignments
* __30%__ - Midterm #1

Continuing with computer science courses requires **a C or better** in this course. 

<a name="homework"></a>

Homework
====
* About one or __two__ homework assignments per week 
* Turned in **electronically via NYU Classes**
* Homework assignments are due one week after posting
* Late homework policy
	* The assignment will _usually_ stay open for late submissions one day after the assignment is due
	* Late homework will receive a minor penalty
	* After one day late, homework cannot be submitted
* __You must write your own code!__
	* Copying code from another student or an online resource will be considered cheating
    * Sharing code with another student will also be considered cheating
    * If an issue arises due to copying or distributing code, the student will be required to meet with Director of Undergraduate Studies 
* Help debugging, such as helping determine the root cause of a program crash, and high-level discussions, such as discussing how certain basic programming structures work, are allowed

<a name="books"></a>

Textbooks
====

* __Required__
    * [Starting Out with Python (3rd Edition, but older can be used too)](http://www.mypearsonstore.com/bookstore/starting-out-with-python-9780133582734)<br />
by Tony Gaddis<br />
Paperback: 640 pages<br />
Publisher: Addison-Wesley; 3 edition (February 2, 2014)<br />
ISBN-10: 0133582736<br />
ISBN-13: 978-0133582734 <br />
Ebook: 9780133582734.JB <br />
* __Optional__
    * [How to Think Like a Computer Scientist: Learning with Python 3](http://openbookproject.net/thinkcs/python/english3e/)<br />
Version date: October 2012<br />
by Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers<br />

Required Software
=====

Installing Python
-----

* Windows
    1. Visit [http://www.python.org/getit/](http://www.python.org/getit/)
    2. Download the Windows MSI installer (if you have a newer computer you probably need the 64 bit version)
    3. A window labeled Opening python-3.3.3.msi will appear – click Save File
    4. After the download is complete, a dialog box will open asking ‘Would you like to save this file?’ – click Save file
    5. An icon labelled ‘python-3.3.3′ for release 3.3.3 will appear on the screen. (Perhaps a more recent release will appear.)
    6. When you click the icon, the computer will ask ‘Do you want to run this file?’, Click the run button.
    7. In the setup box, the option ‘install for all users’ will have a circle with a period in it. Click the next button.
    8. A box asking you to select destination directory with the proposed directory Python30. Click the next button.
    9. In the next dialog box (Customize Python 3.3.3), click the next button.
    10. Finally, click finish.
    11. To get the IDE icon on the screen, go to Start/All Programs/python 3.0. A small window will appear to the right with IDLE(PythonGUI). Drag IDLE (PythonGUI) to your desktop to make a shortcut.
* Mac
    1. Visit [http://www.python.org/getit/](http://www.python.org/getit/)
    2. Download the Mac OS X installer for your Operating System. You can check your OS version by clicking on the Apple at the top left side of your computer and looking at the version number under the Apple icon. In general, users of newer computers will want to download the 64 bit version.
    3. A window opens indicating that you want to open python-3.3.3.dmg,If the Save file. Then click OK.
    4. The download window will open. Double click the icon.
    5. In a short while, Install succeeded will appear. Click the close button.
    6. Click on your Applications Folder and find the newly created Python folder. Double click on the IDLE icon to launch IDLE.
    7. Note: if you are running Mac OS 10.9 (Mavericks) you may see the following error message when launching IDLE: `WARNING: The version of Tcl/Tk (x.x.x) in use may be unstable.`
    8. If you see this message you should quit IDLE and install a new version of ActiveTcl version that matches the error message you are getting (i.e. if the error message says version 8.5.9 you can install any version that begins with the numbers 8.5) -- here's the website where you can download an updated version of Tcl/Tk: http://www.activestate.com/activetcl/downloads.

Tutoring Schedule
=====
TBD

<!-- got lazy here, wants some anchorzzzz -->
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<div>
</div>

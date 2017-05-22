"""
fortune_improved.py - 12 points
=====

Improve the fortune telling program from an earlier homework.  This version
will do the following:

* Allow the user to add or remove fortunes
* Allow the user to retrieve a random fortune

The program will:

* Continue to ask for a command, (add, remove, or get a fortune... or quit)
* Stop asking if the command is 'q' for (q)uit (and say Bye!)
* For the other commands:
  * the letter 'a' for (a)dd - will prompt the user for a new fortune to add
  * the letter 'r' for (r)emove 
    * will list all the fortunes, each prefixed with a number
    * the user will be prompted for a number
    * and that fortune will be deleted 
    * if the number is not an index that exists, then print an error 
      message instead
  * the letter 'l' for remove (l)ast
    * will only remove last if there's at least one element
    * will print out the element removed
  * the letter 'g' for (g)et - will retrieve a random fortune

Some notes on implementation:

* Use a list to store the fortunes
* Get a random element from a list by using randomly generating an index
  or by looking up a built-in function that can randomly choose an element 
  from a list (this exists in the random module!)
* The pop method may be helpful for one of the commands
* Some sort of outer looping mechanism may help drive your program
* You may want to use fortunes to break up your program into more manageable
  pieces

Example Output That: 

* gets a random fortune
* adds a fortune
* gets another random fortune
* attempts to remove a fortune that doesn't exist
* removes the 2nd fortune (the one at index 1)
* quits
-----

(a)dd, (r)emove, remove (l)ast or (g)et a fortune, (q) to quit
> g
There are many quotation marks in your future!
(a)dd, (r)emove, remove (l)ast or (g)et a fortune, (q) to quit
> a
Give me a fortune to add.
> You will soon press q.
(a)dd, (r)emove, remove (l)ast or (g)et a fortune, (q) to quit
> g
You will soon press q.
(a)dd, (r)emove, remove (l)ast or (g)et a fortune, (q) to quit
> r
0 You'll have a pastry today.
1 There are many quotation marks in your future!
2 You will soon press q.
Which fortune would you like me to remove?
> 8
That fortune doesn't exist
(a)dd, (r)emove, remove (l)ast or (g)et a fortune, (q) to quit
> r
0 You'll have a pastry today.
1 There are many quotation marks in your future!
2 You will soon press q.
Which fortune would you like me to remove?
> 1
(a)dd, (r)emove, remove (l)ast or (g)et a fortune, (q) to quit
> q
Bye!
=====
"""

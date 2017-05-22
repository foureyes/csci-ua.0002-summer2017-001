"""
battleship.py - Extra Credit for Lower Midterm Score (Up to 6% Added)
=====

This program will count as extra credit to your lower scoring midterm
(provided that you did not score 10% better on your second midterm).

It will only be accepted as extra credit if:

1. The program runs. That is no, syntax errors (programs with run-time errors 
   will be accepted, but run-time errors will receive some penalty).
2. The program allows the player to enter the location of their opponent's
   (the computer's) ship. See #2 in the instructions below.
3. The program accepts player input in row,column format. See #3 in the 
   instructions below.
4. The program contains at least two function (main is acceptable as one of
   the functions, but it does not have to be one of the functions)

Write a simplified one player version of Battleship.  In this version of 
Battleship, the computer hides a ship in a 5 x 5 grid.  The player must find
the ship by inputting row and column pairs.  If the player finds the ship,
the player wins.  The player has unlimited turns!

0. Your program MUST CONTAIN AT LEAST TWO FUNCTIONS (one of them can be main,
   but is not required to be)

1. The computer will generate a board of 5 x 5 o's with column and row 
   numbers as 0 through 4 (one way to do this is to create a variable that 
   contains a list of lists):

o o o o o
o o o o o
o o o o o
o o o o o
o o o o o


2. The computer's ship only occupies one "square" (unlike the regular version 
   of Battleship). This ship should be placed in a random location on the 
   board. However, before this is done, to help make testing your game easier, 
   your program MUST ASK IF THE PLAYER WANTS to explicitly set the location of
   the computer's ship. 
   
   Do you want to set the location of the computer's ship? 
   Type row,col to set or press ENTER/RETURN to skip 
   >

   If the player types in a row and column (for example 1,2), then the 
   computer's ship is placed at that location. No validation is required; you
   can assume that the user will always type in a row and column or they will 
   type in nothing. If the player doesn't type in anything and just presses 
   ENTER/RETURN (in which case input will return an empty string, ""), the 
   computer will generate a random row and column for the location of its ship 
   (both are 0 through 4).

3. The player is then asked to input a row and then a column (both are 0-4),
   separated by a comma... for example: 1,2 means row 1, column 2. Your 
   program MUST ACCEPT INPUT IN THE FORMAT ABOVE.
   a. If the input is just q, the game ends.
   b. If the input is invalid, allow an error to occur in your game (you 
      don't have to worry about invalid input)

4. The row and column input is either a hit or a miss.
   a. If the input uncovers the ship, the player wins and the game ends.
   b. If the input is a miss, the 'o' on the grid is replaced with " " (a 
      space) to keep track of squares that have already been missed.

5. After every turn, the board is printed out again.  See the output at the end
   of this comment for a sample game.



Partial credit will be given!

Hints:
-----
There are many ways to implement this program.  These hints are general guides 
to get started, but don't feel obligated to follow them.

* a list of lists is one way to represent the grid
* (see the lists in lists slide for help)
* both row and column input should not be 'q' for the game to continue
  assignment
* a while loop may be useful to keep the game going until the above
  condition is met
* the string method, split, may be helpful in extracting the row and column
  numbers from the user's input
* it may be useful to break down the program into separate functions (for example, creating the board, detecting a hit, etc.)



Sample Output:
-----

One player battleship!
====================

   
Do you want to set the location of the computer's ship? 
Type row,col to set or press ENTER/RETURN to skip 
> 2,3

o o o o o
o o o o o
o o o o o
o o o o o
o o o o o
What row and column do you want to try? 
> 1,1


o o o o o
o   o o o
o o o o o
o o o o o
o o o o o
What row and column do you want to try?
> 2,3

The boat was at row 2 and column 3
YOU WON!!!!

o o o o o
o   o o o
o o o x o
o o o o o
o o o o o
"""

"""
funcynum.py (18 points + 3 extra credit)
=====

This file will contain functions that you'll use in feeling_quizzy.py. There
are 4 parts to this file, and they all depend on one another, so they must be 
done in order. The functions in this file will ultimately produce 'ASCII' art 
numbers. For example, the number 5:

*****
*
*****
    *
*****


Part 1 - Create functions that make horizontal and vertical line strings 
-----
Create three functions:

1. horizontal_line
    * input:
        * the character to make the line out of ('*' for example)
        * the total width of the line
        * the number of spaces before the line (the offset from the left)
    * processing: 
        * creates a <width> wide string composed of the characters specified, 
          starting with an <offset> number of spaces 
    * output: 
        * returns a string representing a horizontal line 

2. vertical_lines(char, height, offset, number, interior_offset):
    * input:
        * the character to make the line out of ('*' for example)
        * the total height of the line
        * the number of spaces before the line (the offset from the left)
        * the number of vertical lines to draw
        * the space between each line (an interior offset)
    * processing: 
        * creates a string that represents the specified number of vertical
          lines 
        * each line is <height> tall 
        * and is composed of the characters specified 
        * there are <interior offset> number of spaces between each vertical
          line
        * there is an <offset> number of spaces before the lines begin
        * for example, '* *\n* *\n* *\n* *' is a set of two vertical lines, 
          each 4 characters tall with no initial offset. NOTICE THAT THERE IS 
          NO NEW LINE at the end, and there ARE NO TRAILING SPACES
        * YOU MUST USE NESTED LOOPS TO CONSTRUCT THIS STRING
        * hint: the outer loop can represent row, the inner loop can represent
          column... and you can use the col_num or row_num to determine if an
          interior offset or newline should be added
    * output: 
        * returns a string representing a series of vertical lines
        
3. vertical_line(char, height, offset):
    * input:
        * the character to make the line out of ('*' for example)
        * the total height of the line
        * the number of spaces before the line (the left offset)
    * processing: 
        * creates a <height> tall string composed of the characters specified, 
          starting with an <offset> number of spaces 
        * hint: imply call your vertical_lines function so that only 1 line is
          printed (remember to pass along the offset and character, though!)
    * output: 
        * returns a string representing a single vertical line 

Examples:
print(horizontal_line('*', 5, 0))
*****

print(horizontal_line('x', 2, 4))
    xx

print(vertical_line('*', 2, 5))
     *
     *

# character, height, offset from left, number of lines, space between
print(vertical_lines('+', 4, 0, 5, 3))
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +


Part 2 - Create functions that return 0 through 9, plus (+), and minus (-)
-----

Create 12 additional functions that return the numbers 0 - 9, +, and -. All
numbers will have a flexible width, but you can assume that the HEIGHT OF THE
NUMBERS WILL ALWAYS BE 5. Use the horizontal and vertical line drawing 
functions to write these functions.

The functions will be called one, two ... minus. The general 
input/output/processing chart will looks similar for each functions. Here's an
example input/output/processing chart, an actual function definition for the
function that prints out the number one, and some examples of usage:

print_one
* input:  
    * a character to create the number with
    * the width of the number
* processing: 
    * creates an 'ASCII' art number that's 5 characters tall and as wide as the
      argument passed in (<width> characters wide)
    * if a width is less than 3, default to 3
* output:     
    * returns a string, that when printed, shows an 'ASCII' art number one

def one(char, width):
    if width < 3:
        width = 3
    return vertical_line(char, 5, width - 1)

Example Output (note the relationship between the number of leading spaces and
the total width):

# offset by 5 from the left
one('*', 5)
    *
    *
    *
    *
    *

# offset by 3 from the left
one('X', 3)
  X
  X
  X
  X
  X

one('$', 1)
$
$
$
$
$

Here's an example of running all of the functions and the resulting output:

print(zero('*', 5))
print()
print(one('*', 5))
print()
print(two('*', 5))
print()
print(three('*', 5))
print()
print(four('*', 5))
print()
print(five('*', 5))
print()
print(six('*', 5))
print()
print(seven('*', 5))
print()
print(eight('*', 5))
print()
print(nine('*', 5))
print()
print(plus('*', 5))
print()
print(minus('*', 5))

*****
*   *
*   *
*   *
*****

    *
    *
    *
    *
    *

*****
    *
*****
*
*****

*****
    *
*****
    *
*****

*   *
*   *
*****
    *
    *

*****
*
*****
    *
*****

*****
*
*****
*   *
*****

*****
    *
    *
    *
    *

*****
*   *
*****
*   *
*****

*****
*   *
*****
    *
    *

  *
  *
*****
  *
  *



*****

Part 3 - Create a function that checks an addition and subtraction operation
-----
Create a function called check_answer. It will will determine if a given 
addition or subtraction problem was solved correctly based on the operands, answer
and operator passed in. 

check_answer
* input:  
    * the 1st (or left) operand
    * the 2nd (or right) operand
    * the proposed answer
    * the operator... either + or -
* processing: 
    * runs the operator on the operands
    * checks against the proposed answer
    * if the operator isn't + or -, default to +
* output:     
    * returns true if the answer matches the actual result of the calculation
      ...returns false otherwise

Example usage and output:

answer1 = check_answer(1, 2, 3, "+")
print(answer1)
answer2 = check_answer(1, 2, -1, "-")
print(answer2)
answer3 = check_answer(9, 5, 3, "+")
print(answer3)
answer4 = check_answer(8, 2, 4, "-")
print(answer4)
answer3 = check_answer(9, 5, 3, "*")
print(answer3)

True
True
False
False
False

Part 4 - Clean Up
-----
Clean up your finished file by doing the following:

* once you're certain that your functions are working the way you expect... 
* COMMENT OUT ALL OF YOUR TEST CODE! (so that running your file does not
  produce any output - we'll see better ways of doing this later)   
* ensure that your file and functions are all named properly
* add comments to your file (including your name, section and date at the 
  beginning)

This will prep the file for the next file in the homework, feeling_quizzy.py,
and it will help with grading. 

Extra Credit
-----

1 point - move your test code so that it runs when you run the file, but
not when you import this as a module (relevant for feeling_quizzy.py)
* at the end of this file... add:

# this means... if this file is the actual file being run...
if __name__ == '__main__':

* ... within that if statement, add all of your test code
* when you run the file (funcynum.py), your test code will run
* however, if you import this as a module in another file, your test 
  code will not run

2 points - implement multiplication 
* add the multiplication sign (can be something that resembles an X or *)
* you have artistic discretion for this - you can make an X anywhere you want
* amend your check_answer so that '*' doesn't cause addition, but instead
  checks for multiplication

"""
def horizontal_line(char, width, offset):
    return offset * ' ' + char * width

def vertical_lines(char, height, offset, number, interior_offset):
    s = ''
    for row_num in range(height):
        row = offset * ' ' 
        for col_num in range(number):
            row += char 
            if col_num < number - 1:
                row += interior_offset * ' '
            elif col_num == number - 1 and row_num < height - 1: 
                row += '\n'
        s += row
    return s

def vertical_line(char, height, offset):
    return vertical_lines(char, height, offset, 1, 0)


def zero(char, width):
    s = horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 3, 0, 2, width - 2) + '\n'
    s += horizontal_line(char, width, 0)
    return s

def one(char, width):
    return vertical_line(char, 5, width - 1)

def two(char, width):
    s = horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 1, width - 1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 1, 0) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    return s

def three(char, width):
    s = horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 1, width - 1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 1, width - 1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    return s

def four(char, width):
    s = vertical_lines(char, 2, 0, 2, width - 2) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 2, width - 1) + '\n'
    return s


def five(char, width):
    s = horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 1, 0) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 1, width - 1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    return s


def six(char, width):
    s = horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 1, 0) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 1, 0, 2, width - 2) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    return s



def seven(char, width):
    s = horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 4, width - 1) + '\n'
    return s


def eight(char, width):
    s = horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 1, 0, 2, width - 2) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 1, 0, 2, width - 2) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    return s


def nine(char, width):
    s = horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 1, 0, 2, width - 2) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 2, width - 1) + '\n'
    return s


def plus(char, width):
    s = vertical_line(char, 2, width - width // 2 - 1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 2, width - width // 2 - 1) + '\n'
    return s


def minus(char, width):
    return '\n' * 2 + horizontal_line(char, width, 0) + '\n' * 2

def check_answer(left_operand, right_operand, answer, operator):
    if operator == '-':
        return (left_operand - right_operand) == answer
    else:
        return (left_operand + right_operand) == answer

if __name__ == '__main__':
    print(horizontal_line('*', 5, 0))
    print(horizontal_line('x', 2, 4))
    print(vertical_line('*', 2, 5))
    print(vertical_lines('+', 4, 0, 5, 3))

    print(zero('*', 5))
    print()
    print(one('*', 5))
    print()
    print(two('*', 5))
    print()
    print(three('*', 5))
    print()
    print(four('*', 5))
    print()
    print(five('*', 5))
    print()
    print(six('*', 5))
    print()
    print(seven('*', 5))
    print()
    print(eight('*', 5))
    print()
    print(nine('*', 5))
    print()
    print(plus('*', 5))
    print()
    print(minus('*', 5))
    
    answer1 = check_answer(1, 2, 3, "+")
    print(answer1)
    answer2 = check_answer(1, 2, -1, "-")
    print(answer2)
    answer3 = check_answer(9, 5, 3, "+")
    print(answer3)
    answer4 = check_answer(8, 2, 4, "-")
    print(answer4)
    answer3 = check_answer(9, 5, 3, "*")
    print(answer3)

    print(one('*', 5))
    one('X', 3)
    print( one('$', 0))

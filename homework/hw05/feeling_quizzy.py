"""
feeling_quizzy.py (9 points)
=====
Use the functions from your file, funcynum, to create a math quiz.

* save this file, feeling_quizzy.py IN THE SAME DIRECTORY AS funcynum.py
* at the very top of this file, import your functions from funcynum.py by:

import funcynum

* now you can use your functions by prefixing with your module name (just
  like using random.randint(a, b) or math.sqrt(25):

funcynum.two('*', 5)

Your math quiz program will ask for some parameters to the game... and then
it will display a series of addition and subtractions questions using your
library of print_xxxxxx functions from funcynum.py. It will ask for an answer
and check that answer using your check_answer function from funcynum.py. At
the end, it will show the percentage of correct answers.

* make sure that you've imported funcynum
* ask for how many quiz problems: 'How many problems?'
    * if the number of problems is not between 3 and 20 inclusive...
    * say: 'Please enter a number between 5 and 20...', and ask again
* ask for a character to use for the game: 'What character do you want the 
  numbers to be made of?'
    * if the character is composed of more than one character, say: 'Please 
      enter a single character!', and ask again
* finally, ask for the width of each number...
    * default to 3 if the width entered is less than 3 by saying: 'Oops... 
      defaulting to width 3'
* to ask addition and subtraction questions...
    * generate two random numbers for each operand
    * generate a random operation, either addition or subtraction
    * print out the problem using your print_xxxxxx functions
    * ask the user for an answer
    * check if the answer is correct
        * if it's not correct, print out the correct answer
        * if it is correct, print out 'Correct!'
* display the percent correct (formatted 2 decimal places) and how many they
  answered correctly out of the total number of questions

An example game is below. Note the validation that occurs for the number of
problems and the characters...
      
How many problems?
> 2
Please enter a number between 5 and 20...
How many problems?
> 3
What character do you want the numbers to be made of?
> ccc
Please enter a single character!
What character do you want the numbers to be made of?
> X
How wide do you want each number to be?
> 3

 What is ...
XXX
X X
XXX
  X
  X

 X
 X
XXX
 X
 X

  X
  X
  X
  X
  X
 = 10
Correct!

 What is ...
XXX
  X
XXX
  X
XXX



XXX



XXX
X X
XXX
  X
  X
 = -6
Correct!

 What is ...
XXX
X
XXX
  X
XXX

 X
 X
XXX
 X
 X

XXX
X X
XXX
  X
  X
 = 10
Nope, the answer is 14
You got  66.67% correct (2 out of 3)
"""
import funcynum_ret as funcynum
import random
num_problems = int(input('How many problems?\n> '))
while num_problems < 3 or num_problems > 20:
    print('Please enter a number between 5 and 20...')
    num_problems = int(input('How many problems?\n> '))
char = input('What character do you want the numbers to be made of?\n> ')
while len(char) != 1:
    print('Please enter a single character!') 
    char = input('What character do you want the numbers to be made of?\n> ')
width = int(input('How wide do you want each number to be?\n> '))
if width < 3:
    print('Oops... defaulting to width 3')
    width = 3

def print_num(n, char, width):
    if n == 0:
        print(funcynum.zero(char, width))
    elif n == 1:
        print(funcynum.one(char, width))
    elif n == 2:
        print(funcynum.two(char, width))
    elif n == 3:
        print(funcynum.three(char, width))
    elif n == 4:
        print(funcynum.four(char, width))
    elif n == 5:
        print(funcynum.five(char, width))
    elif n == 6:
        print(funcynum.six(char, width))
    elif n == 7:
        print(funcynum.seven(char, width))
    elif n == 8:
        print(funcynum.eight(char, width))
    elif n == 9:
        print(funcynum.nine(char, width))

def print_op(op, char, width):
    if op == '+':
        print(funcynum.plus(char, width))
    elif op == '-':
        print(funcynum.minus(char, width))

num_correct = 0
for i in range(num_problems):
    left_operand, right_operand = random.randint(0, 9), random.randint(0, 9)
    operator = '+' if random.randint(0, 1) == 0 else '-'
    if operator == '+':
        answer = left_operand + right_operand
    else:
        answer = left_operand - right_operand
    print(left_operand, operator, right_operand)
    print('\n What is ...')
    print_num(left_operand, char, width)
    print()
    print_op(operator, char, width)
    print()
    print_num(right_operand, char, width)
    user_answer = int(input(' = '))
    if user_answer == answer:
        print('Correct!')
        num_correct += 1
    else:
        print('Nope, the answer is', answer)
print('You got ', format(num_correct / num_problems, '.2%'), 'correct (%s out of %s)' % (num_correct, num_problems))


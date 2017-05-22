"""
The format Function
=====
The format function takes a value and turns it into a string based on some 
specified "format". The format function takes two arguments:

1. a value (of any type)
2. a "format specifier" (a string)

It ALWAYS returns a string.

The 2nd argument, the format specifier allows you to specify how the value
will be formatted, by using the following attributes (there are than these,
but these are the attributes we covered in class):

* type (can be d for digit, f for floating, % for percent, s for string)
* precision (dot followed by number of places, like .2)
* comma (a single comma: ,)
* width (an integer specify the __total__ width of the string returned)
* alignment (< for left aligned, > for right aligned, ^ for center aligned)

The format specifier is _actually_ just a string, but the string has a very
specific syntax for the characters that it contains. An abbreviated version 
of the syntax is as follows:

[alignment][width][,][.precision][type]

The complete version can be found here: 
https://docs.python.org/3/library/string.html#format-specification-mini-language

See the examples below for using the format function:
"""

# note that the return value of format is just a string!
print(type(format(7, 'd')))

# so you can use the result of format directly as a string argument to another
# function
print(format(7, 'd'))

# type can be d for digit (that is, a whole number)
# (note that the type of 42 is int, and d specifies digit)
s = format(42, 'd')
print(s)

# add a comma before d if you want commas in your output:
s = format(42000, ',d')
print(s)

# if the value's type in the 1st argument doesn't match the type specified by
# the second argument, you'll get an error!  ...note that the 1st argument
# is a string, and the 2nd argument says that it should be formatted as a
# digit (uncomment the lines below to see an error)
#s = format('42', 'd')
#print(s)

# type can be f for floating point number
s = format(42, 'f')
print(s)

# you can specify the number of decimal places for a floating point number by 
# appending a dot and a number to f -- the following format specifier has 2
# decimal places
s = format(42, '.2f')
print(s)

# if the type you specfiy is %, then the number is multiplied by 100 and a 
# percent sign is added
s = format(0.09, '%')
print(s)

# you can still specify the number of decimal places for a % by using dot
# (just like floating point numbers)
s = format(0.09, '.1%')
print(s)

# now combining commas, dots and floating point numbers
# (just like floating point numbers)
s = format(1234.5, ',.2f')
print(s)

# the last type is s, which means that you're just formatting as a  string:
s = format('a string', 's')
print(s)

# of course, the above example doesn't seem so useful until...
# you specify a width, which is the _WIDTH OF THE ENTIRE RESULTING STRING_
# (the string below is 30 characters wide)
s = format('a string', '30s')
print(s)
print('s is', len(s))

# now combining width with comma and digit...
# (just like floating point numbers)
s = format(2016, '30,d')
print(s)

# and... width with a floating point set to two decimal places
s = format(3.14159, '15.2f')
print(s)

# you can also control alignment by using < (left) or > (right)
left_aligned = format(3.14159, '<20.4f')
right_aligned = format(3.14159, '>20.4f')
print(left_aligned)
print(right_aligned)

# again, the second argument is a string, so it can just be a variable name
# that has a string value...
my_format = '15.2f'
s = format(3.14159, '15.2f')
print(s)

# which leads us to this program, where a user can control alignment
align = input('do you want to align output to the (l)eft or to the (r)ight?\n>')
custom_format = '20s'
if(align == 'l'):
    custom_format = '<' + custom_format
elif(align == 'r'):
    custom_format = '>' + custom_format
print('\nnotice that the output is 20 characters:')
print('=' * 20)
print(format('hello world', custom_format))

"""
String Concatentation vs the % Operator

First: a discussion about operators. Operators are programming language
constructs that allow a programmer to combine values. Some example of
operators include: //, -, **, etc.

Two commonly used string operators are:

* concatenation: + (operands must both be strings)
* repetition: * (one operand must be an int, the other must be a string)

__BOTH OPERATORS, + AND *, RESULT IN STRINGS!__

If the types do not follow the operator's specifications, then an error 
occurs. For example:

"hello" + 5
"300" * "bye"

One other operator is the percent operator, %:

* the left operand must be a string (with "placeholders")
* the right operand is, within parentheses, a comma separated list of values
* it always evaluates a string
* the string that results from the % operator is the result of:
    * substituting all of the placeholders...
    * with the values on the left
    * a common sequence to signify a placeholder in a string is %s
    * so... the string, "Hello %s, how are you" ...
    * would have the %s replaced with a value
    * there can be more than one %s
    * with each %s substituted by values based on position
    * (the 1st %s is replaced by the 1st value on the right)
"""

# the % operator has a string on the left and a string and value(s) on the 
# right... and it always returns a string
result = 'Hello %s' % ('World')
print(result)
print(type(result))

# you could even use the result of the percent operator directly in another
# function
print('Hello %s' % ('World'))

# you can have multiple values, which are placed positionally
result = 'Hello %s, greetings from %s' % ('World', 'Python')
print(result)

# why would you use the percent operator?
# consider using string concatenation
thing = 'World'
greeter = 'Python'
result = 'Hello ' + thing + ', greetings from ' + greeter
print(result)

# notice that in the above version, you must carefully place quotation 
# marks and plus symbols or else you'll get a syntax error!
# additionally, adding punctuation and spaces are awkward

# compare using the % operators again:
result = 'Hello %s, greetings from %s' % (thing, greeter)
print(result)


"""
if statements
=====

This section will go over:

1. logical operators
    * joining comparisons with logical operators
    * and vs or
2. using multiple if statements vs. using if, elif, else
"""

# consider the situation where:
# you want to continually ask the user if they would like
# the program to stop asking a question...
#
# * if they don't answer either 'yes' or 'yeah'
# * then the program keeps on going
# * once they answer 'yes' or 'yeah', then the program
# * stops

# first, let's take a look at getting input:
answer = input('do you want me to stop asking this question?\n>')

# once we have the answer, we may be tempted to use a 
# boolean expression like:
# answer != 'yeah' or 'yes'
# however, there are multiple issues here!
# 1. the second operand of the or should a boolean value, but instead,
#    it is a string!
#    to fix it, use the full comparison:
#
#    answer != 'yeah' or answer != 'yes'
#
#    this is because when a value is used in a boolean context, but it
#    isn't actually a boolean type, python converts the value for you!
#    * any non-empty string is converted to True
#    * any non-zero number is converted to True
#    * an empty string ("") or zero (0) is converted to False
#
# 2. next, the conditional should be changed to either:
#
#    answer != 'yeah' and answer != 'yes'
#    not (answer != 'yeah' or answer != 'yes')
#
#    ...using or alone would make an infinite loop (try running through
#    the possible results of plugging in 'yeah', 'yes' ... and see that
#    neither results in False, which is what we want
#
# 3. putting it all together:

while answer != 'yeah' and answer != 'yes':
    answer = input('do you want me to stop asking this question?\n>')
     
# next, let's examine using consecutive if statements using the example
# from the slides:
# Write a program that translate an athlete's finishing placement 
# (1st, 2nd and 3rd) into its Olympic medal value: 
# * first, ask the user for the finishing placement
# * based on that number, print out the correct medal:
#   * gold for 1
#   * silver for 2
#   * bronze for 3
#   * and anything else means no medal 
# for example:
#
# What number should I translate into a medal?
# >2
# silver
#
# What number should I translate into a medal?
# >23
# no medal for you!


# first let's try using consecutive __IF STATEMENTS ONLY__ ...
# try running the program and entering 2; it will not work as expected!
place = int(input('What number should I translate into a medal?\n>'))
if place == 1:
    print("gold")
if place == 2:
    print("silver")
if place == 3:
    print("bronze")
else:
    print("no medal for you!")

# this is because each if statement is independent from each other
# in the code above, the else is only paired with the last if, and all of 
# the other ifs can run on their own. to fix this, use else if instead
# ... so that only one branch will be run, rather than potentially all!
place = int(input('What number should I translate into a medal?\n>'))
if place == 1:
    print("gold")
elif place == 2:
    print("silver")
elif place == 3:
    print("bronze")
else:
    print("no medal for you!")

"""
accumulators
=====
some basic / intermediate examples of:

1. accumulating into a number
2. accumulating into a string
3. accumulating with user input
"""
# sum of numbers 1 through 10 using for
total = 0
for num in range(1, 11):
    total += num
print(total)

# sum of numbers 1 through 10 using while
total = 0
num = 1
while num < 11:
    total += num
    num += 1
print(total)

# note that the for loop version is a little bit easier since you only need
# a single accumulator, total... and num is simply the loop variable. on the
# other hand, the while loop requires num to be accumulated.
#
# also note that the number of iterations of both can be controlled simply
# by making: (a) the 2nd argument in for a variable or (b) making the 11 in 
# num < 11 a variable

# accumulating into an empty string to build a "square" of x's:
# (this can be done with string repetition, without a loop, too)
# note the new line at the end of each line... this is simply making the 
# following square:
#
# xxxxx
# xxxxx
# xxxxx
# xxxxx
#
# which as a string is: "xxxxx\nxxxxx\nxxxxx\nxxxxx\nxxxxx"
s = ''
for i in range(5):
    s += 'x' * 5 + '\n'
print(s) 

# finally, accumulation and input together for building a string
# this program simply asks the user for words, which are put together to make
# a sentence. once the user's word is stop in all uppercase, the program will
# stop asking for words:
#
# word please
# > hello
# word please
# > world
# word please
# > STOP
# hello world

word = ''
sentence = ''
while word != 'STOP':
    if word != '':             # prevent empty string from adding a space
        sentence += word + ' ' # add the word and a space
    word = input('word plz\n> ')
print(sentence)

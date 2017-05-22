"""
4. Write a FUNCTION called “valid_n_number” that determines if a NYU Student ID is valid.  For the purpose of this question a valid NYU Student ID is defined as follows:

•       exactly 9 characters long (including leading 'N')
•       begins with the uppercase character ‘N’
•       all characters beside the beginning ‘N’ character must be numbers

Your function should accept a test “N number” as an ARGUMENT (String) and RETURN a status value (Boolean).  Here’s a sample program that uses your function:

test1 = valid_n_number("N123")
test2 = valid_n_number("N1234567890")
test3 = valid_n_number("P12345678")
test4 = valid_n_number("NXYZ!5678")
test5 = valid_n_number("N12345678")

print (test1, test2, test3, test4, test5) 
False False False False True

And here’s the expected output:

assume that it's valid
check if it's 9 characters, and if it isn't, it's not valid
check if begins with the uppercase character ‘N’, if it doesn't, it's not valid
check that all characters beside the beginning ‘N’ character must be numbers, if not, not valid
give back validity...
"""



"""
test1 = valid_n_number("N123")
test2 = valid_n_number("N1234567890")
test3 = valid_n_number("P12345678")
test4 = valid_n_number("NXYZ!5678")
test5 = valid_n_number("N12345678")
"""


"""
5. Write a program that asks the user to enter in 5 NYU Student ID numbers.  Ensure that the ID numbers that the user enters are valid (use your function from question #4) and that they do not enter duplicate IDs.  Let the user know if they make a mistake. When you have collected 5 IDs print them out in ascending order.  Here’s a sample running of this program.  Note that shaded items represent data that the user has typed into the program:

Enter a N Number: N12345678
Enter a N Number: N123
Invalid N Number
Enter a N Number: P12345678
Invalid N Number
Enter a N Number: N12345678
Duplicate N Number
Enter a N Number: N00000003
Enter a N Number: N00000001
Enter a N Number: N00000002
Enter a N Number: N00000000

Your N-Numbers:

N00000000
N00000001
N00000002
N00000003
N12345678


"keep track of stuff"... we need a variable (or variables)

# create a list of n-numbers (start it off as empty)
# continually ask for an n number until there are 5 valid ones
#   when user gives input...
#   check if it's valid (if it isn't display an error)
#   check if we already have it (if it isn't display an error)
#   if it's valid, and it's unique (we don't have it yet), save it
# output the n numbers in order
"""
def valid_n_number(n_number):
    return len(n_number) == 9 and n_number[0] == 'N' and n_number[1:].isdigit()

n_numbers = []
while len(n_numbers) < 5:
    test_number = input('Enter an N-Number')
    if not valid_n_number(test_number):
        print('not a valid n number')
    elif test_number in n_numbers:
        print('duplicate')
    else:
        n_numbers.append(test_number)

n_numbers.sort()
for n in n_numbers:
    print(n)

















colors = ['Red', 'Green', 'Blue', 'Yellow', 'Pink']

i = 0
while i < len(colors):
    print (i, colors[i])
    i += 2

"""
# 0, 2, 4
for i in range(0,len(colors), 2):
    print (i, colors[i])
"""

"""
0 Red
2 Blue
4 Pink
"""

lyrics = "like Baby baby baby ohhh Baby baby Like nooo"

"""output: like baby ohhh nooo"""















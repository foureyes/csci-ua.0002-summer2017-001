"""
newton's
multiplication table
decimal to binary - iterative
decimal to binary - remainder
number triangle
approximate pi
approximate pi
reduce fraction
days in mo
reduce 
"""
def mult_table(n):
    cell_width = len(str(n * n)) + 1
    table = ''
    for row_num in range(1, n + 1):
        row = ''
        for col_num in range(1, n + 1):
            row += format(row_num * col_num, '>%s' % cell_width) 
        table += row + '\n'
    return table

print(mult_table(7))




import math
def distance(x1, x2, y1, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d

def dec_to_bin_1(n):
    bin_num = ''
    max_exp = 7
    for exp in range(max_exp, -1, -1):
        place = 2 ** exp
        if place <= n:
            n -= place
            bin_num += '1'
        else:
            bin_num += '0'

    return bin_num

        

def dec_to_bin_2(n):
    dividend = n
    divisor = 2
    bin_num = ''
    for i in range(8):
        quotient = dividend // divisor
        remainder = dividend % divisor
        dividend = quotient
        bin_num = str(remainder) + bin_num
    return bin_num
"""
for i in range(256):
    print('%s: %s, %s' % (i, dec_to_bin_1(i), dec_to_bin_2(i)))
"""

def newtons(n):
    threshold = 0.01
    guess = n
    new_guess = n / 2
    while abs(new_guess - guess) > threshold:
        print(guess, new_guess)
        guess = new_guess
        new_guess = 0.5 * (guess + n / guess)
    return new_guess

print(newtons(9))
print(newtons(16))
print(newtons(5))




def gcd(a, b):
    smaller = a
    if smaller > b:
        smaller = b
    gcd = 1
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    return gcd

print(gcd(9, 12))
print(gcd(12, 9))
print(gcd(17, 15))

def reduce(numerator, denominator):
    div = gcd(numerator, denominator)
    return '%s/%s' % (numerator // div, denominator // div)

print(reduce(10, 15))
print(reduce(100, 12))
print(reduce(17, 12))

n = int(input('give me the numerator'))
d = int(input('give me the denominator'))

print(reduce(n, d))


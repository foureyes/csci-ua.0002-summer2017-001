"""
a_little_dicey.py
"""
import random
comp_total, play_total = 0, 0
play_to = int(input('Play to?\n> '))
if play_to < 20:
    print('It\'s not even worth playing to %s!' % ( play_to))

turn = input('Who goes first?\n> ')
while turn != 'p' or turn != 'c':
    print('Please enter p or c...')
    turn = input('Who goes first?\n> ')

while comp_total <= play_to and play_total <= 20:
    if turn == 'p':
        num_rolls = int(input('How many dice do you want to roll?\n> '))
        if num_rolls >= 1 and num_rolls <= 3:
            for i in range()
        else:
            print('Please enter a number between one and three')

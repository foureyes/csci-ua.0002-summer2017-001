"""
for loops are count controlled
what's a range object... what does it represent
it's a arithmetic sequence numbers... 

* 1, 2, 3, 4
* 2, 4, 6, 8
* 3, 2, 1, 0
range(3, -1, -1)

To create a range object, use the function range
* range(a) - counts from 0 up to, but not including a
* range(a, b) - counts from a upt to, but not including b
* range(a, b, c) - same as above ...buuuuuuuuuut, c is the step
"""
# ask for how many trials
# roll a six sided die and count how many times a 1 is rolled
# roll it <number of trials> times
# print out how many times 1 is rolled


"""
how many trials? 3
roll1: 6
roll2: 1
roll3: 1
2
import random
roll_number = int(input('how many trials? > '))
count = 0
for n in range(1, roll_number + 1):
    roll = random.randint(1, 6)
    print('roll' + str(n + 1) +  ': ' +  str(roll))
    if roll == 1:
        count += 1
print(count)
--------------------
adding step 1
adding step 2

=======
|     |
=======
|     |
=======
|     |
=~  ~==
|     |
=======
|     |
import random
height = int(input('how tall do you want ur ladder 2 b? > '))
step = "======="
rung = "|     |"
broken_step = "=~  ~=="
ladder = ""
for i in range(height):
    print('adding step', i + 1)
    broken = random.randint(1, 3)
    if broken == 1:
        ladder += broken_step + "\n"
    else:
        ladder += step + "\n"
    ladder += rung + "\n"

print(ladder)
"""
"""
import random
odds_score
evens_score
while no one has reached 2 points
    odds player and evens player both put out 1 or 2
    odds_play
    evens_play
"""
import random

odds_score = 0
evens_score = 0

while odds_score < 2 and evens_score < 2:
    odds_play = random.randint(1, 2)
    evens_play = random.randint(1, 2)
    total = odds_play + evens_play
    if total % 2 == 0:
        evens_score += 1
    else:
        odds_score += 1
    print('odds:', odds_play, 'evens:', evens_play)
    print('total', total)
    print('odds score:', odds_score, 'evens score:', evens_score)














































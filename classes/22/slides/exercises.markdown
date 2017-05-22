---
layout: slides
title: About Class #22 
---
<section markdown="block">
# Let's Try Implementing Rock Paper Scissors!
</section>

<section markdown="block">
### Create a Function That Determines "Who" Won

* rock, paper, and scissors will be represented by r, p, and s
* the function should take two arguments, one "hand" from player one, the other from player two
* it should return the number of who won
* it should return None for ties
</section>

<section markdown="block">
### Outcome
{% highlight python %}
def outcome(hand_one, hand_two):
	if hand_one == hand_two:
		return None
	if hand_one == 'r' and hand_two == 's' or hand_one == 'p' and hand_two =='r' or hand_one == 's' and hand_two == 'p':
		return 1
	else:
		return 2
{% endhighlight %}
</section>

<section markdown="block">
### Example Output of Game
{% highlight python %}
(r)ock, (p)aper, (s)cissors or (q)uit
>r
PLAY: player: r, computer: r
tie
SCORE: player: 0, computer: 0
(r)ock, (p)aper, (s)cissors or (q)uit
>p
PLAY: player: p, computer: r
player wins
SCORE: player: 1, computer: 0
(r)ock, (p)aper, (s)cissors or (q)uit
>q
{% endhighlight %}
</section>

<section markdown="block">
### Game
{% highlight python %}
import random
hands = ['r', 'p', 's']
command = ''
player_score = 0
computer_score = 0
while command != 'q':
	command = input("(r)ock, (p)aper, (s)cissors or (q)uit\n>")
	if command == 'q':
		break
	elif command in hands:
		computer_move = random.choice(hands)
		winner = outcome(command, computer_move)
		print("PLAY: player: %s, computer: %s" % (command, computer_move)) 
		if winner == 1:
			print("player wins")
			player_score += 1
		elif winner == 2:
			print("computer wins")
			computer_score += 1
		else:
			print("tie")
			# tie
		print("SCORE: player: %s, computer: %s" % (player_score, computer_score)) 
	else:
		print("I don't know that command")	
{% endhighlight %}
</section>


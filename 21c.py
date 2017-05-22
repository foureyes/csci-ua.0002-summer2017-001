"""
create a function that generates a deck of cards
[['suit', 'value']]
[['clubs', 'A'], ['clubs', '2']]
52 cards
4 - suits, clubs, hearts, diamonds, spades (as strings)
2 - 10, A, J, Q, K (as strings)

generate_deck()
return a new list of lists...
"""
"""
# create two lists, 
# 1st contains all possible suits
# 2nd contains all possible values
# create a list to contain the deck of cards
# loop over all suits
# for every suit
# loop over all values
# add the suit/value pair as a list into the new list
"""
import random
def generate_deck():
    suits = ['clubs', 'diamonds', 'spades', 'hearts']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []
    for s in suits:
        for v in values:
            #           |---------- list literal to combine suit and value
            deck.append([s, v])
            """ combines suits and values into a single list"""
            """ add that to our deck """

    return deck

deck = generate_deck()
for i in range(100):
    i1 = random.randint(0, len(deck) - 1)
    i2 = random.randint(0, len(deck) - 1)
    deck[i1], deck[i2] = deck[i2], deck[i1]

player_hand = []
computer_hand = []
for i in range(2):
    player_hand.append(deck.pop())
print(player_hand)

value = 0
for card in player_hand:
    value += int(card[1])
print(value)

















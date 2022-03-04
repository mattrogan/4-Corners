from card import Card
from random import shuffle

deck = []
for i in range(4):
    suit = i + 1

    for j in range(13):
        value = j + 1

        deck.append(Card(suit, value))

shuffle(deck)
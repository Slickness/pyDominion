#! /usr/bin/python3.8
import random

class Card():
    def __init__(self, name, kind, cost = 0, value = 0):
        self.cost = cost
        self.name = name
        self.kind = kind
        self.value = value


class Deck():
    def __init__(self):
        self.deck = []
    
    def add(self, card):
        if isinstance(card, Card):
            self.deck.append(card)

    def drawCard(self):
        return self.deck.pop(0)
    
    def shuffle(self):
        random.shuffle(self.deck)

    def remove(self,card):
        self.deck.remove(card)


# setting up each type of card
# Treasue
copper = Card("Copper", "T", 0, 1)
silver = Card("Silver", "T", 3, 2)
gold = Card("Gold", "T", 6, 3)
# Victory
estate = Card("Estate", "V", 2, 1)
duchy = Card("Duchy", "V", 5, 3)
province = Card("Provice", "V", 8, 6)
curse = Card("curse", "V", 0, -1)
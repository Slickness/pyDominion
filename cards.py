#! /usr/bin/python3.8
import random

class Card():
    def __init__(self, cost):
        self.cost = cost

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


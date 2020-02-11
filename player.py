#! /usr/bin/python3.8
from cards import Deck, Card

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = Deck()
        self.pile = Deck()
        self.discard = Deck()

    def endTurn(self):
        for card in reversed(self.hand.deck):
            self.discard.add(card)
            self.hand.remove(card)

    def emptyDiscard(self):
        for card in reversed(self.discard.deck):
            self.pile.add(card)
            self.discard.remove(card)
        self.pile.shuffle()

    def drawCardPile(self):
        if len(self.pile.deck) == 0:
            self.emptyDiscard()
        self.hand.add(self.pile.drawCard())

    def drawHand(self):
        '''since you start with 10 cards you should never have less than 5 cards'''
        for x in range(5):
            if len(self.pile.deck) == 0:
                self.emptyDiscard()
            self.drawCardPile(self)

test = Player("randy")

print (test.drawHand())
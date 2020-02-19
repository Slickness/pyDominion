#! /usr/bin/python3.8
from cards import Deck, Card
import cards
import copy

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = Deck()
        self.pile = Deck()
        self.money = 0
        self.discard = Deck()
        self.startDeck()
        self.drawHand()
        self.actions = 1
        self.buys  = 1

    def endTurn(self):
        for card in reversed(self.hand.deck):
            self.discard.add(card)
            self.hand.remove(card)
        self.drawHand()
        self.actions = 1
        self.buys  = 1
        self.money = 0

    def emptyDiscard(self):
        for card in reversed(self.discard.deck):
            self.pile.add(card)
            self.discard.remove(card)
        self.pile.shuffle()

    def drawCardPile(self):
        if len(self.pile.deck) == 0:
            self.emptyDiscard()
        self.hand.add(self.pile.drawCard())

    def addMoney(self, value):
        self.money = self.money + value

    def drawHand(self):
        '''since you start with 10 cards you should never have less than 5 cards'''
        for _x in range(5):
            if len(self.pile.deck) == 0:
                self.emptyDiscard()
            self.drawCardPile()
        for card in self.hand.deck:
            if card.kind == "T":
                self.addMoney(card.value)
                
    
    def startDeck(self):

        '''Each player will start with 7 copper and 3 estates '''
        for _x in range(7):
            self.pile.add(copy.deepcopy(cards.copper))
        for _x in range(3):
            self.pile.add(copy.deepcopy(cards.estate))
        self.pile.shuffle()
    
    def finalScore(self):
        score = 0
        decks = [self.pile.deck, self.discard.deck, self.hand.deck]
        for pile in decks:
            for card in pile:
                if card.kind == "V":
                    if card.name == "Gardens":
                        score += int((self.pile.size + self.discard.size + self.hand.size)/10)
                    else:
                        score += card.value

        return score
# testing out the player cll


test = Player("randy")

for card in test.hand.deck:
    print (card.name)
<<<<<<< HEAD
print (test.finalScore())
=======
print (test.money)
>>>>>>> d32d16ce270302f928d1ea9795a5f84fbe947f17

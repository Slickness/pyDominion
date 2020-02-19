#! /usr/bin/python3.8
import random

class Card():
<<<<<<< HEAD
    def __init__(self, name, kind, cost = 0, value = 0, action = {}):
=======
    def __init__(self, name, kind, cost = 0, value = 0):
>>>>>>> d32d16ce270302f928d1ea9795a5f84fbe947f17
        self.cost = cost
        self.name = name
        self.kind = kind
        self.value = value
<<<<<<< HEAD
        self.action = action
=======
>>>>>>> d32d16ce270302f928d1ea9795a5f84fbe947f17


class Deck():
    def __init__(self):
        self.deck = []
<<<<<<< HEAD
        self.size = len(self.deck)
=======
>>>>>>> d32d16ce270302f928d1ea9795a5f84fbe947f17
    
    def add(self, card):
        if isinstance(card, Card):
            self.deck.append(card)

    def drawCard(self):
<<<<<<< HEAD
        return self.deck.pop(-1)
=======
        return self.deck.pop(0)
>>>>>>> d32d16ce270302f928d1ea9795a5f84fbe947f17
    
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
<<<<<<< HEAD
curse = Card("curse", "V", 0, -1)

decks = [
    Card("Gardens", "V", 4, 1),
    Card("Removel", "A", 4, 0, {"Trash",("up", 2)} ),
    Card("MoneyLender", "A", 4, 0 ,{"TrashC": 3}),
    Card("Moat", "A", 2, 0, {"cards": 2, "reaction": True}),
    Card("Mine", "A", 5, 0, {"TrashT": 3}),
    Card("Militia", "A", 4, 0 , {"Treasure": 2, "PlayersCards": 3}), # down to 
    Card("Market", "A", 5, 0, {"cards": 1, "Action": 1, "Buy": 1, "Treasure": 1}),
    Card("Library", "A", 5, 0, {"Draw": 7}), #up to, can discard actions in process
    Card("Laboratory", "A", 5, 0, {"cards": 2, "Action": 1}),
    Card("Festival", "A", 5, 0, {"Action": 2, "Buy": 1, "Treasure": 2}),
    Card("Feast", "A", 4, 0, {"TrashThis": 5}), # gain card up to 5
    Card("Council Room", "A", 5, 0, {"Card": 4, "Buy": 1, "other": 1}), # each other player draws 1
    Card("Chape", "A", 2, 0, {"TrashCards": 4}), # trash up to 4 cards from your hand
    Card("Chancellor", "A", 3, 0, {"Treasure": 2, "deck": True}),
    Card("Cellar", "A", 2, 0, {"Action": 1, "Trade": True}),
    Card("Bureaucrat", "A", 4, 0, {"Gain", "Silver", "other", "Victory"}), # others reveal victory bakc to deck
    Card("Adventureer", "A", 6, 0, {"Reveal": 2}), # keep drawing untul 2 treasure cards discard rest
    Card("Smitty", "A", 4, 0, {"cards": 3}),
    Card("Spy", "A", 4, 0, {"cards": 1, "Action": 1, "show": True}), # each play shows top card of deck can discard
    Card("Thief", "A", 4, 0, {"Top2": True, }), # each player reveals top two cards trash one if treasure can take
    Card("Throne Room", "A", 4, 0 ,{"ChooseAaction": 2}),
    Card("Village", "A", 3, 0, {"cards": 1, "Action": 2}),
    Card("Witch", "A", 5, 0, {"cards": 2, "Curse": 1}),
    Card("WoodCutter", "A", 3, 0, {"Buy": 1, "Treasure": 2}),
    Card("Workshop", "A", 3, 0, {"Gain": 4}),
]

=======
curse = Card("curse", "V", 0, -1)
>>>>>>> d32d16ce270302f928d1ea9795a5f84fbe947f17

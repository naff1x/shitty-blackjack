# -*- coding: utf-8 -*-

class Deck:
    import random


    def __init__(self):
        self.newDeck = 52*[None]

        position = 0
        suits = ["hearts", "spades", "diamonds", "clubs"]
        for rank in range (13):
            for suit in suits:
                self.newDeck[position] = Card(rank+2, suit)
                position += 1


    def getDeck(self):
        return self.newDeck


    def shuffleDeck(self):
        self.random.shuffle(self.newDeck)
        print("Deck shuffled!")


    def printDeck(self):
        for i in range(len(self.newDeck)):
            print("Position: " + str(i) + " // Rank: " + str(self.newDeck[i].rank) + " // Suit: " + str(self.newDeck[i].suit))

class Card:


    def __init__(self, inRank, inSuit):
        # "rank" meaning number or face and "suit" meaning clubs, diamonds etc.
        self.rank = inRank
        self.suit = inSuit


    def __repr__(self):
        return "Card rank: " + str(self.rank) + " // Card suit: " + self.suit

    def getValue(self):
        return self.rank

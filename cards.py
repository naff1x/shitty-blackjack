# -*- coding: utf-8 -*-

class Deck:
    import random


    def __init__(self):
        self.newDeck = 52*[None]

        position = 0
        for rank in range (13):
            for suit in range(4):
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

        if inRank == 11 or inRank == 12 or inRank == 13:  # Handles face cards (queen, king and jack)
            self.value = 10
        elif inRank == 14:  # Handles ace (this is a temporary solution as ace can be 1 and 11)
            self.value = 11
        else:
            self.value = inRank

        if inSuit == 0:
            self.suit = "clubs"
        elif inSuit == 1:
            self.suit = "diamonds"
        elif inSuit == 2:
            self.suit = "hearts"
        elif inSuit == 3:
            self.suit = "spades"


    def getValue(self):
        return self.value
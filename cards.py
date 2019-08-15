# -*- coding: utf-8 -*-
import pygame

class Deck:
    import random

    def __init__(self):
        self.deck = 52 * [None]

        position = 0
        suits = ["hearts", "spades", "diamonds", "clubs"]
        for rank in range (13):
            for suit in suits:
                self.deck[position] = Card(rank + 2, suit)
                position += 1

    def getDeck(self):
        return self.deck

    def shuffleDeck(self):
        self.random.shuffle(self.deck)
        print("Deck shuffled!")

    def printDeck(self):
        for i in range(len(self.deck)):
            print("Position: " + str(i) + " // Rank: " + str(self.deck[i].rank) + " // Suit: " + str(self.deck[i].suit))


class Card:

    def __init__(self, inRank, inSuit):
        # "rank" meaning number or face and "suit" meaning clubs, diamonds etc.
        self.rank = inRank
        self.suit = inSuit
        self.image_path = "images/cards/"+str(inRank)+"_"+inSuit+".png"
        self.visual = pygame.image.load(self.image_path).convert()

    def __repr__(self):
        return "Card rank: " + str(self.rank) + " // Card suit: " + self.suit

    def get_value(self):
        return self.rank

    def get_visual(self):
        return self.visual


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

    def getTopCard(self):
        item = self.deck[-1]
        self.deck.pop()  # "pop() removed last item in the list by default
        return item

    def printDeck(self):
        for i in range(len(self.deck)):
            print("Position: " + str(i) + " // Rank: " + str(self.deck[i].rank) + " // Suit: " + str(self.deck[i].suit))


class Card:

    def __init__(self, inRank, inSuit):
        # "rank" meaning number or face and "suit" meaning clubs, diamonds etc.
        self.rank = inRank
        self.suit = inSuit
        self.value = inRank
        self.image_path = "images/cards/"+str(inRank)+"_"+inSuit+".png"
        self.visual = pygame.transform.scale(pygame.image.load(self.image_path).convert(), (145, 200))

    def __repr__(self):
        return "Card rank: " + str(self.rank) + " // Card suit: " + self.suit

    def getValue(self):
        if 10 < self.rank < 14:
            return 10
        else:
            return self.value

    def getVisual(self):
        return self.visual

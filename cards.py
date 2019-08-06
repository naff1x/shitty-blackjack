# -*- coding: utf-8 -*-

class Deck:
    def __init__(self):
        newDeck = 52*[None]


        position = 0

        for rank in range (13):
            for suit in range(4):
                newDeck[position] = Card(rank+2, suit)
                position += 1

        #for i in range(len(newDeck)):
            #print(str(newDeck[i].rank) + " " + str(newDeck[i].suit))

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

        #print("Rank: "+ str(self.rank) + " Value: " + str(self.value) + " Suit: " + self.suit)

    def getValue(self, card):
        return self.value

Deck()
# -*- coding: utf-8 -*-

class Deck:
    def __init__(self):
        newDeck = 52*[None]

        for a in range(4):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(2, i)
        for a in range(4, 8):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(3, i)
        for a in range(8, 12):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(4, i)
        for a in range(12, 16):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(5, i)
        for a in range(16, 20):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(6, i)
        for a in range(20, 24):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(7, i)
        for a in range(24, 28):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(8, i)
        for a in range(28, 32):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(9, i)
        for a in range(32, 36):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(10, i)
        for a in range(36, 40):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(11, i)
        for a in range(40, 44):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(12, i)
        for a in range(44, 48):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(13, i)
        for a in range(48, 52):
            for i in range(4):
                print(a, i)
                newDeck[a] = Card(14, i)
        
        #for i in range(52):
            #print(newDeck[i].rank, newDeck[i].suit)

class Card:
    def __init__(self, rank, inputSuit):
        # "rank" meaning number or face and "suit" meaning clubs, diamonds etc.
        self.rank = rank
        if inputSuit == 0:
            self.suit = "clubs"
        elif inputSuit == 1:
            self.suit = "diamonds"
        elif inputSuit == 2:
            self.suit = "hearts"
        elif inputSuit == 3:
            self.suit = "spades"
        print("Rank: "+ str(self.rank) + " Suit: " + self.suit)

    def getValue(self, card):
        return self.rank

Deck()
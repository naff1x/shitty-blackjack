from cards import *

class Bank:
    def __init__(self):
        self.hand = Hand()

    def hit(self, card):
        if card.getValue() is 14:  # If the card is an ace...
            if self.getValue() + 11 > 21:  # If the ace's 11 would result in a loss...
                card.value = 1
            else:
                card.value = 11

        self.hand.addCard(card)

    def getValue(self):
        return self.hand.getValue()

class Player:
    def __init__(self):
        self.hand = Hand()
        self.money = 1000
        # insats

    def hit(self, card):
        if card.getValue() is 14:  # If the card is an ace...
            if self.getValue()+11 > 21:  # If the ace's 11 would result in a loss...
                card.value = 1
            else:
                card.value = 11

        self.hand.addCard(card)

    def getValue(self):
        return self.hand.getValue()

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getValue(self):
        sum = 0
        for c in self.cards:
            sum += c.getValue()
        return sum

    def __repr__(self):
      s = ""
      for c in self.cards:
         s += c.print() +", "
      return s

    def clearHand(self):
        self.cards.clear()


"""c = Card(1,"spades")
print(c)
print(c.getValue())
h = Hand()
h.addCard(c)
print(h.getValue())

p = Player()
p.hit(c)
print(p.getValue())
p.hit(c)
print(p.getValue())"""




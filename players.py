class Bank:
    def __init__(self):
        self.hand = Hand()

class Player:
    def __init__(self):
        self.hand = Hand()
        self.money = 1000;

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def value(self):
        sum = 0;
        for c in cards:
            sum += c.value()
        return sum


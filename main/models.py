from django.db import models


# Create your models here.
class Card:
    def __init__(self, value, suit):
        self.suit = suit
        if type(value) == str:
            if value == 'A':
                self.name = f'{value}_of_{suit}'
                self.rank = 1
            else:
                self.name = f'{value}_of_{suit}'
                self.rank = 10
        else:
            self.name = f'{value}_of_{suit}'
            self.rank = value

    def __repr__(self):
        return self.name


class Deck(models.Model):
    name = models.CharField(max_length=20)
    rank = models.IntegerField()
    suit = models.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate_deck():
        ranks = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K')
        suits = ('diamonds', 'clubs', 'hearts', 'spades')
        list_of_cards = [Card(i, j) for i in ranks for j in suits]
        [Deck.objects.create(name=i.name, rank=i.rank, suit=i.suit) for i in list_of_cards]
        # for i in list_of_cards:
        #     card = Deck(name=i.name, rank=i.rank, suit=i.suit)
        #     card.save()

# a = Card('A', 'diamonds')
# print(a.rank, a.name, a.suit)
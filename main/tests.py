from django.test import TestCase
import models


# Create your tests here

def test_card():
    ranks = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K')
    suits = ('diamonds', 'clubs', 'hearts', 'spades')
    list_of_cards = [models.Card(i, j) for i in ranks for j in suits]
    print(list_of_cards)


def test_card_2():
    a = models.Card('A', 'diamonds')
    print(a.name, a.rank, a.suit)

test_card_2()
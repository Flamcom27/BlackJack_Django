from django.db import models


# Create your models here.
class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        if rank == str:
            if rank == 'A':
                self.name = f'{rank}_of_{suit}'
                self.rank = (1, 11)
            else:
                self.name = f'{rank}_of_{suit}'
                self.rank = 10
        else:
            self.name = f'{rank}_of_{suit}'
            self.rank = rank

    def __repr__(self):
        return self.name


# class Deck(models.Model):
#     def generate_deck(self):
#         pass


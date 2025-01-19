import random
from modules.card import Card
from modules import planets
planet = ("Earth", "Jupiter", 'Mars','Neptune', 'Mercury','Saturn',)

class Shop_deck:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.shopcards = []
        self.create(self.number_of_decks)
        self.mano = []
        


    def create(self, number_of_decks):
        decks = [planets for name in planet for shop_cards in range(number_of_decks) ]
        self.shopcards.extend(decks)

    def shuffle(self):
        self.shopcards = random.sample(self.shopcards, len(self.shopcards))

    def draw_shop(self):
        if len(self.shopcards) == 0:
           self.create(self.number_of_decks) 
        drawn_card = self.shopcards[0] 
        self.shopcards.remove(self.shopcards[0])  
        print(len(self.shopcards))
        return drawn_card
    
    




    def reset(self):
        self.shopcards = []
        self.create(self.number_of_decks)

    @property
    def remaining(self):
        return len(self.shopcards)
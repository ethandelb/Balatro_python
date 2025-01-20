import random
from modules.card import Card
from modules import planets
planet = ("Earth", "Jupiter", 'Mars','Neptune', 'Mercury','Saturn','Uranus','Venus')

class Shop_deck:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.shopcards = []
        self.create(self.number_of_decks)
        self.mano = []
        


    def create(self, number_of_decks):
       for _ in range(number_of_decks):
            for name in planet:
                new_card = planets.Planet(name)
                self.shopcards.append(new_card)
    
    def shuffle(self):
        self.shopcards = random.sample(self.shopcards, len(self.shopcards))


    def draw_shop(self):
        if not self.shopcards:
            self.create(self.number_of_decks) 
        shop_drawn_card = self.shopcards[0] 
        self.shopcards.remove(self.shopcards[0])  
        print(len(self.shopcards))
        return self.shopcards.pop(0)
    
    




    def reset(self):
        self.shopcards = []
        self.create(self.number_of_decks)

    @property
    def remaining(self):
        return len(self.shopcards)
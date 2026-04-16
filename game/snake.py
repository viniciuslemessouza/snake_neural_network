from player import Player
from food import Food

class Game:
    def __init__(self):
        self.player = Player(0, 0)
        self.food = Food(0, 0)

    def generate_player_position(self):
        pass

    def generate_food_position(self):
        pass
from player import Player
from food import Food
from display import Display

class Game:
    def __init__(self):
        self.player = Player(0, 0)
        self.food = Food(0, 0)
        self.display = Display(1200, 800, 200)

    def generate_player_position(self):
        pass

    def generate_food_position(self):
        pass
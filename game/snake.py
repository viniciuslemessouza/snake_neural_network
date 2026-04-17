from player import Player
from food import Food
from display import Display

FPS = 30

class Game:
    def __init__(self):
        self.player = Player(0, 0)
        self.food = Food(0, 0)
        self.display = Display(1200, 800, 200)

    def generate_player_position(self):
        pass

    def generate_food_position(self):
        pass

    def play(self):
        while self.display.running:
            self.display.update()
            self.display.clock.tick(FPS)

if __name__ == "__main__":
    Game().play()
from player import Player
from food import Food
from display import Display

FPS = 10
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
HUD_WIDTH = 200

class Game:
    def __init__(self):
        self.player = Player(0, 0)
        self.food = Food(0, 0)
        self.display = Display(SCREEN_WIDTH, SCREEN_HEIGHT, HUD_WIDTH)
        self.set_positions()

    def set_positions(self):
        self.player.set_position(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.food.set_position(SCREEN_WIDTH, SCREEN_HEIGHT, self.player.body)

    def play(self):
        while self.display.running:
            self.update()
            self.display.clock.tick(FPS)

    def draw(self):
        self.display.surface.fill("black")
        self.display.draw(self.food)
        for rect in self.player.body:
            player = self.player
            player.rect = rect
            self.display.draw(self.player)

    def update(self):
        self.display.get_events(self.player)
        self.player.update()
        self.display.update()
        self.draw()

if __name__ == "__main__":
    Game().play()
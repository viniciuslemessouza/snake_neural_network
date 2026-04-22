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
        self.score = 0
        self.set_positions()

    def set_positions(self):
        self.player.set_position(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.food.set_position(SCREEN_WIDTH, SCREEN_HEIGHT, self.player.body)

    def play(self):
        while DISPLAY.running:
            self.update()
            self.check_collisions()
            self.draw()
            DISPLAY.clock.tick(FPS)

    def draw(self):
        DISPLAY.surface.fill("black")
        DISPLAY.draw(self.food)
        for rect in self.player.body:
            self.player.rect = rect
            DISPLAY.draw(self.player)
        self.display_info()

    def display_info(self):
        DISPLAY.plot_hud()
        DISPLAY.plot_text("Score", self.score, 0)
        DISPLAY.plot_text("Length", self.player.length, 1)
        DISPLAY.plot_text("Hunger", self.player.hunger, 2)
        DISPLAY.plot_text("Steps", self.player.steps, 3)

    def update(self):
        DISPLAY.get_events(self.player)
        self.player.update()
        DISPLAY.update()

    def check_collisions(self):
        if self.body_collision(self.player.rect) or self.wall_collision(self.player.x, self.player.y):
            self.over()
        if self.food_collision():
            self.got_food()

    def got_food(self):
        self.score += 1
        self.player.length += 1
        self.player.hunger = 0
        self.food.set_position(SCREEN_WIDTH, SCREEN_HEIGHT, self.player.body)

    def food_collision(self):
        return self.player.rect == self.food.rect

    def body_collision(self, rect):
        return rect in self.player.body[:-1]

    @staticmethod
    def wall_collision(x, y):
        return not 0 <= x < SCREEN_WIDTH or not 0 <= y < SCREEN_HEIGHT

    def over(self):
        self.__init__()

if __name__ == "__main__":
    DISPLAY = Display(SCREEN_WIDTH, SCREEN_HEIGHT, HUD_WIDTH)
    Game().play()
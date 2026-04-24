from game.player import Player
from game.food import Food
from game.display import Display, pygame

FPS = 10
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
HUD_WIDTH = 200

DISPLAY = Display(SCREEN_WIDTH, SCREEN_HEIGHT, HUD_WIDTH)

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
        self.get_events()
        self.player.update()
        DISPLAY.update()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.player.vx != 1:
                        self.player.go_left()
                        break
                if event.key == pygame.K_RIGHT:
                    if self.player.vx != -1:
                        self.player.go_right()
                        break
                if event.key == pygame.K_UP:
                    if self.player.vy != 1:
                        self.player.go_up()
                        break
                if event.key == pygame.K_DOWN:
                    if self.player.vy != -1:
                        self.player.go_down()
                        break
            if event.type == pygame.QUIT:
                DISPLAY.running = False
                break

    def check_collisions(self):
        if self.body_collision() or self.wall_collision(self.player.x, self.player.y):
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

    def body_collision(self):
        return self.player.rect in self.player.body[:-1]

    @staticmethod
    def wall_collision(x, y):
        return not 0 <= x < SCREEN_WIDTH or not 0 <= y < SCREEN_HEIGHT

    def over(self):
        self.__init__()

if __name__ == "__main__":
    Game().play()
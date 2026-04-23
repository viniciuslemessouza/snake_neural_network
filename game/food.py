import random

from game.block import Block

class Food(Block):
    def __init__(self, x, y, color="#aa0000"):
        super().__init__(x, y, color)

    def set_position(self, screen_width, screen_height, exceptions):
        while True:
            self.x = random.randint(0, screen_width // self.tile - 1) * self.tile
            self.y = random.randint(0, screen_height // self.tile - 1) * self.tile
            self.get_rect()
            if not self.rect in exceptions:
                break
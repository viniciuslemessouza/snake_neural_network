from game.block import Block

class Player(Block):
    def __init__(self, x, y, color="#00bb00"):
        super().__init__(x, y, color)
        self.vx = 0
        self.vy = 0
        self.body = []
        self.length = 5
        self.steps = 0
        self.hunger = 0

    def increase_length(self):
        if len(self.body) >= self.length:
            self.body.pop(0)
        if self.vx != 0 or self.vy != 0:
            self.body.append(self.rect)
        else:
            self.body = [self.rect]

    def set_position(self, screen_width, screen_height):
        self.x = (screen_width // self.tile) // 2 * self.tile
        self.y = (screen_height // self.tile) // 2 * self.tile

    def go_left(self):
        self.vx = -1
        self.vy = 0

    def go_right(self):
        self.vx = 1
        self.vy = 0

    def go_up(self):
        self.vx = 0
        self.vy = -1

    def go_down(self):
        self.vx = 0
        self.vy = 1

    def move(self):
        self.x += self.vx * self.tile
        self.y += self.vy * self.tile

    def update(self):
        self.move()
        self.get_rect()
        self.increase_length()
        if self.vx != 0 or self.vy != 0:
            self.steps += 1
            self.hunger += 1
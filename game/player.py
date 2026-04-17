from block import Block

class Player(Block):
    def __init__(self, x, y, color="#00bb00"):
        super().__init__(x, y, color)
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

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
        self.get_rect()
        self.move()

    def get_rect(self):
        self.rect = [self.x, self.y, self.tile, self.tile]
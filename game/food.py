from block import Block

class Food(Block):
    def __init__(self, x, y, color="#aa0000"):
        super().__init__(x, y, color)
        self.x = x
        self.y = y
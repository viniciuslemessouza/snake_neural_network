from block import Block

class Player(Block):
    def __init__(self, x, y, color="#00bb00"):
        super().__init__(x, y, color)
        self.x = x
        self.y = y
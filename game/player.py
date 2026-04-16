from block import Block

class Player(Block):
    def __init__(self, x, y, color, outline_color):
        super().__init__(x, y, color, outline_color)
        self.x = x
        self.y = y
        self.color = color
        self.outline_color = outline_color
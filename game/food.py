from block import Block

class Food(Block):
    def __init__(self, x, y, color="red", outline_color="white"):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.color = color
        self.outline_color = outline_color
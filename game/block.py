class Block:
    def __init__(self, x, y, color, tile=20, outline_color="white"):
        self.x = x
        self.y = y
        self.tile = tile
        self.color = color
        self.outline_color = outline_color
        self.rect = [x, y, tile, tile]

    def get_rect(self):
        self.rect = [self.x, self.y, self.tile, self.tile]
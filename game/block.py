class Block:
    def __init__(self, x, y, color, size=20, outline_color="white"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.outline_color = outline_color
        self.rect = [x, y, size, size]
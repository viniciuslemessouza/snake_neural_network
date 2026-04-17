import pygame

pygame.init()

class Display:
    def __init__(self, width, height, hud_width):
        self.width = width
        self.height = height
        self.hud_width = hud_width
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(width+hud_width, height)

    def update(self):
        self.screen.fill("black")
        pygame.display.flip()
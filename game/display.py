import pygame

pygame.init()

class Display:
    def __init__(self, width, height, hud_width):
        self.width = width
        self.height = height
        self.hud_width = hud_width
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([width+hud_width, height])
        self.running = True

    def update(self):
        self.get_events()
        self.screen.fill("black")
        pygame.display.flip()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
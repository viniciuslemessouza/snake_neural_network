import pygame

pygame.init()

class Display:
    def __init__(self, width, height, hud_width):
        self.width = width
        self.height = height
        self.hud_width = hud_width
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode([width + hud_width, height])
        self.running = True

    def update(self):
        self.get_events()
        pygame.display.flip()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

    def draw(self, game_object):
        pygame.draw.rect(self.surface, game_object.color, game_object.rect, 0, round(game_object.size*0.1))
        pygame.draw.rect(self.surface, game_object.outline_color, game_object.rect, 1, round(game_object.size*0.1))
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
        self.font = pygame.font.SysFont("Times New Roman", 20, True)

    @staticmethod
    def update():
        pygame.display.flip()

    def draw(self, game_object):
        pygame.draw.rect(self.surface, game_object.color, game_object.rect, 0, round(game_object.tile * 0.1))
        pygame.draw.rect(self.surface, game_object.outline_color, game_object.rect, 1, round(game_object.tile * 0.1))

    def plot_hud(self):
        pygame.draw.line(self.surface, "white", [self.width, 0], [self.width, self.height], 2)

    def plot_text(self, message, value, index, color="white"):
        text = self.font.render(f"{message}: {value}", True, color)
        self.surface.blit(text, [self.width + 20, index * 30 + 20])
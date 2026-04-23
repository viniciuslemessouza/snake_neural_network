from neural_network.network import Network
from game.snake import *

class GeneticAlgorithm:
    def __init__(self, population_length, structure):
        self.population_length = population_length
        self.structure = structure
        self.population = [Network(self.structure) for _ in range(self.population_length)]
        self.game = Game()
        self.net_index = 0

    def play(self):
        while DISPLAY.running:
            while not self.check_collisions() and DISPLAY.running:
                self.game.update()
                if self.game.food_collision():
                    self.game.got_food()
                self.game.draw()
                DISPLAY.clock.tick(FPS)
            self.game.over()
            self.record_network()
            self.net_index += 1

    def check_collisions(self):
        return self.game.body_collision() or self.game.wall_collision()

    def record_network(self):
        self.population[self.net_index].fitness = ((self.game.score * 100) + self.game.player.steps -
                                                   (self.game.player.hunger * 8))

genetic = GeneticAlgorithm(8, [2, 3, 1])
genetic.play()
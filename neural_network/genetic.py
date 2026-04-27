import os.path
import pickle

from math import ceil
from copy import deepcopy
from random import random, uniform

from neural_network.network import Network
from game.snake import Game, DISPLAY

FPS = 60

class GeneticAlgorithm:
    def __init__(self, population_length, structure):
        self.population_length = population_length
        self.structure = structure
        self.population = self.load_generation()
        self.game = Game()
        self.net_index = 0
        self.gen_index = 0
        self.parent_rate = 0.2
        self.mutation_rate = 0.01
        self.best_gen_fitness = 0
        self.best_gen_score = 0
        self.best_fitness = 0
        self.best_score = 0

    def run(self):
        while DISPLAY.running:
            while not self.check_collisions() and DISPLAY.running:
                self.game.draw()
                self.plot_metrics()
                self.run_network()
                self.game.update()
                if self.game.food_collision():
                    self.game.got_food()
                if self.game.player.hunger >= 400:
                    break
                DISPLAY.clock.tick(FPS)
            self.record_network()
            self.game.over()
            self.save_metrics()
            self.next_network()
        self.save_generation()

    def load_generation(self):
        population = [Network(self.structure) for _ in range(self.population_length)]

        if os.path.exists("neural_network.pkl") and os.path.exists("structure.pkl"):
            with open("structure.pkl", "rb") as structure_file:
                structure = pickle.load(structure_file)
                if structure == self.structure:
                    with open("neural_network.pkl", "rb") as network_file:
                        population = pickle.load(network_file)

        return population

    def save_generation(self):
        with open("structure.pkl", "wb") as structure_file:
            pickle.dump(self.structure, structure_file)
        with open("neural_network.pkl", "wb") as network_file:
            pickle.dump(self.population, network_file)

    def save_metrics(self):
        self.best_gen_fitness = max(network.fitness for network in self.population)
        self.best_gen_score = max(network.score for network in self.population)
        self.best_fitness = max(self.best_fitness, max(network.fitness for network in self.population))
        self.best_score = max(self.best_score, max(network.score for network in self.population))

    def plot_metrics(self):
        DISPLAY.plot_text("Generation", self.gen_index+1, 5, "lightblue")
        DISPLAY.plot_text("Network", self.net_index+1, 6, "lightblue")
        DISPLAY.plot_text("Best Fitness", self.best_fitness, 7, "lightblue")
        DISPLAY.plot_text("Best Score", self.best_score, 8, "lightblue")
        DISPLAY.plot_text("Best Gen. Fit.", self.best_gen_fitness, 9, "lightblue")
        DISPLAY.plot_text("Best Gen. Sco.", self.best_gen_score, 10, "lightblue")

    def next_network(self):
        self.net_index += 1
        if self.net_index == self.population_length:
            self.save_generation()
            self.net_index = 0
            self.gen_index += 1
            self.population = self.next_generation()

    def run_network(self):
        network = self.population[self.net_index]
        inputs = self.get_inputs()
        network.run(inputs)
        self.play_game()

    def play_game(self):
        output = self.population[self.net_index].output
        move = max(range(len(output)), key=output.__getitem__)

        if move == 0: # Left
            if self.game.player.vy == -1:
                self.game.player.go_left()
            elif self.game.player.vy == 1:
                self.game.player.go_right()
            elif self.game.player.vx == -1:
                self.game.player.go_down()
            elif self.game.player.vx == 1:
                self.game.player.go_up()

        if move == 1: # Straight
            pass

        if move == 2:  # right
            if self.game.player.vy == -1:
                self.game.player.go_right()
            elif self.game.player.vy == 1:
                self.game.player.go_left()
            elif self.game.player.vx == -1:
                self.game.player.go_up()
            elif self.game.player.vx == 1:
                self.game.player.go_down()

        if self.game.player.vx + self.game.player.vy == 0:
            if move == 0:
                self.game.player.go_up()
            if move == 1:
                self.game.player.go_left()
            if move == 2:
                self.game.player.go_right()

    def get_inputs(self):
        player = self.game.player
        food = self.game.food

        x = player.x
        y = player.y
        tile = player.tile

        vx = player.vx
        vy = player.vy

        # posições relativas
        front_x = x + vx * tile
        front_y = y + vy * tile

        left_x = x - vy * tile
        left_y = y + vx * tile

        right_x = x + vy * tile
        right_y = y - vx * tile

        body = {(b[0], b[1]) for b in player.body[:-1]}

        # perigo
        danger_front = (
                self.game.wall_collision(front_x, front_y)
                or (front_x, front_y) in body
        )

        danger_left = (
                self.game.wall_collision(left_x, left_y)
                or (left_x, left_y) in body
        )

        danger_right = (
                self.game.wall_collision(right_x, right_y)
                or (right_x, right_y) in body
        )

        # comida relativa
        food_front = 0
        food_left = 0
        food_right = 0

        dx = food.x - x
        dy = food.y - y

        if vx == 1:  # direita
            food_front = dx > 0
            food_left = dy < 0
            food_right = dy > 0

        elif vx == -1:  # esquerda
            food_front = dx < 0
            food_left = dy > 0
            food_right = dy < 0

        elif vy == 1:  # baixo
            food_front = dy > 0
            food_left = dx > 0
            food_right = dx < 0

        elif vy == -1:  # cima
            food_front = dy < 0
            food_left = dx < 0
            food_right = dx > 0

        return [
            int(danger_front),
            int(danger_left),
            int(danger_right),

            int(food_front),
            int(food_left),
            int(food_right),

            int(vx == -1),
            int(vx == 1),
            int(vy == -1),
            int(vy == 1),
        ]

    def check_collisions(self):
        return self.game.body_collision() or self.game.wall_collision(self.game.player.x, self.game.player.y)

    def record_network(self):
        current_fitness = self.population[self.net_index].fitness
        new_fitness = round(
                self.game.score * 100
                + self.game.player.steps * 0.5
                - self.game.player.hunger * 2
        )
        self.population[self.net_index].fitness = max(current_fitness, new_fitness)
        self.population[self.net_index].score = self.game.score

    def next_generation(self):
        parents = deepcopy(self.get_parents())
        parents_mutation = deepcopy(parents)
        return parents + self.mutation(parents_mutation)

    def get_parents(self):
        self.population.sort(key=lambda x: x.fitness, reverse=True)
        return self.population[:round(self.parent_rate*self.population_length)]

    def mutation(self, parents):
        mutation_range = self.population_length - len(parents)
        nets = [deepcopy(parent) for parent in parents for _ in range(ceil(mutation_range / len(parents)))]
        for net in nets:
            for layer in net.net:
                for neuron in layer:
                    for weight_index in range(len(neuron.weights)):
                        if random() <= self.mutation_rate:
                            neuron.weights[weight_index] = uniform(-1, 1)
        return nets[:mutation_range]

if __name__ == "__main__":
    genetic = GeneticAlgorithm(2048, [10, 16, 3])
    genetic.run()
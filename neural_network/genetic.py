from neural_network.network import Network
from game.snake import *

class GeneticAlgorithm:
    def __init__(self, population_length, structure):
        self.population_length = population_length
        self.structure = structure
        self.population = [Network(self.structure) for _ in range(self.population_length)]
        self.game = Game()
        self.net_index = 0

    def run(self):
        while DISPLAY.running:
            while not self.check_collisions() and DISPLAY.running:
                self.game.draw()
                self.run_network()
                self.game.update()
                if self.game.food_collision():
                    self.game.got_food()
                if self.game.player.hunger >= 100:
                    break
                DISPLAY.clock.tick(FPS)
            self.game.over()
            self.record_network()
            self.next_network()

    def next_network(self):
        self.net_index += 1
        if self.net_index == self.population_length:
            self.net_index = 0

    def run_network(self):
        inputs = self.get_inputs()
        self.population[self.net_index].run(inputs)
        self.play_game()

    def play_game(self):
        output = self.population[self.net_index].output
        move = output.index(max(output))

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
        wall_distance_up = self.game.player.x / SCREEN_WIDTH
        wall_distance_down = self.game.player.y / SCREEN_HEIGHT
        wall_distance_left = (SCREEN_WIDTH - self.game.player.x) / SCREEN_WIDTH
        wall_distance_right = (SCREEN_HEIGHT - self.game.player.y) / SCREEN_HEIGHT
        food_distance_x = (self.game.player.x - self.game.food.x) / SCREEN_WIDTH
        food_distance_y = (self.game.player.y - self.game.food.y) / SCREEN_HEIGHT
        body_distance_x, body_distance_y = self.get_body_distance()

        return [wall_distance_up, wall_distance_down, wall_distance_left, wall_distance_right, food_distance_x,
                food_distance_y, body_distance_x, body_distance_y, self.game.player.vy, self.game.player.vx]

    def get_body_distance(self):
        x = self.game.player.x
        y = self.game.player.y
        while True:
            x += self.game.player.vx * self.game.player.tile
            y += self.game.player.vy * self.game.player.tile

            if [x, y, self.game.player.tile, self.game.player.tile] in self.game.player.body[:-1]:
                body_dist_x = abs(self.game.player.x - x) / SCREEN_WIDTH
                body_dist_y = abs(self.game.player.y - y) / SCREEN_HEIGHT
                return [body_dist_x, body_dist_y]
            if self.game.wall_collision(x, y) or self.game.player.vx + self.game.player.vy == 0:
                return [0, 0]

    def check_collisions(self):
        return self.game.body_collision() or self.game.wall_collision(self.game.player.x, self.game.player.y)

    def record_network(self):
        self.population[self.net_index].fitness = ((self.game.score * 100) + self.game.player.steps -
                                                   (self.game.player.hunger * 8))

genetic = GeneticAlgorithm(128, [10, 24, 24, 3])
genetic.run()
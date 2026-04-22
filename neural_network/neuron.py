import math
import random

class Neuron:
    def __init__(self, n_inputs):
        self.weights = [random.gauss(0, math.sqrt(2 / n_inputs)) for _ in range(n_inputs)]
        self.bias = random.gauss(0, 1)
        self.activation = lambda x: max(0, x)

    def forward(self, inputs):
        sign = sum(w * x  for w, x in zip(self.weights, inputs)) + self.bias
        return self.activation(sign)
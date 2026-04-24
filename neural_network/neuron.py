import random
import math

class Neuron:
    def __init__(self, n_inputs):
        self.weights = [random.uniform(-1, 1) for _ in range(n_inputs)]
        self.bias = random.uniform(-.1, .1)
        self.activation = lambda x: max(0, math.tanh(x))

    def forward(self, inputs):
        sign = sum(w * x  for w, x in zip(self.weights, inputs)) + self.bias
        return self.activation(sign)
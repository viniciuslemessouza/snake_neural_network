from math import tanh
from random import uniform

class Neuron:
    def __init__(self, n_inputs):
        self.weights = [uniform(-1, 1) for _ in range(n_inputs)]
        self.bias = uniform(-1, 1)
        self.activation = tanh

    def forward(self, inputs):
        weights = self.weights
        sign = self.bias

        for i in range(len(weights)):
            sign += weights[i] * inputs[i]
        return self.activation(sign)
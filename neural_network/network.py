from neural_network.neuron import Neuron

class Network:
    def __init__(self, structure):
        self.structure = structure
        self.net = []
        self.output = 0
        self.fitness = 0

    def run(self, inputs):
        for neurons_per_layer in self.structure:
            layer = []
            self.output = []
            for _ in range(neurons_per_layer):
                neuron = Neuron(len(inputs))
                layer.append(neuron)
                self.output.append(neuron.forward(inputs))
            inputs = self.output
            self.net.append(layer)

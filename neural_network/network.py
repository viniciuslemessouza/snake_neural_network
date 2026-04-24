from neural_network.neuron import Neuron

class Network:
    def __init__(self, structure):
        self.structure = structure
        self.net = self.build_net()
        self.output = []
        self.fitness = 0

    def build_net(self):
        net = []
        n_inputs = self.structure[0]
        for neurons_per_layer in self.structure:
            layer = []
            for _ in range(neurons_per_layer):
                layer.append(Neuron(n_inputs))
            net.append(layer)
            n_inputs = neurons_per_layer
        return net

    def run(self, inputs):
        for layer in self.net:
            self.output = []
            for neuron in layer:
                self.output.append(neuron.forward(inputs))
            inputs = self.output

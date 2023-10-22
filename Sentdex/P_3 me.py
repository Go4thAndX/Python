# Building neural networks from scratch in Python
# https://youtu.be/tMrbN67U9d4
# Zie Neural Network Concepts.txt

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

# Output of the current layer
layer_outputs = []

for neuron_weight, neuron_bias in zip(weights, biases):
    # Output for given neuron
    neuron_output = 0

    for neuron_input, weight in zip(inputs, neuron_weight):
        # neuron_output_orig = neuron_output
        neuron_output += neuron_input * weight
        # neuron_output = neuron_output_orig + (neuron_input * weight)

    # neuron_output_orig = neuron_output
    neuron_output += neuron_bias
    # neuron_output = neuron_output_orig + neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)

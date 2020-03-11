#### Perceptron (Threshold Logic Unit)

inputs : x1...xn

weights : w1...wn

weighted sum : z = w1x1 + w2x2 + ... + wnxn = x(transposed) * w

steps functions commonly used:

1) heaviside
2) sign

##### training a TLU means to find the right values for w0,w1,w2.

computing outputs of a fully connected layer:

perceptron learning rule:

#### MCP (Multiple layered Perceptron)

a single TLU can't solve XOR problems, but a MCP can.

if ANN contains deep stacks of layers, its called the DNN (Deep Neural Network).

##### Training MLP is made possible by backpropagation training algorithm.

uses two passes; one forward, one backwards through the network.

it computes the gradient of the network's error with regards to every model paramater.

it finds out how each weight and bias should be tweaked in order to reduce error.

basically a Gradient Descent using efficient techniques for computing the gradients automatically.

1) makes a prediction (forward pass)and measures the error
2) then goes through each layer in reverse to measure the error contribution in each connection (backward pass)
3) finally tweaks the connection weights to reduce error (Gradient Descent)

##### Activator functions for MCP

1) sigmoid
2) hyperbole
3) rectified linear unit

We need the activator functions because linear functions, when chained, will only produce linear functions in the end (by the Chain Rule). 
This means that layering them in deep layers will be equivalent to a single layer and can't solve complex problems.

Large DNNs with nonlinear functions can theoretically approximate any continuous functions.

 
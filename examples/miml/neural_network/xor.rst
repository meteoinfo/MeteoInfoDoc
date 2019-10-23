.. _examples-miml-neural_network-xor:

**************************
XOR with Neural Network
**************************

XOR: This example is essentially the "Hello World" of neural network
programming.  This example shows how to construct an neural
network to predict the output from the XOR operator.  This example
uses backpropagation to train the neural network.

    ==  ==  =======
    a	b	a XOR b
    ==  ==  =======
    1	1	0
    0	1	1
    1	0	1
    0	0	0
    ==  ==  =======

::

    from miml.neural_network import FeedforwardNetwork

    indata = array([[0,0],[1,0],[0,1],[1,1]])
    ideal = array([0,1,1,0])
    net = FeedforwardNetwork(5, 'trainlm')
    net.layers[0].set_activation('tanh')
    net.train(indata, ideal, isprint=True)
    print net.predict([0,0])
    print net.predict([0,1])
    
::

    >>> run script...
    Epochs 1: Error=0.666
    Epochs 2: Error=0.327
    Epochs 3: Error=0.180
    Epochs 4: Error=0.018
    Epochs 5: Error=0.003
    Epochs 6: Error=0.001
    array([-0.015162892109416235])
    array([0.9941280862563597])

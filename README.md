I want to make a neural network from scratch, in order to abstract away the technicalities of it's inner workings in the future. This will hopefully allow more complex networks to be made, whilst still having a good understanding of the mathematics of how the network is functioning underneath. 

## 1. Making the Neural Network, **The \__init__ method** 

Neural Networks are a combination of the following elements
* An **input layer**, **x**
* An arbitrary (i.e. can vary) amount of **hidden layers**
* An **output layer**, **ŷ**
* Weights and biases within each layer, **W and b**
* A choice of **activation function** for each hidden layer, **σ**

## 2. Training the Neural Network, **The ***feedforward*** method, and the ***backpropagation*** method**

The output of a 2-layer neural network is:
* **ŷ=σ(W<sub>2</sub>σ(W<sub>1</sub>x + b<sub>1</sub>) + b<sub>2</sub>)**

We now want to change and update the **W's and b's** until we have an accurate prediction **ŷ** given the input data **y**
This process is commonly referred to as **training**.
The training process consist of the following steps:
* Calculating the predicted output **ŷ** know as **feedforward**
* Updating weights and biases, known as **backpropagation**

## 3. Loss Function

There are many possible loss functions, but an intuitive version used in this code is the sum of squares loss function:

**= Σ(y - ŷ)<sup>2</sup>**

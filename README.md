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

![alt text](https://user-images.githubusercontent.com/36263575/58904839-3de9e800-8700-11e9-883c-ac3740d77c84.png)

## 4. Running backpropagation and feedforwards algorithms to find appropriate weights

Say we have the following relationship between our data and our labels.

| x1 | x2 | x3 | y |
|----|----|----|---|
| 0  | 0  | 1  | 0 |
| 0  | 1  | 1  | 1 |
| 1  | 0  | 1  | 1 |
| 1  | 1  | 1  | 0 |

We want to train the algorithm to apprximate the function f(x) that provides the map of x to y, by updated the weights of the neural network.

![alt text](https://user-images.githubusercontent.com/36263575/58977577-f1ff7780-87c1-11e9-9d9a-08883dc1e0b2.png)

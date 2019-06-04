class NeuralNetwork:
	def __init__(self, x, y):
		# Take the data x, and assign it to an instance of the input object
		self.input = x
		# Produce a first array (1st hidden layer) of randomised weights with number of rows equal to number of columns in the data (x=self.input.shape[1]) and number of columns eqaul to 4 (y=4)
		self.weights1 = np.random.rand(self.input.shape[1], 4)
		# Produce a second array (2nd hidden layer) of randomised weights with number of rows equal to 4 (x=4) and number of columns eqaul to 1 (y=1) 
		self.weights2 = np.random.rand(4,1)
		# Take the labels y, and assign them to an instance of the y object
		self.y = y
		# Make an array, of the same size as the labels y array, of zeros, and assign it to an instance of the ouput object
		self.output = np.zeros(y.shape)
	
	def feedforward(self):
		# layer 1 is as follows - z=sigma(w1*x + b1)
		self.layer1 = sigmoid(np.dot(self.input, self.weights1))
		# output is = sigmoid(w2*z +b2)
		self.output = sigmoid(np.dot(self.layer1, self.weights2))
	def backprop(self):
		# apply chain rule to weights1 or w1
		d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))
		# apply chain rule to weights2 or w2
		d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))

		# we now need to update weights with the derivative (change) of the loss function
		self.weights1 += d_weights1
        self.weights2 += d_weights2

"""

	linear_regression.py

	Implementation of linear regression, by hand, using numpy
	https://cmdlinetips.com/2020/03/linear-regression-using-matrix-multiplication-in-python-using-numpy/
	https://towardsdatascience.com/linear-regression-by-hand-python-and-r-79994d47f68
	https://towardsdatascience.com/linear-regression-with-python-and-numpy-25d0e1dd220d
	https://ml-cheatsheet.readthedocs.io/en/latest/linear_regression.html
"""

import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression

class LinearRegressionByHand():
	"""
	
	By-hand implementation of linear regression

	"""
	def __init__(self):
		pass

	def fit(self, X, y, num_epochs = 50, learning_rate = 2):

		# initializations
		self.X = np.array(X)
		self.y = np.array(y).reshape(-1, 1)
		self.num_vars = X.shape[1] # number of cols/variables in our model

		# initialize weight matrix, bias
		self.weight_matrix = np.random.normal(0, 2, (self.num_vars, 1)) # sampling from ~N(0, 1), weights for each column
		self.bias = 1

		# loop through, update weights
		for i in range(num_epochs):

			# get MSE
			mean_squared_error = self.calc_MSE(self.X, self.y)

			# calculate gradient, which'll give us the partial derivatives for each column 
			# (e.g., if X.shape = (200, 5), mean_squared_error.shape = (200, 1), one for each row, so gradient.shape = (5, 1))
			gradient = np.matmul(self.X.T, mean_squared_error)

			# get updates
			self.weight_matrix = self.weight_matrix - (learning_rate * gradient)
			self.bias = self.bias - (learning_rate * np.mean(gradient))


	def predict(self, X):
		"""
		Make predictions, based off existing weight matrix
		"""
		pred = np.matmul(X, self.weight_matrix) + self.bias
		return pred

	def calc_MSE(self, X, y):
		
		"""
		Calculate MSE
		"""

		# based off the current weights, calculate Y - Wx 
		error = y - self.predict(X)

		# get squared error
		squared_error = error ** 2
		
		# get mean error
		mean_squared_error = (squared_error) / (2 * X.shape[0]) # divide by 2 (for easier derivative since cost function is squared) and N (for # of rows)

		return mean_squared_error

	def evaluate(self, X = None):

		"""
		Evaluates MSE of predictions (defaults to own predictions)
		"""
		if X is None:
			X = self.predict(self.X)

		error = self.y - X

		squared_error = error ** 2

		mean_squared_error = np.mean(squared_error) / 2

		return mean_squared_error




if __name__ == "__main__":

	X = np.random.random(100).reshape((20, 5)) * 2 # 20 rows, 5 columns
	y = np.random.random(20) * 2 # get our output variables y

	print(f"Our original X is:\n{X}\nOur original y is:\n{y}\n")

	# get linear regression that we created
	linReg_by_hand = LinearRegressionByHand()
	linReg_by_hand.fit(X, y)
	preds_byHand = linReg_by_hand.predict(X)
	print(f"The MSE between the predictions and the actual y values is: {linReg_by_hand.evaluate()}")

	# get linear regression from sklearn
	linReg_sklearn = LinearRegression()
	linReg_sklearn.fit(X, y)
	preds_sklearn = linReg_sklearn.predict(X)

	# get difference in predictions
	print(f"The predictions from doing it by hand were:\n{preds_byHand}\nThe predictions from doing it with sklearn were:\n{preds_sklearn}\n")
	print(f"The difference in the predictions is:{np.sum(preds_byHand - preds_sklearn)}")


	# compare to numpy implementation of linear regression
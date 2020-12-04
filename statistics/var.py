"""
	var.py

	Implementation of variance formula

	Var(X) = E[(X - E[X])]
"""

import numpy as np

def var(X):

	# get E[X]
	mean = np.mean(X)

	#var = np.mean((X - mean)**2)

	# or, with for-loop, to make it more explicit
	total_diffs = 0
	for x in X:
		total_diffs += ((x - mean)**2)

	# get average
	var = total_diffs / X.shape[0]

	return var

if __name__ == "__main__":

	# generate random dataset
	X = np.random.rand(10)

	print(f"The original X is: {X}")

	# calculate by hand, and also with numpy
	var_X = var(X)
	np_var_X = np.var(X)
	print(f"The variance found by hand is: {var_X}")
	print(f"The variance found with numpy is: {np_var_X}")

	assert np.allclose(var_X, np_var_X)


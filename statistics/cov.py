"""

	cov.py

	Calculates covariance, by hand
	https://en.wikipedia.org/wiki/Covariance

"""

import numpy as np
def cov(X):

	"""
	Calculates the covariance of the elements in X. 

	If X.shape = (n, p), the covariance matrix will have shape = (p, p)
	
	cov(X, Y) = E[XY] - E[X]E[Y]
	"""

	print(f"The original matrix is:\n{X}")

	# normalize data
	X = X - X.mean(axis=0) 

	print(f"The normalized X is:\n{X}")
	# calculate covariance
	normalizer = (X.shape[0] - 1) # (n - 1), by Bessel's correction (but can be 1/n as well, since it's in expectation)

	cov = np.dot(X.T, X.conj()) / normalizer
	print(f"The covariance matrix is:\n{cov}")

if __name__ == "__main__":

	# generate random dataset
	b1 = np.random.rand(10)
	b2 = np.random.rand(10)
	X = np.column_stack([b1, b2])

	# get covariance, both by hand and with numpy implementation
	cov_X = cov(X)
	np_cov = np.cov(b1, b2)

	assert np.allclose(cov_X, np_cov)
	
"""

	pca.py

	PCA implementation, from scratch, using Numpy

	Useful resources:
		- https://towardsdatascience.com/principal-component-analysis-pca-from-scratch-in-python-7f3e2a540c51
		- https://www.askpython.com/python/examples/principal-component-analysis

"""

import numpy as np

def pca(X, num_components):

	"""
	
	Implements PCA, using only numpy

	"""

	print(f"The original (unscaled) X is: {X}")

	# 1. subtract the mean (of each column) from X, to scale it
	X_scaled = X - np.mean(X, axis=0)

	print(f"The scaled X is:\n {X_scaled}")

	# 2. Calculate covariances 
	cov_mat = np.cov(X_scaled, rowvar=False)
	print(f"The covariance matrix has shape = {cov_mat.shape} and looks like this: {cov_mat}")

	# 3. Compute eigenvalues and eigenvectors
	eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)

	# 4. Sort eigenvalues in descending order, and get the corresponding eigenvectors
	sorted_index = np.argsort(eigen_values)[::-1]
 
	sorted_eigenvalue = eigen_values[sorted_index]
	sorted_eigenvectors = eigen_vectors[:,sorted_index]

	# 5. Get the eigenvectors that we need
	eigenvector_subset = sorted_eigenvectors[:,0:num_components]

	# 6. Transform our dataset into the coordinate system defined by the eigenvectors
	X_reduced = np.dot(eigenvector_subset.transpose(),X_scaled.transpose()).transpose()

	# 7. Compare
	print(f"The shape of the old X was: {X.shape}")
	print(f"The old X was:\n {X}")
	print("===============================")
	print(f"The shape of the new X is: {X_reduced.shape}")
	print(f"The new X is:\n {X_reduced}")

	return X_reduced

if __name__ == "__main__":

	# generate random dataset
	X = np.random.randint(10,50,100).reshape(20,5) 

	# get PCA of X
	pca(X, 2)


"""

	knn.py

	k-nearest neighbors, by hand

"""

import numpy as np
import math
import statistics

class KNN():

	def __init__(self):
		pass

	def fit(self, X, y):
		self.X = X
		self.y = y

	def predict(self, X, n_neighbors = 3):

		"""
		Implement knn, with # neighbors = n_neighbors
		"""

		# initialize arr of preds:
		preds = []


		# loop through all Xs that we want predictions for
		for new_val in X:

			# initialize list of distances, index of nearest neighbors
			distances_idx_tuples = [] # e.g., (983, 1) means it has a distance of 983 with the idx=1 value

			# loop through all Xs in training set
			for idx, x in enumerate(self.X):

				# calculate distance (use MSE)
				distance = math.sqrt(np.sum((new_val - x)**2))
				
				# initialize first distances
				if len(distances_idx_tuples) < n_neighbors:
					distances_idx_tuples.append((distance, idx))
					# sort by distance (ascending)
					distances_idx_tuples.sort(key= lambda x: x[0])
					continue

				# compare to rightmost distance (since it's sorted, we only need to compare 
				# our new value to the greatest distance value), and replace if smaller
				if distance < distances_idx_tuples[-1][0]:
					# replace:
					distances_idx_tuples[-1] = (distance, idx)

				# re-sort array
				distances_idx_tuples.sort(key = lambda x: x[0])

			# get actual y-values, from closest neighbors
			idxs_closest_neighbors = [x[1] for x in distances_idx_tuples]
			actual_y_vals = self.y[idxs_closest_neighbors]

			# get mode, use as prediction
			pred = statistics.mode(actual_y_vals)

			preds.append(pred)

		# return predictions
		return preds

	def evaluate(self, X, y):

		"""
		Evaluate accuracy on test set
		"""

		preds = self.predict(X)
		accuracy = np.mean(preds == y)
		return accuracy

if __name__ == "__main__":

	# get training, test sets
	X_train = np.random.random(100).reshape(20, 5) * 10
	y_train = np.random.randint(0, 1, 20) # binary vector
	X_test = np.random.random(100).reshape(20, 5) * 10
	y_test = np.random.randint(0, 1, 20)

	# create KNN
	knn = KNN()
	knn.fit(X_train, y_train)
	accuracy = knn.evaluate(X_test, y_test)
	print(f"The accuracy on our test set is: {accuracy}")



"""

	K-means clustering
	
	Numpy implementation of k-means clustering

"""
import numpy as np
import math

def k_means(X, k = 5):

	"""
	Implements k-means clustering
	"""
	
	# randomly initialize "k" means
	means = np.random.random(X.shape[0] * k).reshape((X.shape[0], 5))

	# cluster labels
	labels = []

	# get minimum error threshold
	min_threshold = 0.5

	# loop through rounds
	for round in range(100):

		# get distance from points to centroids
		distances_points_centroids = []

		# loop through all Xs, assign clusters
		for x in X:

			min_idx = 0
			min_distance = 99999

			for i in range(means.shape[1]):

				# get cluster centroid
				center = means[:, i]

				# get distance
				distance = math.sqrt(np.sum((x - center)**2))

				if distance < min_distance:
					min_distance = distance
					min_idx = i

			distances_points_centroids.append(min_distance)

			# assign x to min_idx cluster
			labels.append(min_idx)

		# reassign means based off cluster labels
		for i in range(means.shape[1]):

			# get observations of X corresponding to that label
			X_clust = X[np.where(labels == i), :]

			# get mean point
			mean = X_clust.sum() / X_clust.shape[0]

			# assign that as new mean for that cluster
			means[i] = mean

		# get total error
		total_error = np.sum(distances_points_centroids)

		if total_error < min_threshold:
			break


if __name__ == "__main__":

	# random observations
	X = np.random.random(500).reshape((100, 5)) * 2 # 100 rows, 5 columns

	# group them into 5 clusters
	k = 5

	k_means(X, k=k)



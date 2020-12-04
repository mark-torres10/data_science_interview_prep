"""

	merge_sort.py

	Implements merge sort algorithm
	https://www.geeksforgeeks.org/merge-sort/

	Time complexity: O(nlogn)
	Space complexity: O(N)

"""

def merge(left_arr, right_arr):

	"""
	Merges two arrays into one, such that they're now ordered ascending
	"""

	left_index = 0
	right_index = 0

	# initialize array to store results
	return_arr = []

	# loop through both arrays
	while left_index < len(left_arr) and right_index < len(right_arr):
		if left_arr[left_index] < right_arr[right_index]:
			return_arr.append(left_arr[left_index])
			left_index += 1
		else:
			return_arr.append(right_arr[right_index])
			right_index += 1

	# finish out whatever remains in the other array
	while left_index < len(left_arr):
		return_arr.append(left_arr[left_index])
		left_index += 1

	while right_index < len(right_arr):
		return_arr.append(right_arr[right_index])
		right_index += 1

	return return_arr

def merge_sort(arr):

	"""
	Implements merge sort algorithm
	"""

	# base case
	if len(arr) <= 1:
		return arr

	# recursive case
	middle_idx = len(arr) // 2

	# recursively implement on left, right subarrays
	left = merge_sort(arr[0:middle_idx])
	right = merge_sort(arr[middle_idx:len(arr)])

	# put back together
	merged_arr = merge(left, right)

	return merged_arr

if __name__ == "__main__":

	# sort the following lists (ascending)
	list1 = [1, 5, 29, 1, 3, 17]
	list2 = [1]
	list3 = [1, 20, -2, -3, -10, -200]
	list4 = [200, 199, -11, 16, 1, 0, 0, 0]

	# correct sorted arrays (ascending)
	correct_list1 = [1, 1, 3, 5, 17, 29]
	correct_list2 = [1]
	correct_list3 = [-200, -10, -3, -2, 1, 20]
	correct_list4 = [-11, 0, 0, 0, 1, 16, 199, 200]

	# sort the arrays
	sorted_list1 = merge_sort(list1)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list2 = merge_sort(list2)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list3 = merge_sort(list3)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list4 = merge_sort(list4)
	print("============================================================")
	print("============================================================")	
	print("============================================================")

	assert sorted_list1 == correct_list1
	assert sorted_list2 == correct_list2
	assert sorted_list3 == correct_list3
	assert sorted_list4 == correct_list4


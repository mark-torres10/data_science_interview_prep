"""

	binary_search.py

	Takes as input a sorted array and an element, and checks to see
	where the element is in the array, if it exists

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


def binary_search(arr, idx_low, idx_high, elem):

	"""

	"""

	# check base case
	if idx_high >= idx_low:

		# get midpoint
		idx_mid = (idx_high + idx_low) // 2

		# check num to midpoint
		if elem == arr[idx_mid]:
			print(f"The number {elem} was found in the array {arr} at index = {idx_mid}")
			return idx_mid

		# check left subarray
		elif elem < arr[idx_mid]:
			return binary_search(arr, idx_low, idx_mid - 1, elem)

		elif elem > arr[idx_mid]:
			return binary_search(arr, idx_mid + 1, idx_high, elem)

	else:
		print(f"The number {elem} wasn't found in the array {arr}")
		return -1

if __name__ == "__main__":

	# search through the following lists (ascending)
	sorted_list1 = merge_sort([1, 5, 29, 1, 3, 17])
	sorted_list2 = merge_sort([1])
	sorted_list3 = merge_sort([1, 20, -2, -3, -10, -200])
	sorted_list4 = merge_sort([200, 199, -11, 16, 1, 0, 0, 0])

	output_1 = binary_search(sorted_list1, 0, len(sorted_list1), 27)
	output_2 = binary_search(sorted_list2, 0, len(sorted_list2), 0)
	output_3 = binary_search(sorted_list3, 0, len(sorted_list3), -10)
	output_4 = binary_search(sorted_list4, 0, len(sorted_list4), 16)





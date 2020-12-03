"""

	insertion_sort.py

	Implements insertion sort

	Time complexity: O(N^2)
	Space complexity: O(1)

	https://iq.opengenus.org/insertion-sort-analysis/

"""

def insertion_sort(arr):

	"""

	Implements insertion sort (ascending)

	Algorithm: Step by step procedure:

	Step 1: Assume that the first element in the list is in the sorted section of the list and remaining all elements are in the unsorted section.
	Step 2: Consider the first element from the unsorted list and insert that element into the sorted list in the order specified (ascending or descending)
	Step 3: Repeat the above steps until all the elements from the unsorted list are moved to the sorted list.

	"""

	print("++++++++++++++++++++++++++++++")
	print(f"The initial array is: {arr}")
	print("++++++++++++++++++++++++++++++")
	print("====================")

	for i in range(1, len(arr)):

		val = arr[i]

		j = i - 1

		while j >= 0 and val < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
			print("--------------------")
			print(f"We flipped {val} and {arr[j+1]} so that now {val} comes before {arr[j+1]}")
			print(f"Now the array looks like this (prior to inserting our value where it belongs): {arr}")
			print("--------------------")
		print(f"Now let's insert our value where it belongs:")
		arr[j + 1] = val
		print(f"The left subarray is now sorted. The current state of the array is: {arr}")

	print('--------------------')
	print(f"The final sorted array is: {arr}")
	print("====================")
	
	return arr

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
	sorted_list1 = insertion_sort(list1)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list2 = insertion_sort(list2)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list3 = insertion_sort(list3)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list4 = insertion_sort(list4)
	print("============================================================")
	print("============================================================")	
	print("============================================================")

	assert sorted_list1 == correct_list1
	assert sorted_list2 == correct_list2
	assert sorted_list3 == correct_list3
	assert sorted_list4 == correct_list4




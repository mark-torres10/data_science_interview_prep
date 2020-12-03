"""

	selection_sort.py

	Implements selection sort

	Time complexity: O(N^2)
	Space complexity: O(1)

"""

def swap(i, j, arr):
	"""
	Swaps two elements in an array
	"""

	if i != j:
		arr[i] = arr[i] + arr[j]
		arr[j] = arr[i] - arr[j]
		arr[i] = arr[i] - arr[j]

def selection_sort(arr):

	"""
		Implements selection sort
		https://www.csestack.org/python-selection-sort/
	"""

	print(f"The initial array is: {arr}")
	print("===========")

	for i in range(0, len(arr)):

		# initialize which # is smallest
		idx_small = i

		print(f"The first number that we're considering is: {arr[idx_small]}, at index = {idx_small}")
		print(f"Now, let's compare this number to all the other numbers")

		for j in range(i+1, len(arr)):
			print('-------------------')
			print(f"Is {arr[j]} smaller than {arr[idx_small]}?")
			if arr[j] < arr[idx_small]:
				print(f"Yes, {arr[j]} is smaller than {arr[idx_small]}")
				print(f"Now, {arr[j]} is going to be our new smallest number")
				idx_small = j
			else:
				print(f"No, {arr[j]} is not smaller than {arr[idx_small]}")
			print('-------------------')

		print(f"Now that we've determined the smallest element is {arr[idx_small]} at index = {idx_small}. We're at i = {i} and the smallest index is {idx_small}")

		print(f"Now, let's swap {arr[i]}, at element {i} and {arr[idx_small]}, at element {idx_small}")

		swap(i, idx_small, arr)

		print(f"After swapping the array, the left subarray ({arr[0:i+1]}) should be sorted and the right ({arr[i+1:len(arr)]})is still unsorted. ")

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
	sorted_list1 = selection_sort(list1)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list2 = selection_sort(list2)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list3 = selection_sort(list3)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list4 = selection_sort(list4)
	print("============================================================")
	print("============================================================")	
	print("============================================================")

	assert sorted_list1 == correct_list1
	assert sorted_list2 == correct_list2
	assert sorted_list3 == correct_list3
	assert sorted_list4 == correct_list4

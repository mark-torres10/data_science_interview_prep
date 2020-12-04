"""

	quick_sort.py

	Implementation of quick sort

	Time complexity: O(nlogn)
	Space complexity: O(1)

"""

def quick_sort(arr):

	"""
	Implementation of quick sort algorithm
	https://www.geeksforgeeks.org/quick-sort/
	"""
	pass

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
	sorted_list1 = quick_sort(list1)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list2 = quick_sort(list2)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list3 = quick_sort(list3)
	print("============================================================")
	print("============================================================")
	print("============================================================")
	sorted_list4 = quick_sort(list4)
	print("============================================================")
	print("============================================================")	
	print("============================================================")

	#assert sorted_list1 == correct_list1
	#assert sorted_list2 == correct_list2
	#assert sorted_list3 == correct_list3
	#assert sorted_list4 == correct_list4


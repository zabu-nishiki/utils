def bubble_sort(array):
	array_length = len(array)
	for i_itr in range(array_length):
		for j_itr in range(array_length-i_itr-1):
			if array[j_itr] > array[j_itr+1]: array[j_itr], array[j_itr+1] = array[j_itr+1], array[j_itr]
	return array

def selection_sort(array):
	array_length = len(array)
	for i_itr in range(array_length):
		min_idx = 0
		for j_itr in range(i_itr+1, array_length):
			if array[j_itr] < array[min_idx]: min_idx = j_itr
		array[i_itr], array[min_idx] = array[min_idx], array[i_itr]
	return array

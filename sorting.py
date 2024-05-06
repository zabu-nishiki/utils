def bubble_sort(array):
	array_length = len(array)
	for i_itr in range(array_length):
		for j_itr in range(array_length-i_itr-1):
			if array[j_itr] > array[j_itr+1]: array[j_itr], array[j_itr+1] = array[j_itr+1], array[j_itr]
	return array

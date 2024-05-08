def bubble_sort(array):
	array_length = len(array)
	for i_itr in range(array_length):
		for j_itr in range(array_length-i_itr-1):
			if array[j_itr] > array[j_itr+1]: array[j_itr], array[j_itr+1] = array[j_itr+1], array[j_itr]
	return array
##########################################################################################
def selection_sort(array):
	array_length = len(array)
	for i_itr in range(array_length):
		min_idx = i_itr
		for j_itr in range(i_itr+1, array_length):
			if array[j_itr] < array[min_idx]: min_idx = j_itr
		array[i_itr], array[min_idx] = array[min_idx], array[i_itr]
	return array
##########################################################################################
def upheap(array, child_idx):
	while child_idx!=0:
		parent_idx = int((child_idx-1)/2)
		if array[parent_idx] < array[child_idx]:
			array[parent_idx], array[child_idx] = array[child_idx], array[parent_idx]
			child_idx = parent_idx
		else: break
def downheap(array, idx):
	if idx==0: return
	parent_idx = 0
	while True:
		child_idx = 2 * parent_idx + 1
		if child_idx > idx: break
			if child_idx<idx and array[child_idx]<array[child-idx+1]: child_idx += 1
		if array[parent_idx]<array[child_idx]:
			array[parent_idx], array[child_idx] = array[child_idx]<array[parent_idx]
			parent_idx = child_idx
		else: break

def heap_sort(array):
	array_length = len(array)
	for itr in range(array_length): upheap(array, itr)
	for itr in range(array_length)[::-1]:
		array[0], array[itr] = array[itr], array[0]
		downheap(array, itr)
	

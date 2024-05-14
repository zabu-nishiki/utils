##########################################################################################
# Average Calculation | Worst Calculation | Memory Usage | Robustness
##########################################################################################
## Insertion Sort: n^2   | n^2   | 1     | True
## Bubble Sort   : n^2   | n^2   | 1     | True
## Selection Sort: n^2   | n^2   | 1     | False
##########################################################################################
# Merge Sort    : nlogn | nlogn | n     | True
# Heap Sort     : nlogn | nlogn | 1     | False
# Shell Sort    : nlogn | n^1.5 | 1     | False
# Quick Sort    : nlogn | n^2   | nlogn | False
##########################################################################################
def quick_sort(array):
    array_length = len(array)
    if array_length<=1: return array
    pivot = array[array_length//2]
    left   = [itr for itr in array if itr<pivot]
    middle = [itr for itr in array if itr==pivot]
    right  = [itr for itr in array if itr>pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(array):
	array_length = len(array)
	for i_itr in range(1, array_length):
		temp_value = array[i_itr]
		j_itr = i_itr-1
		while j_itr>=0 and array[j_itr]>temp_value:
			array[j_itr+1] = array[j_itr]
			j_itr-=1
		array[j_itr+1] = temp_value
	return array

def bubble_sort(array):
	array_length = len(array)
	for i_itr in range(array_length):
		for j_itr in range(array_length-i_itr-1):
			if array[j_itr] > array[j_itr+1]: array[j_itr], array[j_itr+1] = array[j_itr+1], array[j_itr]
	return array

def selection_sort(array):
	array_length = len(array)
	for i_itr in range(array_length):
		min_idx = i_itr
		for j_itr in range(i_itr+1, array_length):
			if array[j_itr] < array[min_idx]: min_idx = j_itr
		array[i_itr], array[min_idx] = array[min_idx], array[i_itr]
	return array
##########################################################################################
# The elements of l layers (l:=1, 2, ..., L) : 2^(l-1)-1, 2^(l-1), ..., 2^l
# index idx:=1, 2, ..., N
# [1] -< [2, 3] -< [4, 5, 6, 7] -< [8,  9, 10, 11, 12, 13, 14, 15] -< ... -< [2^(l-1),   2^(l-1)+1, ..., 2^l-1]
# [0] -< [1, 2] -< [3, 4, 5, 6] -< [7,  8,  9, 10, 11, 12, 13, 14] -< ... -< [2^(l-1)-1, 2^(l-1),   ..., 2^l-2]
##########################################################################################
def upheap(array, idx):
	while idx!=0:
		parent_idx = int((idx-1)/2)
		if array[parent_idx] < array[idx]:
			array[parent_idx], array[idx] = array[idx], array[parent_idx]
			idx = parent_idx
		else: break
def downheap(array, idx):
	parent_idx = 0
	while idx!=0:
		child_idx = 2 * parent_idx + 1
		if child_idx > idx: break
		if child_idx < idx and array[child_idx]<array[child-idx+1]: child_idx += 1
		if array[parent_idx]<array[child_idx]:
			array[parent_idx], array[child_idx] = array[child_idx], array[parent_idx]
			parent_idx = child_idx
		else: break
def heap_sort(array):
	array_length = len(array)
	for itr in range(array_length): upheap(array, itr)
	for itr in range(array_length)[::-1]:
		array[0], array[itr] = array[itr], array[0]
		downheap(array, itr)


'''
Project 2
CS2420
Ryan Balog
'''
from random import seed, sample
from time import perf_counter
from recursioncounter import RecursionCounter


def create_lyst():
    '''returns a large list to main()'''
    print("Generating list...")
    seed(0)
    lyst = sample(range(10000000), k=10000)

    print("Generated list of size ", len(lyst))
    return lyst


def is_sorted(lyst):
    '''checks data types and returns if list is sorted'''
    if isinstance(lyst, list) != True:
        raise TypeError("Object must be of type List!")
    for value in lyst:
        if isinstance(value, int) != True:
            raise ValueError("List must be full of integers!")
    test = lyst.copy()
    test.sort()

    if test == lyst:
        return True

    return False


def swap(array, i, j):
    '''swaps 2 values in a list'''
    array[i], array[j] = array[j], array[i]


def selection_sort(array):
    '''sorts array via the selection sort algorithm'''
    if isinstance(array, list) == False:
        raise ValueError("Not a list!")
    i = 0
    while i < len(array) - 1:
        min_idx = i
        j = i + 1
        while j < len(array):
            if array[j] < array[min_idx]:
                min_idx = j
            j += 1
        if min_idx != i:
            swap(array, min_idx, i)
        i += 1
    return array


def insertion_sort(array):
    '''sorts array via insertion sort and returns the sorted array'''
    if isinstance(array, list) == False:
        raise ValueError("Not a list!")
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def quicksort(array):
    '''calls quicksort_helper() to sort list'''
    if isinstance(array, list) == False:
        raise ValueError("Not a list!")
    return quicksort_helper(array, 0, len(array) - 1)


def quicksort_helper(array, left, right):
    '''recursively splits down array'''
    RecursionCounter()

    if left < right:
        get_pivot = partition(array, left, right)
        quicksort_helper(array, left, get_pivot - 1)
        quicksort_helper(array, get_pivot + 1, right)

    return array


def partition(array, left, right):
    '''sets pivots and swaps values for sorting'''
    middle = (left + right) // 2
    pivot = array[middle]
    array[middle] = array[right]
    array[right] = pivot
    boundary = left

    for index in range(left, right):
        if array[index] < pivot:
            swap(array, index, boundary)
            boundary += 1
    swap(array, right, boundary)

    return boundary


def mergesort(array):
    '''merge sort algorithm'''
    if isinstance(array, list) == False:
        raise ValueError("Not a list!")
    RecursionCounter()

    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array


def main():
    '''creates copies of random lists and sends them through sort algorithms for benchmarking'''
    lyst = create_lyst()

    if is_sorted(lyst):
        print("List was already sorted, no need to sort")
        return

    # selection_sort()
    print("\nStarting selection_sort:")
    test1 = lyst.copy()
    start_selection = perf_counter()
    selection_sort(test1)
    time_selection = perf_counter() - start_selection
    print(f"selection_sort duration: {time_selection} seconds\n")

    # insertion_sort()
    print("Starting insertion_sort:")
    test2 = lyst.copy()
    start_insertion = perf_counter()
    insertion_sort(test2)
    time_insertion = perf_counter() - start_insertion
    print(f"insertion_sort duration: {time_insertion} seconds\n")

    # quicksort()
    print("Starting quicksort:")
    test3 = lyst.copy()
    start_quick = perf_counter()
    quicksort(test3)
    time_quick = perf_counter() - start_quick
    print(f"quicksort duration: {time_quick} seconds\n")

    # mergesort()
    print("Starting mergesort:")
    test4 = lyst.copy()
    start_merge = perf_counter()
    mergesort(test4)
    time_merge = perf_counter() - start_merge
    print(f"mergesort duration: {time_merge} seconds\n")


if __name__ == "__main__":
    main()

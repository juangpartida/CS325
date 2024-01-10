# 1. [WILL BE GRADED] 
#    Quickselect with Randomized Pivot (CLRS Ch. 9.2).

#    >>> from qselect import *
#    >>> qselect(2, [3, 10, 4, 7, 19])
#    4
#    >>> qselect(4, [11, 2, 8, 3])
#    11

#    Q: What's the best-case, worst-case, and average-case time complexities? Briefly explain.

#    Filename: qselect.py

import random

def partition(arr, low, high):
    # Select a random pivot element
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]

    return j

def qselect(k, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[k]
        elif pivot_index < k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

# Testing examples
if __name__ == "__main__":
    print(qselect(2, [3, 10, 4, 7, 19]))  # Should return 4
    print(qselect(4, [11, 2, 8, 3]))     # Should return 11
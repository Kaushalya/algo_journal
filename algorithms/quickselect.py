"""
Select the k-th smallest element from a list.
"""

import random


def partition(arr, left, right, pivot):
    """Partition function inplace

    Args:
        arr ([type]): [description]
        left ([type]): [description]
        right ([type]): [description]
        pivot ([type]): [description]
    """
    sorted_i = left
    # Move pivot to the end
    pivot_value = arr[pivot]
    arr[pivot], arr[right] = arr[right], arr[pivot]
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[sorted_i] = arr[sorted_i], arr[i]
            sorted_i += 1

    arr[sorted_i], arr[right] = arr[right], arr[sorted_i]
    # print(arr)
    return sorted_i


def quickselect(arr, left, right, k):
    if left==right:
        return arr[left]

    assert k<=right, "k is out of bounds"

    pivot = random.randint(left, right)
    pivot_ind = partition(arr, left, right, pivot)

    # print("pivot", pivot_ind)

    if k == pivot_ind:
        return arr[k]
    elif k < pivot_ind:
        return quickselect(arr, left, pivot_ind-1, k)
    else:
        return quickselect(arr, pivot_ind+1, right, k)


if __name__ == '__main__':
    inp = [2, 4, 8, 1]
    print(quickselect(inp, 0, len(inp)-1, 2))
    print(inp)

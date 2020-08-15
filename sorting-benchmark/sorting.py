import math


def insertion_sort(m):
    """
    Sorts a list using the insertion sort algorithm.
    m = The unsorted list.
    Examples
        insertion_sort([4,7,6,3,2,5,1])
        # => [1,2,3,4,5,6,7]
    Complexity: O(n^2)
    Returns the sorted list.
    """

    for j in range(1, len(m)):
        key = m[j]
        i = j - 1

        # shift everything greater than 'key' to it's right
        while i >= 0 and m[i] > key:
            m[i + 1] = m[i]
            i = i - 1

        m[i + 1] = key

    return m


def bubble_sort(m):
    """
    Sorts a list using the bubble sort algorithm.
    m = The unsorted list.
    Examples
        bubble_sort([4,7,6,3,2,5,1])
        # => [1,2,3,4,5,6,7]
    Complexity: O(n^2)
    Returns the sorted list.
    """
    swaps = []
    for j in range(len(m)):
        for k in range(len(m) - 1, j, -1):
            if(m[k] < m[k - 1]):
                swaps.append([k, k - 1])
                tmp = m[k]
                m[k] = m[k - 1]
                m[k - 1] = tmp
    return m


def merge_sort(m):
    """
    Sorts a list using the merge sort algorithm.
    m = The unsorted list.
    Examples
        merge_sort([4,7,6,3,2,5,1])
        # => [1,2,3,4,5,6,7]
    Complexity: O(n*Log(n))
    Returns the sorted list.
    """

    length = len(m)

    if length == 1:
        return m

    mid = int(math.floor(length / 2))

    left = merge_sort(m[0:mid])
    right = merge_sort(m[mid:length])

    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted lists.
    left  = A sorted list.
    right = A sorted list.
    Examples
        merge([2,4],[1,3])
        # => [1,2,3,4]
    Complexity: O(n1 + n2)
    Returns the sorted list post merge.
    """

    merged = []

    # while at least one list has elements
    while left or right:

        if left and right:
            if left[0] <= right[0]:
                key = left.pop(0)
            else:
                key = right.pop(0)
        elif left:
            key = left.pop(0)
        else:
            key = right.pop(0)

        merged.append(key)

    return merged


def quick_sort(m):
    """
    Sorts a list using the quick sort algorithm.
    m = The unsorted list.
    Examples
        quick_sort([4,7,6,3,2,5,1])
        # => [1,2,3,4,5,6,7]
    Complexity: O(n^2)
    Returns the sorted list.
    """

    if len(m) <= 1:
        return m

    pivot = m.pop()
    less = []
    gr8t = []

    for i in m:
        if i <= pivot:
            less.append(i)
        else:
            gr8t.append(i)

    return quick_sort(less) + [pivot] + quick_sort(gr8t)

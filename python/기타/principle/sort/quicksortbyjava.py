# arr = [5, 4, 6, 7, 8, 9, 3, 3, 3, 1, 2, 3]
# arr = [3, 9, 4, 7, 5, 0, 1, 8, 6, 2]
arr = [6, 5, 3, 6, 3, 52, 34, 234, 23, 423, 4, 1, 1, 1, 34, 1]


def partition(lis, left, right):
    pivot = lis[(left + right) // 2]

    while left <= right:
        while lis[left] < pivot:
            left += 1
        while lis[right] > pivot:
            right -= 1
        if left <= right:
            lis[left], lis[right] = lis[right], lis[left]
            left += 1
            right -= 1
    return left


def quicksort(arr1, start, end):

    # if start < end:
    #     part2 = partition(arr1, start, end)
    #     quicksort(arr1, start, part2 - 1)
    #     quicksort(arr1, part2, end)

    # if start >= end:
    #     return
    # part2 = partition(arr1, start, end)
    # quicksort(arr1, start, part2 - 1)
    # quicksort(arr1, part2, end)

    mid = partition(arr1, start, end)
    if start < mid - 1:
        quicksort(arr1, start, mid - 1)
    if mid < end:
        quicksort(arr1, mid, end)


quicksort(arr, 0, len(arr)-1)
print(arr)

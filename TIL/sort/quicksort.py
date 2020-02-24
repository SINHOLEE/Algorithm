'''
리턴값이 없는 방법...
'''

# arr = [5, 4, 6, 7, 8, 9, 3, 3, 3, 1, 2, 3]
arr = [3, 9, 4, 7, 5, 0, 1, 8, 6, 2]


def qsort(a, start, end):
    if start >= end:
        return

    mid = partition(a, start, end)
    qsort(a, start, mid-1)
    qsort(a, mid, end)

    ###
    '''
        if start < end:
        quicksort(arr1, start, part2 - 1)
        quicksort(arr1, part2, end)

    '''


def partition(aa, low, high):
    pivot = arr[(low + high) // 2]
    while True:
        # 왼쪽 인덱스가 오른쪽 인덱스보다 클 때 멈춘다(교차할 때 멈춘다)
        if low > high:
            break

        # 피봇을 기준으로 왼쪽인덱스의 값이 작으면 인덱스+1, 크거나 같으면 멈춘다.
        while True:
            if arr[low] <= pivot:
                break
            low += 1

        # 피봇을 기준으로 오른쪽인덱스의 값이 크면 인덱스+1, 작거나 같으면 멈춘다.
        while True:
            if arr[high] >= pivot:
                break
            high -= 1

        # base case(low>high)의 반대의 경우에는 low와 high를 스왑한다.
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    #
    return low


qsort(arr, 0, len(arr)-1)
print(arr)

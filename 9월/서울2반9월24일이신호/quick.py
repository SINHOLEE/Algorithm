def quick_sort(low, high):

    if high <= low:
        return

    mid = partition(low, high)
    quick_sort(low, mid - 1)
    quick_sort(mid, high)

def partition(low, high):
    pivot = arr[(low + high) // 2]
    while True:
        if low > high:
            break
        while True:
            if arr[low] >= pivot:
                break
            low += 1
        while True:
            if arr[high] <= pivot:
                break
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    return low


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, N-1)
    print('#%s %s' % (tc, arr[N//2]))


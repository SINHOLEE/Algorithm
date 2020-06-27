import sys
sys.setrecursionlimit(10000)


def recursive(idx):
    if idx <= 2:
        return arr[idx]
    if arr[idx] == 0:
        arr[idx] = recursive(idx-1) + recursive(idx-2)
    return arr[idx]


n = int(input())
arr = [0] * (n+2)
arr[1] = 1
arr[2] = 2
print(recursive(n) % 10007)

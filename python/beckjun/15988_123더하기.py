'''
큰수 다룰때, 저장하는 공간 자체가 많이 들어가므로, mod연산을 하고 나서 저장하는 것이 메모리관리에 효과적이다.
'''

n = int(input())
arr = [0] * (1000000 + 3)
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 1000001):
    arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % 1000000009

for _ in range(n):
    print(arr[int(input())] % 1000000009)

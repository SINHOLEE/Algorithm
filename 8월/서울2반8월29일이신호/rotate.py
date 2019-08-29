T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))


    print('#{} {}'.format(tc, temp[M % N]))
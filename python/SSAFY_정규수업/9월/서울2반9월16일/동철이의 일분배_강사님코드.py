T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = []
    for n in range(N):
        temp = list(map(int, input().split()))
        mat.append(temp)

def my_sum(a):
    result = 0
    for tp in temp:
        result += tp
    return result

elements = list(range(1,13))
# print(elements)
T = int(input())

for tc in range(1, T+1):
    N, K = input().split()
    N = int(N)  # 부분집합의 개수
    K = int(K)  # 원소의 합 숫자.
    count = 0
    
    for i in range(1<<len(elements)):
        temp = []
        for j in range(len(elements)):
            if i & (1<<j):
                temp += [elements[j]]
        if len(temp) == N and my_sum(temp) == K:
            count += 1
    print('#{} {}'.format(tc, count))
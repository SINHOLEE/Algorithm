T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # N은 인덱스 길이, M은 추가할 횟수, L은 내가 구하고 싶은 인덱스
    my_list = list(map(int, input().split()))
    for m in range(M):
        mid, value = map(int, input().split())
        left = my_list[:mid]
        right = my_list[mid:]
        my_list = left + [value] + right

    print('#{} {}'.format(tc, my_list[L]))

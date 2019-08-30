T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    dump = [0] * N  # 화덕 공간 / 0인덱스는 쓰지 않음

    pizza = [0] + list(map(int, input().split()))  # 인덱스 안에 번호에 피자

    for i in range(N):

        dump[i] = [pizza[i + 1], i + 1]
    print(dump)

    # while


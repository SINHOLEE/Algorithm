T = int(input())

for t in range(1, T+1):

    a = list(map(int,input().split()))
    K, N, M = a[0], a[1], a[2] # k:최대이동거리, N :종점 정류장, M : 충전기 대수
    charger = list(map(int,input().split()))

    movable = K  # 3
    location = 0
    count = 0
    while location + movable != N:
        if movable == 0:
            count = 0
            break
        else:
            if location + movable in charger:
                location += movable
                count += 1
                movable = K
                # print(location, count)
            else:
                movable -= 1

    print('#{} {}'.format(t,count))

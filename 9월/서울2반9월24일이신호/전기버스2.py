
def move(location, result):
    global min_count, N, count
    count += 1
    if location >= N - 1:
        if min_count > result:
            min_count = result
        return
    if result > min_count:
        return
    power = bus_stops[location]
    for i in range(power, -1, -1):
        if i == 0:
            break
        if location + i > N -1:
            continue

        move(location + i, result + 1)


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    count = 0
    bus_stops = arr[1:]
    min_count = 1000000000000000000000
    move(0, -1)
    print('#%s %s %s' % (tc,min_count,count))

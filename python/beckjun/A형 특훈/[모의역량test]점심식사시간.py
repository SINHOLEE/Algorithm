T = int(input())
def find_time(distances, k):
    if len(distances) == 0:
        return 0
    total = 0
    distances = sorted(distances)
    queue = [] # 3개까지 들어갈 수 있다.
    while True:
        if len(distances) == 0:
            total += max(queue)
            break
        distances = list(map(lambda x:x-1, distances))
        queue = list(map(lambda x:x -1, queue ))
        while True:
            if len(queue) == 0:
                break
            if queue[0] != 0:
                break
            queue.pop(0)

        while True:
            # print(distances)
            if len(distances) == 0:
                break
            if len(queue) >= 3:
                break
            if distances[0] > -1:
                break

            distances.pop(0)
            queue.append(k)


        total += 1
    return total

def make_subset(a, b, depth):
    global min_time
    if depth == people_len:
        # a, b 는 좌표들
        if len(a) != 0:
            a_distances = list(map(lambda x:abs(x[0] - k_data[0][0]) + abs(x[1] - k_data[0][1]) ,a))
        else:
            a_distances = []
        if len(b) != 0:
            b_distances = list(map(lambda x:abs(x[0] - k_data[1][0]) + abs(x[1] - k_data[1][1]),b))
        else:
            b_distances = []
        aaa = find_time(a_distances, k_data[0][2])
        bbb = find_time(b_distances, k_data[1][2])
        res = max(aaa, bbb)
        if min_time > res:
            min_time = res
        return
    make_subset(a+[people[depth]], b, depth+1)
    make_subset(a, b+[people[depth]], depth+1)

for t in range(1, T+1):
    n = int(input())
    people = []
    k_data= [] # (x1,y1, 거리1) ,(x2, y2, 거리2)
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            if temp[j] == 1:
                people.append((i, j))
            elif temp[j] >= 2:
                k_data.append((i, j, temp[j]))
    # print(people)
    people_len = len(people)
    # print(k_data)
    min_time = 987654321
    visited = [False] * people_len
    make_subset([],[],0)
    print('#%s %s' % (t, min_time))
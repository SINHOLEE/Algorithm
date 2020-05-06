import sys
sys.setrecursionlimit(1500)


def find(x):
    global parent
    if parent.get(x) is None:
        parent[x] = x
        return x

    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global parent
    # 둘중에 작은애가 큰 애로 갈거임.
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[x] = y


def solution(k, room_number):
    global parent
    answer = []
    for num in room_number:
        answer.append(find(num))
        union(parent[num], parent[num]+1)
    return answer


parent = {}
solution(10 ** 12, [10**12-200000+1] * 200000)

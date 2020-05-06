# union find


def find(x):
    global parent
    if parent[x] == 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def solution(k, room_number):
    global parent
    parent = [0] * (k+1)
    answer = [0] * len(room_number)
    i = 0
    for num in room_number:
        if parent[num] == 0:
            answer[i] = num
            parent[num] = find(num+1)
        else:
            answer[i] = find(num)
            parent[answer[i]] = find(answer[i]+1)
        # union(num, parent[num]+1)
        i+=1
    return answer

parent = []
solution(10, [1,1,1,5,4,1,2])

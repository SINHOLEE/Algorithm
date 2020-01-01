import heapq

v,e,p = map(int,input().split())

adj_mat = [[987654321] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,w = map(int, input().split())

    adj_mat[a][b] = w
    adj_mat[b][a] = w

#1 건우 구한 후 마산가는 길
key1 = [(987654321,i) for i in range(v+1) ]
key1[1] = (0, 1)
visited1 = [0] * (v+1)
hq = [key1[1]]
one_to_gunwoo_to_masan = 0
#1.1 건우 구하기
while hq:
    dis, node = heapq.heappop(hq)
    if node == p:
        break
    visited1[node] = 1
    for w in range(1, v+1):
        if adj_mat[node][w] != 987654321:
            if not visited1[w]:
                if key1[w][0] >= dis + adj_mat[node][w]:
                    temp = (dis+adj_mat[node][w], w)
                    key1[w] = temp
                    heapq.heappush(hq, temp)
# print(key1)
# print(visited1)
hq = [key1[p]]
# 마산가기
while hq:
    dis, node = heapq.heappop(hq)
    if node == v:
        one_to_gunwoo_to_masan = dis
        break
    visited1[node] = 1
    for w in range(1, v+1):
        if adj_mat[node][w] != 987654321:
            if not visited1[w]:
                if key1[w][0] >= dis + adj_mat[node][w]:
                    temp = (dis+adj_mat[node][w], w)
                    key1[w] = temp
                    heapq.heappush(hq, temp)

#2 바로 마산가는 길

key2 = [(987654321, i ) for i in range(v+1)]
key2[1] = (0, 1)
hq = [key2[1]]
visited2 = [0] * (v+1)
one_to_masan = 0
while hq:
    dis, node = heapq.heappop(hq)
    if node == v:
        one_to_masan = dis
        break
    visited2[node] = 1
    for w in range(1, v+1):
        if adj_mat[node][w] != 987654321:
            if not visited2[w]:
                if key2[w][0] >= dis + adj_mat[node][w]:
                    temp = (dis+adj_mat[node][w], w)
                    key2[w] = temp
                    heapq.heappush(hq, temp)

if one_to_gunwoo_to_masan == one_to_masan:
    print('SAVE HIM')
else:
    print('GOOD BYE')

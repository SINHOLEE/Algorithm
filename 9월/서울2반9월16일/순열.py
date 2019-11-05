# arr = [3, 1, 6, 4]
#
# def perm(r):
#     global count
#     count+= 1
#     if len(arr) == r:
#         print(temp, 'count = ',count)
#         return
#     for j in range(len(arr)):
#         if visited[j] == False:
#             visited[j] = True
#             temp[r] = arr[j]
#             perm(r + 1)
#             visited[j] = False
#
#
# visited = [False] * len(arr)
# temp = [0] * len(arr)
# count = 0
# perm(0)

def perm(depth, temp):
    if depth == 3:
        print(temp)
        return
    for i in range(3):
        # if i == 1:
        #     continue
        temp[depth], temp[i] = temp[i], temp[depth]
        perm(depth+1, temp)
        temp[depth], temp[i] = temp[i], temp[depth]
perm(0, [0,1,2])
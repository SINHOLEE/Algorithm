# def combi(n, r):
#     global count
#     if r == 0:
#         count += 1
#         print(count)
#         return
#     elif n < r:
#         return
#     else:
#         tr[r - 1] = arr[n - 1]
#         combi(n-1, r-1)
#         combi(n-1, r)
#
# n = 24
# r = 12
#
# arr = list(range(1, 25))
#
# tr = [0] * r
# count = 0
# combi(n, r)
#
# print(count)
arr = [3, 1, 6,4,1]
#
# def perm(a, tem):
#     if len(tem) == len(arr):
#         print(tem)
#         return
#     for j in range(len(arr)):
#         if visited[j] == False:
#             visited[j] = True
#             # temp.append(arr[j])
#             perm(a+1,tem )
#             # temp.pop()
#             visited[j] = False
#
#
# visited = [False] * len(arr)
# temp = [0] * len(arr)
#
# perm(-1, 4)
r= 0

def combi(a, r):
    global count
    count += 1
    if len(temp) == r:
        print(temp)
        return
    for j in range(a, len(arr)):
        if visited[j] == False:
            visited[j] = True
            temp.append(arr[j])
            combi(j, r)
            temp.pop()
            visited[j] = False


visited = [False] * len(arr)
temp = []
count = 0
for i in range(len(arr)):
    visited[i] = True
    temp.append(arr[i])
    combi(i, r)
    temp.pop()
    visited[i] = False
print(count)
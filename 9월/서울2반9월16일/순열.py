arr = [3, 1, 6, 4]

def perm(r):
    global count
    count+= 1
    if len(arr) == r:
        print(temp, 'count = ',count)
        return
    for j in range(len(arr)):
        if visited[j] == False:
            visited[j] = True
            temp[r] = arr[j]
            perm(r + 1)
            visited[j] = False


visited = [False] * len(arr)
temp = [0] * len(arr)
count = 0
perm(0)
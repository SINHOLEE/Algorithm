di = [0,1]
dj = [1,0]

def dfs(x,y,res, op):
    global max_res, min_res
    if x == n-1 and y == n-1:
        if max_res < res:
            max_res = res
        if min_res > res:
            min_res = res

        return
    for k in range(2):
        newX, newY = x+di[k], y+dj[k]
        if 0<= newX<n and 0<= newY<n:
            if op == 0:
                dfs(newX, newY, res , mat[newX][newY])
            elif op == '+':
                dfs(newX,newY,res+int(mat[newX][newY]), 0)
            elif op == '*':
                dfs(newX,newY,res*int(mat[newX][newY]), 0)
            else:
                dfs(newX,newY,res-int(mat[newX][newY]), 0)
n = int(input())

mat = [list(map(str, input().split())) for _ in range(n)]

max_res = -99999
min_res = 99999
dfs(0, 0, int(mat[0][0]),0)

print('%s %s' % (max_res, min_res))
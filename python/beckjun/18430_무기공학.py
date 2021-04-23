#6:56

def main(N,M,mat):
    global answer
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    answer = 0
    visited = [[0]*M for _ in range(N)]

    def calc_strength(i,j,ay,ax,by,bx):
        return mat[i][j]*2 + mat[ay][ax] + mat[by][bx]
    
    def backtracking(si,sj, res):
        global answer
        answer = max(answer, res)
        for i in range(N):
            for j in range(M):
                if i<si: continue
                if i==si and j<sj: continue
                for k in range(4):
                    a_wing = k
                    b_wing = (k+1)%4
                    ay,ax = i+dy[a_wing], j+dx[a_wing]
                    by,bx = i+dy[b_wing], j+dx[b_wing]
                    
                    # 현재 위치가 visited면 continue
                    if (visited[i][j]):continue
                    # 날개가 outofbound이면 continue
                    if not (0<=ay<N and 0<=ax<M):continue
                    if not (0<=by<N and 0<=bx<M):continue
                    # 날개에 visited가 있으면 continue
                    if(visited[ay][ax] or visited[by][bx]): continue
                    visited[i][j] = 1
                    visited[ay][ax] = 1
                    visited[by][bx] = 1
                    backtracking(i,j,res+calc_strength(i,j,ay,ax,by,bx))
                    visited[i][j] = 0
                    visited[ay][ax] = 0
                    visited[by][bx] = 0
    backtracking(0,0,0)
    return answer

if __name__ == '__main__':
    N,M = map(int,input().split(" "))
    mat = [[*map(int, input().split(" "))] for _ in range(N)]
    
    print(main(N, M, mat))
    
class Solution:
    sy = sx = ey = ex = n = m = zero_cnt = 0
    visited = []
    grid = []

    def dfs(self, y, x, walk, cnt1):
        near = ((1, 0), (0, 1), (-1, 0), (0, -1))
        cnt = 0
        if y == self.ey and x == self.ex and walk == self.zero_cnt + 1:
            return 1
        for dy, dx in near:
            yy, xx = y+dy, x+dx
            if not(0 <= yy < self.n and 0 <= xx < self.m):
                continue
            if self.visited[yy][xx]:
                continue
            if self.grid[yy][xx] == -1:
                continue
            self.visited[yy][xx] = 1
            cnt += self.dfs(yy, xx, walk+1, cnt1)
            self.visited[yy][xx] = 0

        return cnt

    def uniquePathsIII(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 0:
                    self.zero_cnt += 1
                if grid[i][j] == 1:
                    self.sy, self.sx = i, j
                if grid[i][j] == 2:
                    self.ey, self.ex = i, j

        self.visited = [[0] * self.m for _ in range(self.n)]
        self.visited[self.sy][self.sx] = 1
        cnt = self.dfs(self.sy, self.sx, 0, 0)

        return cnt

s = Solution()
print(s.uniquePathsIII( [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
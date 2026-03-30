class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            for dr, dc in directs:
                dfs(r + dr, c + dc)
            

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
            
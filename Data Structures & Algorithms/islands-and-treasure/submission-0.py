class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = True

        step = 0
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = step
                for dr, dc in directs:
                    newr = r + dr
                    newc = c + dc
                    if 0 <= newr < m and 0 <= newc < n and visited[newr][newc] == False and grid[newr][newc] != -1:
                        q.append((newr, newc))
                        visited[newr][newc] = True

            step += 1


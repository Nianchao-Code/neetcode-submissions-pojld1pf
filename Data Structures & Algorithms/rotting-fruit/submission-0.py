class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0

        while q:
            if fresh == 0:
                break

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in direction:
                    newr = r + dr
                    newc = c + dc
                    if 0 <= newr < m and 0 <= newc < n and grid[newr][newc] == 1:
                        q.append((newr, newc))
                        grid[newr][newc] = 2
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1



        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x = p[0]
            y = p[1]
            heapq.heappush(heap, (x * x + y * y, x, y))

        res = []

        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            
            if first == second:
                continue

            new_weight = first - second
            heapq.heappush(stones, -new_weight)

        return -stones[0] if stones else 0
            


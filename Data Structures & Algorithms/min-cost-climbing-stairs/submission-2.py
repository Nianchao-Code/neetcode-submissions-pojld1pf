class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev1 = 0
        prev2 = min(cost[0], cost[1])
        if n == 2:
            return prev2

        for i in range(3, n + 1):
            cur = min(prev2 + cost[i - 1], prev1 + cost[i - 2])
            prev1 = prev2
            prev2 = cur

        return cur
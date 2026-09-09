class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float("inf")
        res = 0

        for p in prices:
            cur_min = min(cur_min, p)
            res = max(res, p - cur_min)

        return res

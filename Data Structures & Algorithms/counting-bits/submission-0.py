class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            r = 0
            while i:
                i &= i-1
                r += 1
            res.append(r)
        return res
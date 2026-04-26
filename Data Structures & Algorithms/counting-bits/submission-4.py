class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def cnt(num):
            res = 0
            while num:
                if num & 1 == 1:
                    res += 1
                num >>= 1
            return res
        
        res = []
        for i in range(n + 1):
            res.append(cnt(i))

        return res
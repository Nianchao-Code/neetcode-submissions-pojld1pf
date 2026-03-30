class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for m in dic.values():
            if m > 1:
                return True
        return False
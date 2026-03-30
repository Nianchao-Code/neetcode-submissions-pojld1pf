class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from numpy import prod
        res = []
        for i in range(len(nums)):
            tempt = 0
            tempt = nums[i]
            nums.remove(nums[i])
            res.append(prod(nums))
            nums.insert(i, tempt)
        return res




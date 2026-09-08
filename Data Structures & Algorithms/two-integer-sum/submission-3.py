class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i, num in enumerate(nums):
            if target - num in dict1:
                return [dict1[target - num], i]
            dict1[num] = i

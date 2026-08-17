class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i, num in enumerate(nums):
            if target - num not in dict1:
                dict1[num] = i
            else:
                return [dict1[target - num], i]

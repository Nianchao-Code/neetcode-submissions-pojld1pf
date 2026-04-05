class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 in nums_set:
                continue
            start = num
            length = 0
            while start in nums_set:
                start += 1
                length += 1
            ans = max(ans, length)
        return ans


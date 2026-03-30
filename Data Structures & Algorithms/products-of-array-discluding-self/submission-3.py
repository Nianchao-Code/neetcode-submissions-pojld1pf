class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_lst = [1] * n
        suffix_lst = [1] * n

        for i in range(1, n):
            prefix_lst[i] = prefix_lst[i - 1] * nums[i - 1]

        for j in range(n - 2, -1, -1):
            suffix_lst[j] = suffix_lst[j + 1] * nums[j + 1]

        for i in range(n):
            nums[i] = prefix_lst[i] * suffix_lst[i]

        return nums
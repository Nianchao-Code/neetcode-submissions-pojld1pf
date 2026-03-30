class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums[::-1]

        prefix_lst = nums.copy()
        suffix_lst = nums.copy()

        for i in range(1, len(prefix_lst)):
            if i > 1:
                prefix_lst[i] = prefix_lst[i - 1] * nums[i - 1]
            else:
                prefix_lst[i] = nums[i - 1]

        for j in range(len(suffix_lst) - 2, -1, -1):
            if j < len(suffix_lst) - 2:
                suffix_lst[j] = suffix_lst[j + 1] * nums[j + 1]
            else:
                suffix_lst[j] = nums[j + 1]

        nums[0] = suffix_lst[0]
        nums[-1] = prefix_lst[-1]
        for i in range(1, len(nums) - 1):
            nums[i] = suffix_lst[i] * prefix_lst[i]

        return nums
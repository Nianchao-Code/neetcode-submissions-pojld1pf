class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(len(nums) - 1):
            cur_p = prefix[-1] * nums[i]
            prefix.append(cur_p)

        suffix = [1]
        for i in range(len(nums) - 1, 0, -1):
            cur_p = suffix[-1] * nums[i]
            suffix.append(cur_p)

        suffix = suffix[::-1]
        return [x * y for x, y in zip(prefix, suffix)]
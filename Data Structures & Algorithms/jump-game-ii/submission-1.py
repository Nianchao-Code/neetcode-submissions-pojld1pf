class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        cur_end = 0
        cur_farthest = 0

        for i in range(len(nums) - 1):
            num = nums[i]
            cur_farthest = max(cur_farthest, i + num)

            if i == cur_end:
                steps += 1
                cur_end = cur_farthest

        return steps
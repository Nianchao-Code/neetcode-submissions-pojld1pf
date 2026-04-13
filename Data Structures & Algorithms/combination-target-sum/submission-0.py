class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, cursum):
            if cursum == target:
                res.append(path[:])
                return

            if cursum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, cursum + nums[i])
                path.pop()

        backtrack(0, 0)
        return res
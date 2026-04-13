class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, cursum):
            if cursum == target:
                res.append(path[:])
                return
            
            if cursum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, cursum + candidates[i])
                path.pop()

        backtrack(0, 0)
        return res
            
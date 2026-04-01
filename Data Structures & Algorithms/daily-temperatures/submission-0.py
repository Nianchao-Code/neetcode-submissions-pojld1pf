class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, poped_index = stack.pop()
                res[poped_index] = i - poped_index
            stack.append((t, i))

        return res

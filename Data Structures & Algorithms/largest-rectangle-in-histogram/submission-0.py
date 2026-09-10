class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                left_i, height = stack.pop()
                res = max(res, height * (i - left_i))
                start = left_i

            stack.append((start, h))

        right = len(heights)

        for i, h in stack:
            res = max(res, h * (right - i))

        return res





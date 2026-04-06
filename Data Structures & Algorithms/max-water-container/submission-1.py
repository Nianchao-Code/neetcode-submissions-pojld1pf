class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        
        res = 0
        while left < right:
            width = right - left
            res = max(res, width * min(heights[left], heights[right]))
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return res
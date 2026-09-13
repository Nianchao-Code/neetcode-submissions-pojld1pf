class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if n < m:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        left = 0
        right = m
        half = (m + n + 1) // 2

        while left <= right:
            i = (right - left) // 2 + left
            j = half - i

            nums1_left = nums1[i - 1] if i >= 1 else -float("inf")
            nums1_right = nums1[i] if i < m else float("inf")
            nums2_left = nums2[j - 1] if j >= 1 else -float("inf")
            nums2_right = nums2[j] if j < n else float("inf")

            if nums2_right >= nums1_left and nums1_right >= nums2_left:
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

            elif nums2_left > nums1_right:
                left = i + 1

            else:
                right = i - 1



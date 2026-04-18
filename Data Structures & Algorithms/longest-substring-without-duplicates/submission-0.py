class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        char_cnt = set()

        for right in range(len(s)):
            while s[right] in char_cnt:
                char_cnt.remove(s[left])
                left += 1

            char_cnt.add(s[right])
            res = max(res, right - left + 1)

        return res

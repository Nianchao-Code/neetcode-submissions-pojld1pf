class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxfreq = 0
        res = 0
        left = 0
        cnt = {}

        for right in range(len(s)):
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            maxfreq = max(maxfreq, cnt[s[right]])

            while right - left + 1 - maxfreq > k:
                cnt[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
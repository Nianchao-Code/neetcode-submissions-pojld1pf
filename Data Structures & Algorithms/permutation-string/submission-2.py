class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = Counter(s1)
        s2_cnt = {}

        left, right = 0, 0
        while right < len(s2):
            char = s2[right]
            if char not in s1_cnt:
                s2_cnt = {}
                right += 1
                left = right
                continue

            s2_cnt[char] = s2_cnt.get(char, 0) + 1
            while s2_cnt[char] > s1_cnt[char]:
                s2_cnt[s2[left]] -= 1
                left += 1
            
            if s2_cnt == s1_cnt:
                return True
            
            right += 1

        return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        window = defaultdict(int)
        k = len(s1)

        if k > len(s2):
            return False

        for i in range(len(s2)):
            window[s2[i]] += 1

            if i >= k:
                window[s2[i - k]] -= 1
                if window[s2[i - k]] == 0:
                    del window[s2[i - k]]

            if window == cnt1:
                return True

        return False
                


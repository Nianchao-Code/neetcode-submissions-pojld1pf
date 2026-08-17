class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            cnt = [0] * 26
            for char in s:
                cnt[ord(char) - ord("a")] += 1
            group[tuple(cnt)].append(s)

        return list(group.values())
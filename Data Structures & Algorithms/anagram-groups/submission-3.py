class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for s in strs:
            cnt_s = [0] * 26
            for char in s:
                cnt_s[ord(char) - ord("a")] += 1
            dict1[tuple(cnt_s)].append(s)
        
        return list(dict1.values())
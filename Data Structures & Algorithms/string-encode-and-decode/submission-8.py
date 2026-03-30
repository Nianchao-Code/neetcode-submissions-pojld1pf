class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        print(s)

        while i < len(s):
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            num_len = j - i
            j += (length + 1)
            res.append(s[i+num_len+1:j])
            i = j
        return res


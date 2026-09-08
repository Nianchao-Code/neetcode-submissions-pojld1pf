class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        num = 0
        i = 0

        while i < len(s):
            while s[i].isdigit():
                num = 10 * num + int(s[i])
                i += 1
            output.append(s[i + 1: i + 1 + num])
            i += num + 1
            num = 0

        return output




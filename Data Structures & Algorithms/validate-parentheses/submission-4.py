class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_p = {"]": "[", ")": "(", "}": "{"}

        for p in s:
            if stack and p in dict_p:
                if dict_p[p] != stack.pop():
                    return False
            else:
                stack.append(p)

        return not stack
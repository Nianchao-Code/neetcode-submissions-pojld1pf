class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {")": "(", "]": "[", "}": "{"}
        stack = []

        for p in s:
            if p in ["}", "]", ")"]:
                if not stack or stack[-1] != open_to_close[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)

        return True if not stack else False

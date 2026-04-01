class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = []

        for p in s:
            if p in close_to_open:
                if not stack or stack[-1] != close_to_open[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)

        return True if not stack else False

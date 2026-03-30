class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            else:
                if stack and stack[-1] == Map[c]:
                    stack.pop()
                else:
                    return False
        return not stack
            

        

        

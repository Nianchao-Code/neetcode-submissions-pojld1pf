class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(open, close):
            if len(path) == n * 2:
                res.append("".join(path[:]))
                return

            if open < n:
                path.append("(")
                backtrack(open + 1, close)
                path.pop()

            if open > close:
                path.append(")")
                backtrack(open, close + 1)
                path.pop()

        backtrack(0, 0)
        return res

            
            

            
            
            
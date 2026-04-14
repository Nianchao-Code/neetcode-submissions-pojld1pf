class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        res = []
        path = []
        def backtrack(start):
            if start == len(digits):
                res.append("".join(path))
                return

            for ch in digit_to_letter[digits[start]]:
                path.append(ch)
                backtrack(start + 1)
                path.pop()

        backtrack(0)
        return res if res[0] != "" else []

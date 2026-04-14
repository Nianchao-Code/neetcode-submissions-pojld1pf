class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(str1):
            return str1 == str1[::-1]

        res = []
        path = []
        def backtrack(start):
            if start == len(s):
                res.append(path[:])

            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res



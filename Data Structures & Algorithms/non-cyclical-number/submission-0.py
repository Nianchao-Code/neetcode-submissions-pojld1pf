class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {n}

        def happy_convert(num):
            output = 0
            while num != 0:
                output += pow(num % 10, 2)
                num //= 10
            return output

        while n != 1:
            n = happy_convert(n)
            if n in visited:
                return False
            visited.add(n)

        return True
            
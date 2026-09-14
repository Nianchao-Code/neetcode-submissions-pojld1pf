class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = {n}

        def helper(num):
            output = 0
            while num > 0:
                digit = num % 10
                output += pow(digit, 2)
                num //= 10
            return output

        while n != 1:
            n = helper(n)
            if n in num_set:
                return False

            num_set.add(n)

        return True
class Solution:
    def reverse(self, x: int) -> int:
        min = -2**31
        max = 2**31 - 1

        is_negative = 0

        if x == min:
            return 0

        if x < 0:
            is_negative = 1
            x = -x
        
        res = 0
        while x:
            digit = x % 10
            x = x // 10

            if res > max // 10 or (res == max // 10 and digit > max % 10):
                return 0
            res = res * 10 + digit
        
        return res if is_negative == 0 else -res
        

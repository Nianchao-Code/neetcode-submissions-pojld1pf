class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            new_d = total % 10
            carry = total // 10

            digits[i] = new_d

        return [1] + digits if carry == 1 else digits
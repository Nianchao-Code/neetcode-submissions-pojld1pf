class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        val = 0

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                temp = num[i : i + 3]
                if val <= int(temp):
                    val = int(temp)
                    res = temp

        return res


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            num2 = target - numbers[i]
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (right - left) // 2 + left
                if numbers[mid] == num2:
                    return [i + 1, mid + 1]
                elif numbers[mid] < num2:
                    left = mid + 1
                else:
                    right = mid - 1

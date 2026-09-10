class TimeMap:

    def __init__(self):
        self.dict1 = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict1[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        time_value = self.dict1[key]
        left = 0
        right = len(time_value) - 1
        res = ""

        while left <= right:
            mid = (right - left) // 2 + left
            t = time_value[mid][0]
            if t > timestamp:
                right = mid - 1
            else:
                res = time_value[mid][1]
                left = mid + 1

        return res
        

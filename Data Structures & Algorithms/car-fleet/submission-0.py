class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_to_s = []
        stack = []

        for p, s in zip(position, speed):
            p_to_s.append((p, s))

        p_to_s.sort(key = lambda x: x[0], reverse = True)

        res = 0
        for p, s in p_to_s:
            if stack:
                prev_p, prev_s = stack.pop()
                if prev_s >= s or (target - prev_p) / prev_s < (target - p) / s:
                    res += 1
                    stack.append((p, s))
                else:
                    stack.append((prev_p, prev_s))
            else:
                stack.append((p, s))
        
        return res + 1
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(p, s) for p, s in zip(position, speed)]
        position_speed.sort(key = lambda x: x[0])

        stack = []
        for p, s in position_speed:
            t = (target - p) / s
            while stack and stack[-1] <= t:
                stack.pop()

            stack.append(t)

        return len(stack)
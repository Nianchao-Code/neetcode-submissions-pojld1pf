class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        m_stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]

            while m_stack and temperatures[m_stack[-1]] < t:
                j = m_stack.pop()
                res[j] = i - j
            
            m_stack.append(i)

        return res
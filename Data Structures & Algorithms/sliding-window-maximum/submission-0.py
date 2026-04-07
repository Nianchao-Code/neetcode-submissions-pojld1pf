class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m_q = deque()
        left = 0
        res = []

        for right in range(len(nums)):
            while m_q and nums[m_q[-1]] <= nums[right]:
                m_q.pop()
            
            m_q.append(right)

            if right - left + 1 > k:
                if m_q[0] <= left:
                    m_q.popleft()
                left += 1

            if right >= k - 1:
                res.append(nums[m_q[0]])

        return res
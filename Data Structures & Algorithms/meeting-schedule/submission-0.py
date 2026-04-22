"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals) - 1):
            cur_i = intervals[i]
            next_i = intervals[i + 1]

            if cur_i.end > next_i.start:
                return False

        return True
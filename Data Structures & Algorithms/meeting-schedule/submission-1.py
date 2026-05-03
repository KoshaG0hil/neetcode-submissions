"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        prev_time=intervals[0]

        for i in intervals[1:]:
            if i.start < prev_time.end:
                return False
            prev_time= i

        return True

        
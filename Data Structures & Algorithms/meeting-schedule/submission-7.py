"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedIntervals = sorted(intervals, key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            i1 = sortedIntervals[i - 1]
            i2 = sortedIntervals[i]

            if i1.end > i2.start:
                return False
        return True
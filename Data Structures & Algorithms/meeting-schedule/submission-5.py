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
        next_meeting_index = 1
        for i in range(len(sortedIntervals)-1):
            first_meeting = sortedIntervals[i]
            while (next_meeting_index < len(sortedIntervals)):
                next_meeting = sortedIntervals[next_meeting_index]
                if first_meeting.end > next_meeting.start:
                    return False
                next_meeting_index += 1
            next_meeting_index = 0
            next_meeting_index = i + 2
        return True
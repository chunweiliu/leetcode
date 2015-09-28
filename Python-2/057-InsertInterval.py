# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # Assume all intervals are non-overlapping.
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key=lambda interval: interval.start)

        ans = []
        candidate = intervals[0]
        for i in range(1, len(intervals)):
            if candidate.start <= intervals[i].start <= candidate.end:
                # Merge the overlap intervals.
                candidate.end = max(intervals[i].end, candidate.end)
            else:
                # Insert new candidate.
                ans.append(candidate)
                candidate = intervals[i]
        ans.append(candidate)
        return ans

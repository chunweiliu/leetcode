# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # Sort the itervals with their start element. Merge the near by
        # interval if its start is in the range of the current one.
        if not intervals:
            return intervals

        # Sort the intervals.
        intervals.sort(key=lambda interval: interval.start)

        # Merge the intervals.
        ans = []
        candidate = intervals[0]
        for i in range(1, len(intervals)):
            if candidate.start <= intervals[i].start <= candidate.end:
                # Need to merge
                candidate.end = max(intervals[i].end, candidate.end)
            else:
                ans.append(candidate)
                candidate = intervals[i]
        # Once the last intervals updated, it need to be appended.
        ans.append(candidate)
        return ans


if __name__ == '__main__':
    print Solution().merge(
        [Interval(2, 6), Interval(1, 3), Interval(8, 10), Interval(9, 18)])

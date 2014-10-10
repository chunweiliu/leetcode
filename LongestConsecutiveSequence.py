class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        """Hash table keep the longest.
        If the key is a lower interval, than the value is the upper.
        If the key is an upper interval, than the value is the lower.
        (two directions counts)
        Time: O(n)
        Space: O(k)
        Corner: len(num) == 0
        """
        if len(num) == 0:
            return None

        intervals = dict()
        for i in num:
            if i in intervals:
                continue

            lower = intervals[i - 1] if i - 1 in intervals else i
            upper = intervals[i + 1] if i + 1 in intervals else i

            intervals[i] = i  # so we don’t want duplicates
            intervals[lower] = upper  # both directions count
            intervals[upper] = lower

        return max(abs(lower-upper) + 1
                   for (lower, upper) in intervals.iteritems())

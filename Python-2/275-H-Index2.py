class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Given a sorted array, it usually existed a O(logn) solution.
        # Otherwise, we can sort the input in O(nlogn) and propose some O(n).

        # At least n - m papaer was cited n - m times:
        # c0, c1, ... cm, ... cn-1
        #  1,  1, ...n-m, ... whatever
        n = len(citations)
        l, r = 0, n  # Start from n then use r = m for shifting left.
        while l < r:
            m = l + (r - l) / 2
            if citations[m] == n - m:
                return n - m

            if citations[m] > n - m:
                r = m
            else:
                l = m + 1
        return n - l

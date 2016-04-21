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
        i, j = 0, n - 1
        while i <= j:
            m = i + (j - i) / 2
            num_paper = n - m  # The number of top cited paper.
            if citations[m] == num_paper:
                return num_paper

            if citations[m] > num_paper:
                j = m - 1
            else:
                i = m + 1
        return n - i

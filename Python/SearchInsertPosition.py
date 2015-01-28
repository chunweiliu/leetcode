class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        """Binary search and record a candidate
        Time: O(log n)
        Space: O(1)
        """
        if not A:
            return None

        candidate = 0
        start, end = 0, len(A) - 1
        while start <= end:
            middle = (start + end) / 2
            if A[middle] == target:
                return middle
            elif A[middle] < target:
                start = middle + 1
                candidate = start
            else:
                end = middle - 1
        return candidate

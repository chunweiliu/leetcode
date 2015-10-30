class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Use new framework of binary search.
        # 1. start and end are two bundary that outside the solution.
        # 2. Hold the loop invariant.

        start, end = -1, x + 1  # For searching the range [0, x]
        while end - start > 1:
            mid = (end - start) / 2 + start
            mid_square = mid * mid
            if mid_square == x:
                return mid
            if mid_square < x:  # start * start < x
                start = mid
            else:
                end = mid
        return start


if __name__ == '__main__':
    print Solution().mySqrt(1)

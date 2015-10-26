class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count == 1

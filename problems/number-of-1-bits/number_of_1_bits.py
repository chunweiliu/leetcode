class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        Bit the n & (n - 1) operation to clean up least significant bits.
        Example:
            110110
            110101
            ------
            110100
        """
        ones = 0
        while n:
            n &= (n - 1)
            ones += 1
        return ones    
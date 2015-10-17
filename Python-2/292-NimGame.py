class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Who take n - 1, n - 2, n - 3 will lose.
        return True if n % 4 else False

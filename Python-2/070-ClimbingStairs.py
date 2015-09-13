class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        stair = [0] * n
        stair[0] = 1
        stair[1] = 2
        for i in range(2, n):
            stair[i] = stair[i - 1] + stair[i - 2]
        return stair[-1]

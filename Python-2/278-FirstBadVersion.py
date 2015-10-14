# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        good, bad = 1, n
        while good < bad:
            test = good + (bad - good) / 2
            if isBadVersion(test):
                bad = test
            else:
                good = test + 1
        return bad

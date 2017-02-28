class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exist = set()
        while n and n not in exist:
            if n == 1:
                return True

            exist.add(n)

            s = 0
            for d in map(int, str(n)):
                s += d ** 2
            n = s

        return False

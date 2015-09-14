class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Algo: Binary search for a right candidate between [0, x // 2]
        # Case: x == 1
        i, j = 0, x // 2 + 1
        candidate = 0
        while i <= j:
            m = i + (j - i) // 2
            square = m * m
            if square == x:
                return m
            if square < x:
                candidate = m
                i = m + 1
            else:
                j = m - 1
        return candidate

if __name__ == '__main__':
    print Solution().mySqrt(1)

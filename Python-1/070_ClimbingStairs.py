import unittest


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        """DP
        D[n] = D[n - 1] + D[n - 2]
        D[2] = 2
        D[1] = 1
        D[0] = 0
        """
        if n < 2:
            return 0 if n < 1 else 1
        D = [0] * n
        D[0] = 1
        D[1] = 2
        for i in range(2, n):
            D[i] = D[i - 1] + D[i - 2]
        return D[n - 1]


class Test(unittest.TestCase):
    def test_base(self):
        n = 0
        ans = 0
        self.assertEqual(Solution().climbStairs(n), ans)

    def test_base1(self):
        n = 1
        ans = 1
        self.assertEqual(Solution().climbStairs(n), ans)

    def test_base2(self):
        n = 2
        ans = 2
        self.assertEqual(Solution().climbStairs(n), ans)


if __name__ == '__main__':
    unittest.main()

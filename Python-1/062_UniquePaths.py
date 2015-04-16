import unittest


class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def uniquePaths(self, m, n):
        """DP: path[i, j] = path[i - 1, j - 1] + path[i - 1, j]
        """
        path = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                path[j] += path[j - 1]
        return path[n - 1] if path else 0


class Test(unittest.TestCase):
    def test_base(self):
        m, n = 0, 0
        ans = 0
        self.assertEqual(Solution().uniquePaths(m, n), ans)

    def test_base1(self):
        m, n = 1, 1
        ans = 1
        self.assertEqual(Solution().uniquePaths(m, n), ans)

    def test_base2(self):
        m, n = 2, 2
        ans = 2
        self.assertEqual(Solution().uniquePaths(m, n), ans)

    def test_base3(self):
        m, n = 3, 2
        ans = 3
        self.assertEqual(Solution().uniquePaths(m, n), ans)

if __name__ == '__main__':
    unittest.main()

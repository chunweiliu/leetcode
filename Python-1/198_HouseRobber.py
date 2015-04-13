import unittest


class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        """DP, S[n] = max(S[n-1], S[n-2] + a[n])
        Recursion: TLE
        Iteration: AC
        """
        if len(num) < 2:
            return 0 if not num else num[0]
        # a = self.rob(num[:-1])
        # b = self.rob(num[:-2]) + num[-1]
        # return a if a > b else b

        S = [0] * len(num)
        S[0] = num[0]
        S[1] = num[0] if num[0] > num[1] else num[1]
        for i in range(2, len(num)):
            a = S[i - 1]
            b = S[i - 2] + num[i]
            S[i] = a if a > b else b
        return S[-1]


class Test(unittest.TestCase):

    def test_base(self):
        num = []
        ans = 0
        self.assertEqual(Solution().rob(num), ans)

    def test_base1(self):
        num = [1]
        ans = 1
        self.assertEqual(Solution().rob(num), ans)

    def test_base2(self):
        num = [1, 2]
        ans = 2
        self.assertEqual(Solution().rob(num), ans)

    def test_recursive(self):
        num = [1, 2, 3]
        ans = 4
        self.assertEqual(Solution().rob(num), ans)

    def test_recursive2(self):
        num = [2, 1, 1, 2]
        ans = 4
        self.assertEqual(Solution().rob(num), ans)


if __name__ == '__main__':
    # unittest.main()
    num = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]

    import time
    start_time = time.time()
    Solution().rob(num)
    print time.time() - start_time

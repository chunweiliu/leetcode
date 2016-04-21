import math
import unittest


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Grouping: Each group has (n - 1)! members
        # 1 P(2, 3, 4)
        # 2 P(1, 3, 4)
        # 3 P(1, 2, 4)
        # 4 P(1, 2, 3)
        ans = ''
        digits = map(str, range(1, n + 1))
        k -= 1  # Adjust index to 0 base.
        while n > 0:
            n -= 1
            number_of_each_group = math.factorial(n)

            index, k = divmod(k, number_of_each_group)
            ans += digits.pop(index)
            # k -= i * number_of_each_group  # Equal to modualization.
        return ''.join(ans)

        # Use the built-in tool (TLE)
        # from itertools import permutations
        # return list(permutations(range(1, n + 1)))[k - 1]


class Test(unittest.TestCase):
    def test_case(self):
        n = 4
        k = 10
        from itertools import permutations
        expected = ''.join(map(str,
                               list(permutations(range(1, n + 1)))[k - 1]))
        solution = Solution().getPermutation(n, k)
        self.assertEqual(expected, solution)

if __name__ == '__main__':
    unittest.main()

import math
import unittest

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Use the built-in tool (TLE)
        # from itertools import permutations
        # return list(permutations(range(1, n + 1)))[k - 1]

        # # Apply the next large k times O(nk)
        # def next_large(n):
        #     pass
        # num = '123456789'[:n]
        # for _ in range(k):
        #     num = next_large(num)
        # return num

        # Grouping: Each group has (n - 1)! members
        # 1 P(2, 3, 4)
        # 2 P(1, 3, 4)
        # 3 P(1, 2, 4)
        # 4 P(1, 2, 3)
        ans = ''
        digits = map(str, range(1, n + 1))
        k -= 1
        while n > 0:
            number_of_each_group = math.factorial(n - 1)
            i = k // number_of_each_group
            ans += digits.pop(i)
            k -= (i + 1) * number_of_each_group
            n -= 1
        return ''.join(ans)


class Test(unittest.TestCase):
    def test_case(self):
        n = 3
        k = 2
        from itertools import permutations
        expected = ''.join(map(str,
                               list(permutations(range(1, n + 1)))[k - 1]))
        solution = Solution().getPermutation(n, k)
        self.assertEqual(expected, solution)

if __name__ == '__main__':
    unittest.main()

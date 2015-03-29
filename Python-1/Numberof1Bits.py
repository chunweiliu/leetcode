import unittest


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        """Should have a built-in function for bit count.
        1) shifting bits for the unsigned int n, Time: O(log n)
        """
        nbits = 0
        while n > 0:
            nbits += n % 2
            n = n >> 1
        return nbits


class Test(unittest.TestCase):

    def test_nbits(self):
        b = '00111001'
        n = int(b, 2)  # covert a binary string to decimal
        self.assertEqual(Solution().hammingWeight(n), 4)

if __name__ == '__main__':
    unittest.main()

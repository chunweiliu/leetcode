import unittest


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """Given a 32 bits unsigned integer
        1) using built-in string reverse -> (X) string has no reverse
        2) using slicing syntax -> (*) 0001 -> 1000
        """
        b = bin(n)[2:]  # get rid of '0b' in the front
        rb = b[::-1]
        rb = rb + '0' * (32 - len(rb))  # complement 32 bits
        return int(rb, 2)


class Test(unittest.TestCase):
    def test_rbits(self):
        b = '00000010100101000001111010011100'
        n = int(b, 2)
        rb = '00111001011110000010100101000000'
        rn = int(rb, 2)
        self.assertEqual(Solution().reverseBits(n), rn)


if __name__ == '__main__':
    unittest.main()

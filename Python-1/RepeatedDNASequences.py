import unittest


class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        """Find a pattern with at least 10 chars and repeated in the sequence
        DP, substring from N to 10
        1) start with finding the longest pattern, T: O(n^2) -> TLE
        """
        ret = []
        ndna = len(s) / 2
        while ndna > 9:
            for i in range(len(s) - ndna):
                pattern, position = s[i:i + ndna], i + ndna - 1
                if s.find(pattern, position) > 0:
                    ret.append(pattern)
            ndna = ndna - 1
        return ret


class Test(unittest.TestCase):
    def test_case1(self):
        s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
        expect = ['AAAAACCCCC', 'CCCCCAAAAA']
        self.assertEqual(Solution().findRepeatedDnaSequences(s), expect)

if __name__ == '__main__':
    unittest.main()

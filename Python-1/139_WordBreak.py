import unittest


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        """DP: t[i] = t[i - n] and s[i - n:i] in dict
        Assume the truth table t[i] keep the answer for the first i-th string.
        Then t[i] is true if t[i - n] is true, and s[i - n:i] is a word in dict
        """
        table = [False] * (len(s) + 1)
        table[0] = True
        for i in range(len(s) + 1):
            for word in dict:
                if i - len(word) >= 0 and table[i - len(word)] and \
                   s[i - len(word):i] == word:
                    table[i] = True
                    break
        return table[len(s)]


class Test(unittest.TestCase):
    def test_base(self):
        s = 'leetcode'
        dict = ['leet', 'code']
        ans = True
        self.assertEqual(Solution().wordBreak(s, dict), ans)

    def test_base1(self):
        s = 'leetcodes'
        dict = ['leet', 'code']
        ans = False
        self.assertEqual(Solution().wordBreak(s, dict), ans)

    def test_base2(self):
        s = 'cars'
        dict = ['car', 'ca', 'rs']
        ans = True
        self.assertEqual(Solution().wordBreak(s, dict), ans)


if __name__ == '__main__':
    unittest.main()

class Solution(object):
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type word_dict: Set[str]
        :rtype: bool
        """
        # Assume vaild[i] keeps the answer for the first i-th word. We have:
        # vaild[i] = vaild[j] if s[j:i] for j from 0 to longest word length.
        # O(n^2)
        valid = [False] * (len(s) + 1)
        valid[0] = True  # For corner case.

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                print s[j:i]
                if valid[j] and s[j:i] in word_dict:
                    valid[i] = True
                    break
        return valid[-1]


if __name__ == '__main__':
    s = 'leetcode'
    word_dict = {'leet', 'code'}
    print Solution().wordBreak(s, word_dict)

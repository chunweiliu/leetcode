class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = ''.join([c.lower() for c in s if c.isalnum()])
        # return s == s[::-1]

        i, j = 0, len(s) - 1
        while i <= j:
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                break
        if i > j:
            return True
        return False

if __name__ == '__main__':
    s = '1a2'
    print Solution().isPalindrome(s)

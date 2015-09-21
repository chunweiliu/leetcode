class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([c.lower() for c in s if c.isalnum()])
        return s == s[::-1]

        # TLE
        # def check(s, l, r):
        #     while 0 <= l and r < len(s):
        #         if s[l] == s[r]:
        #             l -= 1
        #             r += 1
        #         else:
        #             return False
        #     return True

        # simplified_s = ''
        # for c in s:
        #     if c.isalpha():
        #         simplified_s += c
        # s = simplified_s
        # n = len(s)
        # if n % 2 == 1:
        #     return check(s, n // 2, n // 2)
        # return check(s, n // 2 - 1, n // 2)

if __name__ == '__main__':
    s = '1a2'
    print Solution().isPalindrome(s)

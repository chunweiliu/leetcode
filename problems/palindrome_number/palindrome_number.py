class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def check_palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if l < 0 and r == len(s):
                return True
            return False

        s = str(x)
        n = len(s)
        if n % 2 == 1:
            return check_palindrome(s, n / 2, n / 2)
        return check_palindrome(s, n / 2 - 1, n / 2)

if __name__ == "__main__":
    print Solution().isPalindrome(1211)

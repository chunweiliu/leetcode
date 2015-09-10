class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for x in range(len(s)):
            s1 = self.check_palindrome(s, x, x)
            s2 = self.check_palindrome(s, x, x + 1)
            candidate = s1 if len(s1) > len(s2) else s2
            if len(candidate) > len(longest):
                longest = candidate
        return longest

    def check_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # When the loop invariant break, l and r have been advanced by 1.
        # Therefore, Adjust the index by l + 1 and r - 1.
        return s[l + 1:r]

if __name__ == "__main__":
    print Solution().longestPalindrome("abcba")

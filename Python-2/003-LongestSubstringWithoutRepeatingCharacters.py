class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # One pass, no look back
        longest = start = 0
        chars = dict()
        for i, char in enumerate(s):
            if char in chars:
                longest = max(longest, i - start)
                start = max(start, chars[char] + 1)
            chars[char] = i
        return max(longest, len(s) - start)

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("dvdf")

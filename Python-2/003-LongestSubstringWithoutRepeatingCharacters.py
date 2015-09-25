class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # One pass, no look back
        # q p x r j x k l t z y q
        # ^ ------- ^
        #       ^ ------------- ^
        # x ................... ^ (don't count since start > chars[char] + 1)
        #       start           i
        longest = start = 0
        chars = dict()
        for i, char in enumerate(s):
            if char in chars:
                # Stop counting and check how long the current length is.
                longest = max(longest, i - start)  # Not include the current.

                # Don't upgrade the start if it is smaller than the repeat char
                # Otherwise, you will include a duplicated char in the middle.
                start = max(start, chars[char] + 1)

            # Record the last possition for each character.
            chars[char] = i
        return max(longest, len(s) - start)

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("dvdf")

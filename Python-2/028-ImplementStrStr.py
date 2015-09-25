class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Time O(mn)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

        # One liner using built in function.
        # return haystack.find(needle)

        # KMP
        # Partial matching table: the longest lengh of the common string in the
        # prefix and the postfix of a neddle. If we didn't find the matching,
        # advance the curser based on the partial matching table.


if __name__ == '__main__':
    haystack = 'aa'
    needle = 'ab'
    print Solution().strStr(haystack, needle)

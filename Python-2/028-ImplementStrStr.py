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

        # Compute the prefix-surfix index for the needle
        index = [0] * len(needle)
        j, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[j]:
                index[i] = j + 1
                i += 1
                j += 1
            else:
                # Go back to check
                j = index[j - 1] if j else 0
                if j == 0:
                    index[i] = 0
                    i += 1

        # Search
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            print i, j, haystack[i], needle[j]
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = index[j - 1] if j else 0

        if j == len(needle):
            return i - j
        return -1


if __name__ == '__main__':
    haystack = 'aa'
    needle = 'ab'
    print Solution().strStr(haystack, needle)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Partial matching table: the longest lengh of the common string in the
        # prefix and the postfix of a neddle. If we didn't find the matching,
        # advance the curser based on the partial matching table.
        # def find_partial_matching_table():
        #     # Use closure.
        #     n = len(needle)
        #     partial_matching_table = [0] * n
        #     for i in range(1, n):
        #         # Update the i-th element in partial matching table
        #         substring = needle[:i]
        #         prefix, postfix = set(), set()
        #         for j in range(1, i):
        #             prefix.add((j, substring[:j]))
        #             postfix.add((i - j, substring[j:]))
        #         intersection = prefix & postfix
        #         if intersection:
        #             max_common_length, _ = max(intersection)
        #         else:
        #             max_common_length = 0
        #         partial_matching_table[i - 1] = max_common_length
        #     return partial_matching_table

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

        # One liner using built in function.
        # return haystack.find(needle)

if __name__ == '__main__':
    haystack = 'aa'
    needle = 'ab'
    print Solution().strStr(haystack, needle)

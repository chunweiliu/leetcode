class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Python built-in function.
        # words = s.split()
        # return len(words[-1]) if words else 0

        # Naive solution.
        # count = 0
        # i = 0
        # while i < len(s):
        #     if s[i] != ' ':
        #         count += 1
        #     else:
        #         # If find a new word then we update.
        #         while i < len(s) and s[i] == ' ':
        #             i += 1
        #         if i != len(s):
        #             count = 1
        #     i += 1
        # return count

        # Check the trailing space and get rid of it.
        tail = len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1

        count = 0
        i = 0
        while i <= tail:
            if s[i] != ' ':
                count += 1
            else:
                count = 0
            i += 1
        return count

if __name__ == '__main__':
    s = 'aa aaa  '
    print Solution().lengthOfLastWord(s)

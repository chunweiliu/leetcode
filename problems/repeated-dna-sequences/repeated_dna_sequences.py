class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]

        Find these string
        * 10 chars
        * repeated
        """
        STRING_LENGTH = 10

        seen = set()
        repeated = set()
        for i in range(len(s) - STRING_LENGTH + 1):
            substring = s[i:i + STRING_LENGTH]
            if substring not in seen:
                seen.add(substring)
            else:
                repeated.add(substring)
        return list(repeated)

s = "AAAAAAAAAAA"
print Solution().findRepeatedDnaSequences(s)

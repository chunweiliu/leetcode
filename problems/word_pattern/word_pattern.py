class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        # Cascaded screening: The length of text and pattern
        if len(pattern) != len(str):
            return False
        mapping = {}

        # Check the pattern to text is a one-to-one mapping
        for i, p in enumerate(pattern):
            if p not in mapping:
                mapping[p] = str[i]
        if len(mapping.keys()) != len(set(mapping.values())):
            return False

        # Check each word
        for i, p in enumerate(pattern):
            if mapping[p] != str[i]:
                return False

        return True

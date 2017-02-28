import string


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Example:
        'egg', 'add' => true
        'foo', 'bar' => false
        """
        return self.isomorphic_string(s) == self.isomorphic_string(t)

    def isomorphic_string(self, s):
        iso_str = []
        seen = {}
        
        for i, c in enumerate(s):
            if c not in seen:
                seen[c] = i
            iso_str.append(string.printable[seen[c]])
        return iso_str

s = 'egg'
t = 'aad'
print Solution().isIsomorphic(s, t)
        
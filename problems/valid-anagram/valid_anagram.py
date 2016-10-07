class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Hash sum (migth have collection)

        # Histogram
        from collections import defaultdict
        hist_s = defaultdict(lambda: 0)
        for c in s:
            hist_s[c] += 1

        hist_t = defaultdict(lambda: 0)
        for c in t:
            hist_t[c] += 1

        return hist_s == hist_t

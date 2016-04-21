import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        missing = len(t)

        l, r = 0, 0
        i = 0
        for j, c in enumerate(s, 1):  # The current window is s[i:j]
            missing -= 1 if need[c] > 0 else 0
            need[c] -= 1
            if not missing:  # Found the first window

                # Decrease the window, as long as need[s[i]] < 0.
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                # If right isn't set, set it
                if not r or j - i <= r - l:
                    l, r = i, j
        return s[l:r]

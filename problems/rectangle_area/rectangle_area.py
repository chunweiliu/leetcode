class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # Two rectangle areas - their intersection.
        union = (C - A) * (D - B) + (G - E) * (H - F)
        if C < E or A > G or B > H or D < F:
            return union

        left = max(A, E)
        bottom = max(B, F)
        right = min(C, G)
        up = min(D, H)
        return union - (right - left) * (up - bottom)

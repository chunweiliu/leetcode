class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two pointers. Neglect obsticles in the middle of i and j.
        #          level
        #  lower   |
        # _|_______|_
        #  i       j
        i, j = 0, len(height) - 1
        lower, level, water = 0, 0, 0
        while i < j:
            if height[i] < height[j]:
                lower = height[i]
                i += 1
            else:
                lower = height[j]
                j -= 1
            level = max(level, lower)
            water += level - lower
        return water

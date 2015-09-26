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
            # The level is always gather from lower.
            level = max(level, lower)
            water += level - lower
        return water

if __name__ == '__main__':
    height = [0, 1, 10, 0, 10, 100, 0]
    print Solution().trap(height)

class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #      
        #     __|__
        #    |  |  |
        # |  |  |  |
        # --------------------
        # 0  1  2  3 '4'
        max_area = 0
        height.append(0)  # So we can advance the index in the end.

        i = 0
        stack = []
        while i < len(height):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                max_area = max(max_area,
                               height[top] * (i if not stack else
                                              i - stack[-1] - 1))
        return max_area

if __name__ == '__main__':
    height = [1, 2, 3, 2]
    print Solution().largestRectangleArea(height)

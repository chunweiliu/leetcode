class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        # The 2D area coule be viewed as a histogram in somehow.
        # 1 1 0 1 -> 1 1 0 1
        # 0 1 1 1 -> 0 2 1 2
        # 0 1 1 1 -> 0 3 2 3 -> max_hist 6
        # 0 1 0 0 -> 0 4 0 0
        def reset_heights(heights, row):
            for j, c in enumerate(row):
                if c == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            return heights

        max_area = 0
        heights = [1 if c == '1' else 0 for c in matrix[0]]
        max_area = self.maximum_rectangle_area_in_histogram(heights)
        for row in matrix[1:]:
            heights = reset_heights(heights, row)
            max_area = max(max_area,
                           self.maximum_rectangle_area_in_histogram(heights))
        return max_area

    def maximum_rectangle_area_in_histogram(self, heights):
        max_area = 0
        heights.append(0)

        i = 0
        stack = []
        while i < len(heights):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if not stack:
                    # All heights are larger than the current top.
                    area = heights[top] * i
                else:
                    # width is the region not includes two heads.
                    area = heights[top] * (i - stack[-1] - 1)
                max_area = max(max_area, area)
        return max_area

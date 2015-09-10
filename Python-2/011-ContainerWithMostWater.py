class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Eliminate search in 2D matrix, similar to finding the medium in a
        # partially order 2D matrix.
        max_area = 0
        i = 0
        j = len(height) - 1
        while i != j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

if __name__ == "__main__":
    height = [1, 2, 3, 4, 5]
    print Solution().maxArea(height)

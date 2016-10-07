class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int

        Given a triangle, find the minimum path sum from top to bottom. 
        Each step you may move to adjacent numbers on the row below.

        Example:
        [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        The minimum path sum from top to bottom is 11 (2 + 3 + 5 + 1 = 11).

        Bonus: if you are able to do this using only O(n) extra space, 
        where n is the total number of rows in the triangle.
        """

        min_path_bottom_up = triangle.pop()
        for row in reversed(triangle):
            for index, element in enumerate(row):
                min_path_bottom_up[index] = element + min(
                    min_path_bottom_up[index], 
                    min_path_bottom_up[index + 1])

        return min_path_bottom_up[0]

      
triangle = [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
print Solution().minimumTotal(triangle)
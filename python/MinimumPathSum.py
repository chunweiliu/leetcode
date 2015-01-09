class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        """DP find minimum from (i-1, j), (i, j-1)
        Time: O(mn)
        Space: O(n)
        Conner: grid is empty
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return grid

        total = 0
        path_sum = [0] * len(grid[0])
        for j, element in enumerate(grid[0]):
            total += element
            path_sum[j] = total

        for i, row in enumerate(grid):
            if i == 0:
                continue
            for j, element in enumerate(row):
                if j == 0:
                    path_sum[j] += element
                else:
                    path_sum[j] = min(path_sum[j-1] + element,
                                      path_sum[j] + element)
        return path_sum[len(grid[0]) - 1]

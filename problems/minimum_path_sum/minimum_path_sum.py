class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Given a m x n grid, find the shortest path sum.
        # 0 1
        # 1 2 -> 3
        m = len(grid)
        n = len(grid[0])
        path_sum = [0] * n
        for i in range(n):
            path_sum[i] = sum(grid[0][:i + 1])

        for i in range(1, m):
            for j in range(n):
                path_sum[j] = min(path_sum[j], path_sum[j - 1]) + grid[i][j]
        return path_sum[-1]

if __name__ == '__main__':
    grid = [[0, 1], [1, 2]]
    print Solution().minPathSum(grid)

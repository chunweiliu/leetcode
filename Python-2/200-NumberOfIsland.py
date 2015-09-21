class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 11000
        # 11000
        # 00100
        # 00011  return 3
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        # Define a function for filling zeros (with rules) to 1s.
        # See how many times we can apply this function.
        def fill_zeros(i, j, visit):
            if 0 <= i < m and 0 <= j < n and \
               not visit[i][j] and grid[i][j] == '1':
                visit[i][j] = True
                fill_zeros(i - 1, j, visit)
                fill_zeros(i + 1, j, visit)
                fill_zeros(i, j - 1, visit)
                fill_zeros(i, j + 1, visit)

        visit = [[False] * n for _ in range(m)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visit[i][j]:
                    fill_zeros(i, j, visit)
                    count += 1
        return count

if __name__ == '__main__':
    grid = ['11000',
            '11000',
            '00100',
            '00011']
    print Solution().numIslands(grid)

class Solution(object):
    def uniquePathsWithObstacles(self, obstacle_grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Surpursingly, this code ran 40ms and beats 96% Python submissions.
        row = len(obstacle_grid)
        column = len(obstacle_grid[0])
        paths = [0] * column

        # Initalize the paths for the first row
        for j in range(column):
            if obstacle_grid[0][j] == 1:
                break
            else:
                paths[j] = 1

        # Take care if the first column is blocked
        for i in range(1, row):
            if obstacle_grid[i][0] == 1:
                paths[0] = 0
            for j in range(1, column):
                if obstacle_grid[i][j] != 1:
                    paths[j] += paths[j - 1]
                else:
                    paths[j] = 0
        return paths[-1]

if __name__ == '__main__':
    obstacle_grid = [[0], [1]]
    print Solution().uniquePathsWithObstacles(obstacle_grid)

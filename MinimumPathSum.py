class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        # initial 2D answer
        Q = grid
        m = len(Q)
        n = len(Q[0])
        P = [[0] * n for x in range(m)]

        P[0][0] = Q[0][0]
        for y in range(1, m):
            P[y][0] = P[y - 1][0] + Q[y][0]
        for x in range(1, n):
            P[0][x] = P[0][x - 1] + Q[0][x]
        for y in range(1, m):
            for x in range(1, n):
                P[y][x] = min(P[y - 1][x], P[y][x - 1]) + Q[y][x]
        return P[m - 1][n - 1]

if __name__ == "__main__":
    #grid = [[1, 2, 3], [4, 5, 6]]
    grid = [[1, 2], [5, 6], [1, 1]]
    print Solution().minPathSum(grid)

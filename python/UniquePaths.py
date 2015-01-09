class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        # 2D list comprehension
        ans = [[0 for x in range(n)] for y in range(m)]

        # can use 1D list for strage

        for x in range(n):
            ans[0][x] = 1
        for y in range(m):
            ans[y][0] = 1

        for y in range(1, m):
            for x in range(1, n):
                ans[y][x] = ans[y - 1][x] + ans[y][x - 1]
        return ans[m - 1][n - 1]

if __name__ == "__main__":
    print Solution().uniquePaths(2, 3)

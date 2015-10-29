class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n+1) for _ in range(m+1)]

        max_width = 0
        for i, row in enumerate(matrix, 1):
            for j, element in enumerate(row, 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min([dp[i-1][j-1],
                                    dp[i-1][j],
                                    dp[i][j-1]]) + 1
                    max_width = max(max_width, dp[i][j])
        return max_width * max_width

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP for the m x n grid
        paths = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                paths[i] += paths[i - 1]
        return paths[-1]

if __name__ == '__main__':
    print Solution().uniquePaths(2, 1)

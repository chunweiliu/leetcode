class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Return a spiral matrix from 1 to n ** 2
        # Trun right when meets a non-zero
        ans = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for count in range(n * n):
            ans[i][j] = count + 1
            if ans[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di  # 90 clock-wise is -90 on the plane
            i += di
            j += dj
        return ans

if __name__ == '__main__':
    n = 3
    print Solution().generateMatrix(n)

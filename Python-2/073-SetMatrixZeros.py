class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 1 1 1
        # 1 0 1
        # 1 1 1
        m, n = len(matrix), len(matrix[0])
        rows_to_set_zeros = [False] * m
        columns_to_set_zeros = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_set_zeros[i] = True
                    columns_to_set_zeros[j] = True
        for i, to_set_zero in enumerate(rows_to_set_zeros):
            if to_set_zero:
                for j in range(n):
                    matrix[i][j] = 0
        for j, to_set_zero in enumerate(columns_to_set_zeros):
            if to_set_zero:
                for i in range(m):
                    matrix[i][j] = 0

if __name__ == '__main__':
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix = [[0, 1]]
    Solution().setZeroes(matrix)
    print matrix

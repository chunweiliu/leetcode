class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 1 2 3      7 4 1
        # 4 5 6  ->  8 5 2
        # 7 8 9      9 6 3
        # Swap horizontally (|)
        for i, row in enumerate(matrix):
            for j in range(len(row) // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
        # Swap counter diagonally (/)
        for i, row in enumerate(matrix):
            for j in range(len(row)):
                if i + j < len(row):
                    matrix[i][j], matrix[-j-1][-i-1] = \
                        matrix[-j-1][-i-1], matrix[i][j]


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    Solution().rotate(matrix)
    print matrix

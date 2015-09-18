class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Start from the top right, eliminate a row or a column each time.
        # Time O(m + n)
        # i, j = 0, len(matrix[0]) - 1
        # while i < len(matrix) and j >= 0:
        #     if matrix[i][j] == target:
        #         return True
        #     if matrix[i][j] > target:
        #         j -= 1
        #     else:
        #         i += 1
        # return False

        # Binary search the entire array.
        # Time O(log(mn)) = O(log m + log n)
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m * n - 1
        while i <= j:
            k = i + (j - i) / 2
            x = matrix[k // n][k % n]
            if x == target:
                return True
            if x < target:
                i = k + 1
            else:
                j = k - 1
        return False

if __name__ == '__main__':
    # matrix = [[1,   3,  5,  7],
    #           [10, 11, 16, 20],
    #           [23, 30, 34, 50]]
    matrix = [[1, 1]]
    target = 2
    print Solution().searchMatrix(matrix, target)

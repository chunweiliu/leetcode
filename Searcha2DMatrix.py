class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        # Two binary searches, one for row and one for column
        # Time: O(n + m)
        # Space: O(1)

        # search row
        rows = [x[0] for x in matrix]
        row = self.binarySearch(rows, target)
        if target < matrix[row][0]:  # boundary condition
            row -= 1

        # search col
        col = self.binarySearch(matrix[row], target)

        if matrix[row][col] == target:
            return True
        else:
            return False

    def binarySearch(self, data, target):
        i, p, q = 0, 0, len(data) - 1
        while p <= q:
            i = (p + q) / 2
            if data[i] == target:
                break
            elif data[i] > target:
                q = i - 1  # - 1 is need
            else:
                p = i + 1  # + 1 is need
        return i


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 11
    print Solution().searchMatrix(matrix, target)

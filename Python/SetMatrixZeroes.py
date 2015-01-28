class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        # Using two vectors to store the indices of zeros
        # Time: O(mn), Space: O(m + n)
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])
        for y in range(len(rows)):
            for x in range(len(cols)):
                if matrix[y][x] == 0:
                    rows[y] = 1
                    cols[x] = 1
        # set zeros
        for y in range(len(rows)):
            for x in range(len(cols)):
                if rows[y] == 1 or cols[x] == 1:
                    matrix[y][x] = 0

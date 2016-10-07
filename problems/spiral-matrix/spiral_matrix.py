class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Display and rotate
        ans = []
        while matrix:
            ans += matrix.pop(0)
            matrix = zip(*matrix)[::-1]
        return ans

        # One-liner
        # Asterisk (*): unpack a tuple for passing arguments
        # return matrix and \
        #        list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])

        # 1 2 3     -----v
        # 4 5 6  -> >----|
        # 7 8 9     ^----<
        # Increase j, increase i,
        # decrease j, decrease i, ...
        # visit = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        # order = []
        # n, m = len(matrix), len(matrix[0])
        # count, max_count = 0, n * m
        # direction = [0, 1]
        # upper = [n, m]
        # lower = [0, 0]
        # i, j = 0, 0
        # while count < max_count:
        #     print i, j
        #     # Visit
        #     if 0 <= i < n and 0 <= j < m and not visit[i][j]:
        #         order.append(matrix[i][j])
        #         visit[i][j] = True
        #     # Figure out next direction
        #     if j + direction[1] == upper[1]:
        #         upper[1] -= 1
        #         direction = [1, 0]
        #     elif i + direction[0] == upper[0]:
        #         upper[0] -= 1
        #         direction = [0, -1]
        #     elif i + direction[0] == lower[0] and count != 0:
        #         lower[0] += 1
        #         direction = [-1, 0]
        #     elif j + direction[1] == lower[1]:
        #         lower[1] += 1
        #         direction = [1, 0]
        #     i += direction[0]
        #     j += direction[1]
        #     count += 1
        # return order

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print Solution().spiralOrder(matrix)

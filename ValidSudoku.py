class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # Check row, column, and sqaure
        # Time: O(n), n is the number of elements
        # Space: O(1)
        B = list()
        for x in range(len(board)):
            b = list()
            for y in range(len(board[0])):
                if board[x][y] != '.':
                    b.append(int(board[x][y]))
                else:
                    b.append(board[x][y])
            B.append(b)
        board = B

        for x in range(len(board)):
            row = board[x]
            flag = self.checkLine(row)
            if flag is False:
                return False

        for x in range(len(board[0])):
            col = [board[y][x] for y in range(len(board))]
            flag = self.checkLine(col)
            if flag is False:
                return False

        for x in range(len(board) / 3):
            for y in range(len(board[0]) / 3):
                sqr = [board[m + 3 * x][n + 3 * y]
                       for m in range(3) for n in range(3)]
                flag = self.checkLine(sqr)
                if flag is False:
                    return False

        return True

    def checkLine(self, line):
        checker = [0] * 10
        for x in range(len(line)):
            if line[x] != '.':
                checker[line[x]] += 1
                if checker[line[x]] > 1:
                    return False
        return True


if __name__ == "__main__":
    board = ["..4...63.",
             ".........",
             "5......9.",
             "...56....",
             "4.3.....1",
             "...7.....",
             "...5.....",
             ".........",
             "........."]
    board = [".4.......",
             "..4......",
             "...1..7..",
             ".........",
             "...3...6.",
             ".....6.9.",
             "....1....",
             "......2..",
             "...8....."]
    print Solution().isValidSudoku(board)

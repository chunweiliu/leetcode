class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        """Check rows, columns, and squares
        Time: O(n^2)
        Space: O(n)
        """
        def is_valid(data):
            for d in data:
                if d != '.' and data.count(d) > 1:
                    return False
            return True

        for row in board:
            if not is_valid(row):
                return False
        print 1

        for x in range(len(board[0])):
            column = [board[y][x] for y in range(len(board))]
            if not is_valid(column):
                return False
        print 2

        for x in range(len(board[0])/3):
            for y in range(len(board)/3):
                square = [board[3*x+m][3*y+n]
                          for m in range(3)
                          for n in range(3)]
                if not is_valid(square):
                    return False
        return True


if __name__ == "__main__":
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    # board = ["..4...63.",
    #          ".........",
    #          "5......9.",
    #          "...56....",
    #          "4.3.....1",
    #          "...7.....",
    #          "...5.....",
    #          ".........",
    #          "........."]
    # board = [".4.......",
    #          "..4......",
    #          "...1..7..",
    #          ".........",
    #          "...3...6.",
    #          ".....6.9.",
    #          "....1....",
    #          "......2..",
    #          "...8....."]
    print Solution().isValidSudoku(board)

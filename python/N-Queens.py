class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        if n == 1:
            return [['Q']]
        if n > 1 and n < 4:
            return []

        board = [0] * n  # column for each rows
        ans = list()
        self.put_queen(0, board, n, ans)

        # formating
        formated_ans = list()
        for board in ans:  # [7, 3, 0, 2, 5, 1, 6, 4]
            formated_board = list()
            for y in range(n):
                row = ['Q' if x == board[y] else '.' for x in range(n)]
                formated_board.append(''.join(row))
            formated_ans.append(formated_board)
        return formated_ans

    def put_queen(self, row, board, n, ans):
        if row == n:
            ans.append(list(board))  # make a copy for return
            return
        for x in range(n):
            board[row] = x
            if self.check(row, board):
                self.put_queen(row + 1, board, n, ans)

    def check(self, row, board):
        for x in range(row):
            diff = abs(board[x] - board[row])
            if diff == 0 or diff == row - x:
                return False
        return True


if __name__ == "__main__":
    print Solution().solveNQueens(4)

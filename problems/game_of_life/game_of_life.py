class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        m = len(board)
        n = len(board[0])
        # Store the next board in an extra bit.
        for i in range(m):
            for j in range(n):
                x = sum([board[ii][jj] % 2
                         for ii in range(max(0, i-1), min(i+2, m))
                         for jj in range(max(0, j-1), min(j+2, n))
                         if not (ii == i and jj == j)])
                print i, j, x
                if board[i][j] and x < 2:
                    board[i][j] = 0b01
                elif board[i][j] and 2 <= x <= 3:
                    board[i][j] = 0b11
                elif board[i][j] and 3 < x:
                    board[i][j] = 0b01
                elif not board[i][j] and x == 3:
                    board[i][j] = 0b10

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

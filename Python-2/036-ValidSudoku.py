class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Make a new type of data structure and see if the duplicate found.
        # (row, char), (char, column), (row, column, char)
        # patterns = list()
        # for i, row in enumerate(board):
        #     for j, char in enumerate(row):
        #         if char != '.':
        #             patterns += (i, char), (char, j), (i // 3, j // 3, char)
        # return len(patterns) == len(set(patterns))

        # Check three posible direction. The tricky part is how to represent
        # a row, column, and square of the board.
        def check_duplicate(nums):
            digits = [0] * 10
            for digit in nums:
                if digit == '.':
                    continue
                digits[int(digit)] += 1
                if digits[int(digit)] >= 2:
                    return True
            return False

        for row in board:
            if check_duplicate(row):
                return False

        for i in range(len(board[0])):
            if check_duplicate(''.join([row[i] for row in board])):
                return False

        for i in range(3):
            for j in range(3):
                square = ''.join([board[3 * i + m][3 * j + n]
                                 for m in range(3)
                                 for n in range(3)])
                if check_duplicate(square):
                    return False
        return True

if __name__ == '__main__':
    board = [".87654321",
             "2........",
             "3........",
             "4........",
             "5........",
             "6........",
             "7........",
             "8........",
             "9........"]
    print Solution().isValidSudoku(board)

from collections import defaultdict


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        possible_solutions = self.generate_possible_solutions(board)
        self.solve(board, possible_solutions)

    def solve(self, board, possible_solutions):
        if len(possible_solutions) == 0:
            return True

        # Start from the position with minimum available solutions
        location = min(possible_solutions.keys(),
                       key=lambda x: len(possible_solutions[location]))
        for solution in possible_solutions[location]:
            i, j = location
            board[i][j] = solution

            update = {location: possible_solutions[location]}
            del possible_solutions


    def generate_possible_solutions(self, board):
        possible_solutions = defaultdict(list)
        seen = defaultdict(list)
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char != '.':
                    seen[('row', i)] += char
                    seen[('column', j)] += char
                    seen[(i // 3, j // 3)] += char
                else:
                    possible_solutions[(i, j)] = []

        # Until the entire seen matrix done, we can't determine the poss. sol.
        nums = '123456789'
        for (i, j) in possible_solutions.keys():
            possible_solutions[(i, j)] = [n for n in nums
                                          if (n not in seen['row', i] and
                                              n not in seen['column', j] and
                                              n not in seen[i // 3, j // 3])]
        return possible_solutions

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Make a new type of data structure and see if the duplicate found.
        # (row, char), (char, column), (row, column, char)
        patterns = list()
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char != '.':
                    patterns += (i, char), (char, j), (i // 3, j // 3, char)
        return len(patterns) == len(set(patterns))

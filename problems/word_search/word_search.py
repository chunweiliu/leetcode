class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # DFS implementation. Speed up for following issues:
        # Which data structure used to represent visited cell?
        # Early rejection.
        m, n = len(board), len(board[0])

        def search(word, curr, visited):
            if not word:
                return True
            r, c = curr
            if (not (0 <= r < m) or not (0 <= c < n) or visited[r][c] or
                    board[r][c] != word[0]):
                return False

            # Search every direction, if one from those match then this works.
            visited[r][c] = True

            # Using for loop casues TLE. Using four OR condition pass the test.

            # This will run four times no matter what.
            # for (i, j) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            #     search_result |= search(word[1:], (i, j), visited)

            # If one search return true, the other will stop and return True.
            search_result = (search(word[1:], (r - 1, c), visited) or
                             search(word[1:], (r + 1, c), visited) or
                             search(word[1:], (r, c - 1), visited) or
                             search(word[1:], (r, c + 1), visited))

            visited[r][c] = False
            return search_result

        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if search(word, (i, j), visited):
                    return True
        return False

if __name__ == '__main__':
    board = ['aa']
    word = 'aa'
    print Solution().exist(board, word)

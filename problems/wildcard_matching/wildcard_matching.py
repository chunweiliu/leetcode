class Solution():
    def isMatch(self, s, p):
        # O(n + m)
        i, j = 0, 0
        m, n = len(s), len(p)
        string_match, pattern_star = -1, -1
        while i < m:
            # if match advance both
            if j < n and s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            # if match with '*'
            elif j < n and p[j] == '*':
                string_match = i
                pattern_star = j
                j += 1
            # if not match, check if '*' show previously
            elif pattern_star != -1:
                j = pattern_star + 1
                string_match += 1
                i = string_match
            # if not match, and no '*' can help
            else:
                return False

        return all(pattern == '*' for pattern in p[j:])

        # TLE: O(n * m)
        #   0 a b b
        # 0 1 0 0 0
        # a 0 1 0 0
        # * 0 1 1 1
        # ? 0 0 1 1
        # # Use a table for record the matching result
        # m = len(p) + 1
        # n = len(s) + 1
        # table = [[0] * n for _ in range(m)]

        # # Trivial case
        # table[0][0] = 1

        # # Update the first column
        # for i in range(1, m):
        #     if p[i - 1] == '*':
        #         table[i][0] = table[i - 1][0]

        # # Update each row
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if p[i - 1] == '*':
        #             if table[i][j - 1]:
        #                 table[i][j:] = [True] * (n - j)
        #                 break
        #             table[i][j] = table[i - 1][j] or table[i][j - 1]
        #         else:
        #             table[i][j] = (table[i - 1][j - 1] and
        #                            (p[i - 1] == s[j - 1] or
        #                             p[i - 1] == '?'))
        # return table[-1][-1]

from collections import defaultdict
import string


class Solution(object):
    def ladderLength(self, begin_word, end_word, word_list):
        # Double BFS
        length = 2
        front, back = set([begin_word]), set([end_word])
        word_list |= front
        word_list |= back
        while front:
            front = (set((word[:i] + char + word[i+1:]  # All valid transitions
                          for word in front  # <-
                          for i in range(len(word))
                          for char in string.lowercase)) &
                     word_list)  # which are also in the list.

            if front & back:
                return length
            length += 1

            # For better performation by reduce the for loop above.
            if len(front) > len(back):
                front, back = back, front

            # Remove the currently reached point.
            word_list -= front
        return 0

    def ladder_length(self, begin_word, end_word, word_list):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        # TLE
        # Build a graph
        word_list |= set([begin_word, end_word])
        graph = self.build_graph(word_list)

        # BFS for the shortest path
        queue = [(begin_word, 1)]
        while queue:
            v, length = queue.pop(0)

            if v == end_word:
                return length

            for n in graph[v]:
                queue.append((n, length + 1))
        return -1

    def build_graph(self, word_list):
        graph = defaultdict(list)
        for i, word in enumerate(word_list):
            for other_word in word_list - set(word):
                if self.edit_distance(word, other_word) <= 1:
                    graph[word].append(other_word)
        return graph

    def edit_distance(self, s, t):
        r = len(s) + 1
        c = len(t) + 1
        t = [[0] * c for _ in range(r)]

        for i in range(1, r):
            t[i][0] = i
        for j in range(1, c):
            t[0][j] = j
        # DP
        for i in range(1, r):
            for j in range(1, c):
                if s[i-1] == t[j-1]:
                    t[i][j] = t[i - 1][j - 1]
                else:
                    t[i][j] = min([t[i - 1][j - 1],
                                   t[i - 1][j],
                                   t[i][j - 1]]) + 1
        return t[-1][-1]

if __name__ == '__main__':
    begin_word = 'a'
    end_word = 'd'
    word_list = set(['b', 'c'])
    print Solution().ladderLength(begin_word, end_word, word_list)

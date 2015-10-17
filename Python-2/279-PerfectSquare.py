class Solution(object):
    def numSquares(self, n):
        edges = [i * i for i in range(1, int(n ** 0.5) + 1)]
        visited = set()
        level = 0
        next_nodes = [0]
        while True:
            current_nodes = next_nodes
            level += 1
            next_nodes = []
            for current_node in current_nodes:
                for edge in edges:
                    next_node = current_node + edge
                    if next_node == n:
                        return level
                    if next_node in visited:
                        continue
                    if next_node > n:
                        break
                    visited.add(next_node)
                    next_nodes.append(next_node)

    def num_squares_pochmann(self, n):
        sums = {0}
        while n not in sums:
            # During the addition, the sums set records all possible
            # perfect squares sum, and the minimum one serves as the conter.
            sums = {sum + i*i
                    for sum in sums
                    for i in xrange(1, int((n - sum)**0.5 + 1))}
        return min(sums)

    def num_squares_bfs2(self, n):
        # TLE at n = 7168
        visited = [False] * (n + 1)
        level = 0
        queue = [(0, 0)]
        while True:
            current_node, level = queue.pop(0)
            visited[current_node] = True
            for i in range(1, int((n - current_node) ** 0.5) + 1):
                next_node = current_node + i * i
                if next_node == n:
                    return level + 1
                if visited[next_node]:
                    continue
                if next_node > n:
                    break
                queue.append((next_node, level + 1))

    def num_squares_bfs1(self, n):
        # TLE at n = 399
        # This is a search on a tree. It is not a BFS on a graph.
        queue = [(0, 0)]
        while queue:
            current_sum, level = queue.pop(0)
            if current_sum == n:
                return level

            for i in range(1, int((n - current_sum) ** 0.5) + 1):
                square = i * i
                if n - square >= 0:
                    queue.append((current_sum + square, level + 1))

    def num_squares_dfs2(self, n):
        # TLE at n = 106
        perfect_squares = [x ** 2 for x in range(1, n // 2 + 1)]
        results = []
        self.subsets(perfect_squares, n, [], results)
        return min(map(len, results))

    def num_squares_dfs1(self, n):
        # TLE at n = 97
        perfect_squares = [x ** 2 for x in range(1, n + 1)]
        results = []
        self.subsets(perfect_squares, n, [], results)
        return min(map(len, results))

    def subsets(self, nums, target, attemp, results):
        if target == 0:
            results.append(attemp)
            return

        for i, n in enumerate(nums):
            if n <= target:
                self.subsets(nums[i:], target - n, attemp + [n], results)

if __name__ == '__main__':
    n = 13
    print Solution().numSquares(n)

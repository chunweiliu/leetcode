from collections import defaultdict


class Solution(object):
    def canFinish(self, num_courses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True

        self.TO_BE_VISITED = 0
        self.VISITING = 1
        self.DONE = 2

        graph = self.make_graph(num_courses, prerequisites)
        status = [self.TO_BE_VISITED] * num_courses
        return self.dfs(num_courses, graph, status)

    def dfs(self, num_courses, graph, status):
        no_cycle = True
        for n in range(num_courses):
            if status[n] != self.DONE:
                # status[n] = self.VISITING
                no_cycle &= self.dfs_visit(n, graph, status)
        return no_cycle

    def dfs_visit(self, v, graph, status):
        status[v] = self.VISITING
        no_cycle = True  # [BUG]
        for n in graph[v]:  # [BUG]
            if status[n] == self.VISITING:
                return False
            if status[n] == self.TO_BE_VISITED:
                no_cycle &= self.dfs_visit(n, graph, status)
        status[v] = self.DONE
        return no_cycle  # [BUG]

    def make_graph(self, num_node, pairs):
        graph = defaultdict(list)
        for (end, start) in pairs:  # end needs start
            graph[start].append(end)
        return graph

if __name__ == '__main__':
    num_courses = 2
    prerequisites = [[0, 1], [1, 0]]
    print Solution().canFinish(num_courses, prerequisites)

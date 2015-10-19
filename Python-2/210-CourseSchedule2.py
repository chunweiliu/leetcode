from collections import defaultdict


class Solution(object):
    def findOrder(self, num_courses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = self.build_graph(num_courses, prerequisites)
        return self.topological_sort(graph)

    def topological_sort(self, graph):
        # Compute in degree of all nodes
        num_course = len(graph.keys())

        in_degree = [0] * num_course
        for courses in graph.values():
            for course in courses:
                in_degree[course] += 1

        # Make a list of zero in-degree.
        zero_in_degree_vertexs = [i for i in range(num_course)
                                  if in_degree[i] == 0]

        # Take out a zero in-degree node and remove all edge from that node.
        order = []
        while zero_in_degree_vertexs:
            v = zero_in_degree_vertexs.pop()
            order.append(v)
            for n in graph[v]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    zero_in_degree_vertexs.append(n)

        # If the number of order is less than the number of course, there is
        # a cycle in the graph.
        return order if len(order) == num_course else []

    def build_graph(self, num_courses, prerequisites):
        graph = defaultdict(list)
        for (end, start) in prerequisites:
            graph[start].append(end)

        for course in range(num_courses):
            if course not in graph:
                graph[course] = []
        return graph

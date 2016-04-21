#include "leetcode.h"

#include <queue>
#include <unordered_set>


class Solution {
 public:
  bool canFinish(int numCourses, 
                 const std::vector<std::pair<int, int>>& prerequisites) {
    std::vector<std::unordered_set<int>> graph;
    MakeGraph(numCourses, prerequisites, &graph);

    // 0) DFS
    return DFS(graph);

    // 1) Topological sort
    // std::vector<int> sorted_list;
    // return TopologicalSort(graph, &sorted_list);
  }

 private:
  enum VisitType {
    NotVisit = 0,
    Visited = 1,  // Ongoing DFS. If we hit this node, there is a backward edge.
    Finished = 2,  // Has finished the DFS, so the top level DFS won't visit.
  };

  void MakeGraph(int numCourses,
                 const std::vector<std::pair<int, int>>& prerequisites, 
                 std::vector<std::unordered_set<int>>* graph) {
    graph->resize(numCourses);
    for (const auto& prerequisit : prerequisites) {
      // The first need the second, so the representation is second -> first.
      graph->at(prerequisit.second).insert(prerequisit.first);
    }
  }

  bool DFS(const std::vector<std::unordered_set<int>>& graph) {
    int n_vertices = graph.size();
    std::vector<VisitType> status(n_vertices, VisitType::NotVisit);

    bool ret = true;
    for (int i = 0; i < n_vertices; ++i) {
      if (status[i] == VisitType::NotVisit) {
        status[i] = VisitType::Visited;
        ret = ret && DFSVisit(graph, i, &status);
      }
    }
    return ret;
  }

  bool DFSVisit(const std::vector<std::unordered_set<int>>& graph, int current,
                std::vector<VisitType>* status) {
    bool ret = true;
    for (const auto& neighbor : graph[current]) {
      if (status->at(neighbor) == VisitType::Visited) return false;

      if (status->at(neighbor) == VisitType::NotVisit) {
        status->at(neighbor) = VisitType::Visited;
        ret = ret && DFSVisit(graph, neighbor, status);
      }
    }
    status->at(current) = VisitType::Finished;
    return ret;
  }

  bool TopologicalSort(const std::vector<std::unordered_set<int>>& graph,
                       std::vector<int>* sorted_list) {
    int num_node = graph.size();
    // Count indegree for each node.
    std::vector<int> indegrees(num_node, 0);
    for (int i = 0; i < num_node; ++i) {
      for (const auto& node : graph[i]) {
        ++indegrees[node];
      }
    }

    // Push zero indegrees to a queue.
    std::queue<int> zero_indegrees;
    for (int i = 0; i < num_node; ++i) {
      if (indegrees[i] == 0) {
        zero_indegrees.push(i);
      }
    }

    while (!zero_indegrees.empty()) {
      int current = zero_indegrees.front();
      sorted_list->push_back(current);
      zero_indegrees.pop();
      for (const auto& node : graph[current]) {
        --indegrees[node];
        if (indegrees[node] == 0) { 
          zero_indegrees.push(node);
        }
      }
    }

    for (int i = 0; i < num_node; ++i) {
      if (indegrees[i] != 0) {
        return false;
      }
    }
    return true;
  }
};

int main(int argc, char** argv) {
  int numCourses = 2;
  std::vector<std::pair<int, int>> prerequisites;
  prerequisites.push_back(std::make_pair(0, 1));
  prerequisites.push_back(std::make_pair(1, 0));

  Solution solution;
  std::cout << solution.canFinish(numCourses, prerequisites) << std::endl;
  return 0;
}
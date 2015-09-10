#include "leetcode.h"

#include <unordered_set>

using namespace std;

class Solution {
 public:
  vector<int> findOrder(int num_courses, 
                        const vector<pair<int, int>>& prerequisites) {
    vector<unordered_set<int>> graph;
    MakeGraph(num_courses, prerequisites, &graph);

    vector<int> sorted_list, empty_list;
    bool acyclic = DFS(num_courses, graph, &sorted_list);
    if (!acyclic) return empty_list;
    return sorted_list;
  }

 private:
  enum VisitType {
    NotVisit = 0,
    Visited = 1,
    Done = 2,
  };

  void MakeGraph(int num_courses, const vector<pair<int, int>>& prerequisites, 
                 vector<unordered_set<int>>* graph) {
    graph->resize(num_courses);
    for (int i = 0; i < prerequisites.size(); ++i) {
      graph->at(prerequisites[i].second).insert(prerequisites[i].first);
    }
  }

  // Runtime error.
  bool DFS(int num_courses, const vector<unordered_set<int>>& graph, 
           vector<int>* sorted_list) {
    vector<VisitType> status(num_courses, VisitType::NotVisit);

    bool acyclic = true;
    for (int i = 0; i < num_courses; ++i) {
      if (status.at(i) == VisitType::Visited) return false;
      if (status.at(i) == VisitType::NotVisit) {
        status.at(i) = VisitType::Visited;
        acyclic = acyclic && DFSVisit(graph, i, &status, sorted_list);
      }
    }
    reverse(sorted_list->begin(), sorted_list->end());
    return acyclic;
  }

  bool DFSVisit(const vector<unordered_set<int>>& graph, int node, 
                vector<VisitType>* status, vector<int>* sorted_list) {
    bool acyclic = true;
    for (const auto& neighbor : graph[node]) {
      if (status->at(neighbor) == VisitType::Visited) return false;
      if (status->at(neighbor) == VisitType::NotVisit) {
        status->at(neighbor) = VisitType::Visited;
        acyclic = acyclic && DFSVisit(graph, neighbor, status, sorted_list);
      }
    }
    sorted_list->push_back(node);
    status->at(node) = VisitType::Done;
    return acyclic;
  }
};

int main(int argc, char** argv) {
  int numCourses = 2;
  std::vector<std::pair<int, int>> prerequisites;
  prerequisites.push_back(std::make_pair(0, 1));
  // prerequisites.push_back(std::make_pair(1, 0));

  Solution solution;
  vector<int> sorted_list = solution.findOrder(numCourses, prerequisites);
  for (const auto& element : sorted_list) {
    cout << element << " ";
  }
  cout << endl;
  return 0;
}
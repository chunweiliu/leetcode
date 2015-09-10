#include "leetcode.h"

#include <queue>
#include <unordered_map>

class Solution {
 public:
  UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
    // BFS
    if (!node) return node;
    hash[node] = new UndirectedGraphNode(node->label);
    std::queue<UndirectedGraphNode*> to_visit;
    to_visit.push(node);
    while (!to_visit.empty()) {
      UndirectedGraphNode* current = to_visit.front();
      to_visit.pop();
      for (const auto& neighbor : current->neighbors) {
        if (hash.find(neighbor) == hash.end()) {
          // Create a new memory space for nodes if need.
          hash[neighbor] = new UndirectedGraphNode(neighbor->label);
          to_visit.push(neighbor);
        }
        // In any case, assgined the edge to the node
        hash[current]->neighbors.push_back(hash[neighbor]);
      }
    }
    return hash[node];
  }
  
  // UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
  //   // DFS
  //   if (!node) return node;
  //   if (hash.find(node) == hash.end()) {
  //     hash[node] = new UndirectedGraphNode(node->label);
  //     for (const auto& neighbor : node->neighbors) {
  //       hash[node]->neighbors.push_back(cloneGraph(neighbor));
  //     }
  //   }
  //   return hash[node];
  // }
 private:
  std::unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> hash;
};

int main(int argc, char** argv) {
  Solution solution;
  UndirectedGraphNode* node0 = new UndirectedGraphNode(-1);
  UndirectedGraphNode* node1 = new UndirectedGraphNode(1);
  node0->neighbors.push_back(node1);
  solution.cloneGraph(node0);
  delete node0;
  delete node1;
  return 0;
}
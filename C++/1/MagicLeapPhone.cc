#include "leetcode.h"

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    // Table look up
    unordered_map<int, int> table;
    for (int i = 0; i < nums.size(); ++i) {
      table[nums[i]] = i;
    }

    for (int i = 0; i < nums.size(); ++i) {
      unordered_map<int, int>::iterator iter = table.find(target - nums[i]);
      if (iter != table.end() && iter->second != i) {
        return {i + 1, iter->second + 1};
      }
    }
    return {};
  }

  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    if (l1 == NULL) {
      return l2;
    }
    if (l2 == NULL) {
      return l1;
    }
    ListNode* ret = l1;
    int carry = 0;
    while (true) {
      l1->val += l2->val + carry;
      if (l1->val > 9) {
        carry = 1;
        l1->val -= 10;
      } else {
        carry = 0;
      }
      if (l1->next == NULL) {
        l1->next = l2->next;  // L1 is finished. Move l2 to l1 to continue.
        break;
      } else if (l2->next == NULL) {
        break;
      }
      l1 = l1->next;
      l2 = l2->next;
    }
    while (l1->next != NULL && carry) {  // Need to check the last node.
      l1 = l1->next;  // Aware!
      l1->val += carry;
      if (l1->val > 9) {
        carry = 1;
        l1->val -= 10;
      } else {
        return ret;
      }
    }
    if (carry) {  // Add a new node by the head of l2.
      l2->val = carry;
      l2->next = nullptr;
      l1->next = l2;
    }
    return ret;
  }

  ListNode* addTwoNumbersLeak(ListNode* l1, ListNode* l2) {
    // Define a dummy node for linked list operation.
    ListNode header(-1), *current = &header;
    int carry = 0;
    while (l1 || l2 || carry) {
      int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
      current->next = new ListNode(sum % 10);  // Memory leaks!
      current = current->next;

      carry = sum / 10;
      l1 = l1 ? l1->next : nullptr;
      l2 = l2 ? l2->next : nullptr;
    }
    return header.next;
  }

  int lengthOfLongestSubstring(string s) {
    int max_length = 0;
    int p = 0;  // The start of the candidate string.
    int q = 0;  // The end of the candidate string.
    unordered_map<char, bool> exist;
    while (q < s.length()) {
      if (exist[s[q]]) {
        max_length = max(max_length, q - p);
        while (s[p] != s[q]) {  // Find the repeat character.
          exist[s[p]] = false;
          p++;
        }
        p++;
        q++;
      } else {
        exist[s[q]] = true;
        q++;
      }
    }
    max_length = max(max_length, q - p);
    return max_length;
  }

  double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    // Median definition.
    int len1 = nums1.size();
    int len2 = nums2.size();
    int total = len1 + len2;
    if (total % 2 == 1) {
      return FindKthElement(nums1.begin(), len1, nums2.begin(), len2,
                            total / 2 + 1);
    }
    return 0.5 * (FindKthElement(nums1.begin(), len1, nums2.begin(), len2, 
                                 total / 2) + 
                  FindKthElement(nums1.begin(), len1, nums2.begin(), len2, 
                                 total / 2 + 1));
  }

  double FindKthElement(vector<int>::iterator iter1, int len1,
                        vector<int>::iterator iter2, int len2,
                        int kth) {
    if (len1 < len2) {  // Assume |nums1| >= |nums2|
      return FindKthElement(iter2, len2, iter1, len1, kth);  
    }
    if (len2 == 0) {
      return *(iter1 + kth - 1);
    }
    if (kth == 1) {
      return min(*iter1, *iter2);
    }
    // Binary search for the k-th element. Get the first n from num1 and the
    // first m from num2 (where n + m == k). If the n-th of num1 is smaller than
    // the m-th of num2, than the k-th wouldn't be in the first n-th of num1.
    // Same observation apply to num2. 
    // Why? Because the kth element couldn't in either n-th nor m-th elements 
    // anyway. You just want to get rid of one part and move on.
    int m = min(kth / 2, len2);
    int n = kth - m;
    if (*(iter1 + n - 1) < *(iter2 + m - 1)) {
      return FindKthElement(iter1 + n, len1 - n, iter2, len2, kth - n);
    }
    return FindKthElement(iter1, len1, iter2 + m, len2 - m, kth - m);
  }

  string longestPalindrome(string s) {
    // Dynamic Programming: Two dimensional truth table for determining if the 
    // substring(i, j) is a palindrome. T[i, j] <- T[i+1, j-1] && s[i] == s[j].
    bool T[1000][1000];
    memset(T, false, sizeof(T));

    // Initialize and check conner cases:
    int n = s.length();
    for (int i = 0; i < n; ++i) {
      T[i][i] = true;
    }
    int longest = 1;
    for (int i = 0; i < n - 1; ++i) {
      if (s[i] == s[i + 1]) {
        T[i][i + 1] = true;
        longest = 2;
      }
    }

    int start = 0;
    for (int len = 3; len <= n; ++len) {
      for (int i = 0; i < n; ++i) {
        int j = i + len - 1;
        if (s[i] == s[j] && T[i + 1][j - 1]) {
          T[i][j] = true;
          longest = len;
          start = i;
        }
      }
    }

    return s.substr(start, longest);
  }

  std::string convert(std::string s, int numRows) {
    std::vector<std::string> strings(numRows);
    int row = 0;
    int direction = 1;
    for (int i = 0; i < s.length(); ++i) {
      // 0 1 2 1 0 1 2 1 0
      if (row == (numRows - 1) && row == 0) {
        direction = 0;
      } else if (row == numRows - 1) {
        direction = -1;
      } else if (row == 0) {
        direction = 1;
      }
      strings[row] += s[i];
      row += direction;
    }

    std::string converted_string;
    for (int i = 0; i < strings.size(); ++i) {
      converted_string += strings[i];
    }
    return converted_string;
  }

  int myAtoi(string str) {
    int begin = 0;
    while (str.compare(begin, 1, " ") == 0) {
      begin++;
    }

    int sign = 1;
    if (str.compare(begin, 1, "-") == 0) {
      sign = -1;
      begin++;
    } else if (str.compare(begin, 1, "+") == 0) {
      begin++;
    }

    long num = 0;
    int i = begin;
    for (; i < str.length(); ++i) {
      if (!IsDigit(str[i])) {
        break;
      }
      num += str[i] - '0';
      if (i != str.length() && IsDigit(str[i + 1])) {
          num *= 10;
      }
    }
    if (sign == 1 && (num > numeric_limits<int>::max() || i - begin > 10)) {
      return numeric_limits<int>::max();
    }
    if (sign == -1 && (num > numeric_limits<int>::max() || i - begin > 10)) {
      return numeric_limits<int>::min();
    }
    return static_cast<int>(sign * num);
  }

  bool IsDigit(char c) {
    int digit = c - '0';
    if (digit < 0 || digit > 9) {
      return false;
    }
    return true;
  }

  std::vector<std::vector<int>> levelOrder(TreeNode* root) {
    std::vector<std::vector<int>> ret;
    if (root == NULL) {
      return ret;
    }

    std::vector<TreeNode*> this_level;
    this_level.push_back(root);
    while (this_level.size() != 0) {
      std::vector<int> this_level_val;
      Transfer(this_level, &this_level_val);
      ret.push_back(this_level_val);

      std::vector<TreeNode*> next_level;
      for (int i = 0; i < this_level.size(); ++i) {
        TreeNode* node = this_level[i];
        if (node->left) {
          next_level.push_back(node->left);
        }
        if (node->right) {
          next_level.push_back(node->right);
        }
      }
      this_level = next_level;
    }
    return ret;
  }

  void Transfer(const std::vector<TreeNode*>& tree, std::vector<int>* vect) {
    vect->resize(tree.size());
    for (int i = 0; i < tree.size(); ++i) {
      vect->at(i) = tree[i]->val;
    }
  }

  std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root) {
    std::vector<std::vector<int>> levels;
    if (root == NULL) {
      return levels;
    }

    std::vector<TreeNode*> this_level;
    this_level.push_back(root);
    int depth = 0;
    while (this_level.size() != 0) {
      std::vector<int> this_level_val;
      Transfer(this_level, &this_level_val);

      if (depth++ % 2 == 1) {
        std::reverse(this_level_val.begin(), this_level_val.end());
      }
      levels.push_back(this_level_val);

      std::vector<TreeNode*> next_level;
      for (int i = 0; i < this_level.size(); ++i) {
        TreeNode* node = this_level[i];
        if (node->left) {
          next_level.push_back(node->left);
        }
        if (node->right) {
          next_level.push_back(node->right);
        }
      }
      this_level = next_level;
    }
    return levels;
  }

  void Transfer(const std::vector<TreeNode*>& tree, std::vector<int>* vect) {
    vect->resize(tree.size());
    for (int i = 0; i < tree.size(); ++i) {
      vect->at(i) = tree[i]->val;
    }
  }

  std::vector<std::vector<int>> levelOrderBottom(TreeNode* root) {
    std::vector<std::vector<int>> ret;
    if (root == NULL) {
      return ret;
    }

    std::vector<TreeNode*> this_level;
    this_level.push_back(root);
    while (this_level.size() != 0) {
      std::vector<int> this_level_val;
      Transfer(this_level, &this_level_val);
      ret.push_back(this_level_val);

      std::vector<TreeNode*> next_level;
      for (int i = 0; i < this_level.size(); ++i) {
        TreeNode* node = this_level[i];
        if (node->left) {
          next_level.push_back(node->left);
        }
        if (node->right) {
          next_level.push_back(node->right);
        }
      }
      this_level = next_level;
    }
    std::reverse(ret.begin(), ret.end());
    return ret;
  }

  bool isBalanced(TreeNode* root) {
    if (!root) return true;  // nullptr would be treated as false in C++ 11.
    return isBalanced(root->left) && isBalanced(root->right) &&
           (abs(Depth(root->left) - Depth(root->right)) <= 1);
  }

  int Height(const TreeNode* root) {
    if (!root) return 0;
    return max(Depth(root->left), Depth(root->right)) + 1;  // Actual height + 1
  }

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

  std::vector<int> rightSideView(TreeNode* root) {
    std::vector<int> right_side_view;
    if (root == NULL) {
      return right_side_view;
    }

    std::vector<std::vector<int>> levels;
    std::vector<TreeNode*> this_level;
    this_level.push_back(root);
    while (this_level.size() != 0) {
      std::vector<int> this_level_val;
      Transfer(this_level, &this_level_val);
      levels.push_back(this_level_val);

      std::vector<TreeNode*> next_level;
      for (int i = 0; i < this_level.size(); ++i) {
        TreeNode* node = this_level[i];
        if (node->left) {
          next_level.push_back(node->left);
        }
        if (node->right) {
          next_level.push_back(node->right);
        }
      }
      this_level = next_level;
    }

    // Pick up the right most element.
    for (int i = 0; i < levels.size(); ++i) {
      right_side_view.push_back(levels[i].back());
    }

    return right_side_view;
  }

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

  int Partition(vector<int>& nums, int left, int right) {
    int i = left;
    int j = left;
    int n = right;
    const int pivot = nums[n];
    while (j <= n) {
      cout << i << " " << j << " " << n << endl;
      if (nums[j] == pivot) j++;
      else if (nums[j] < pivot) {
        swap(nums[i++], nums[j++]);
      } else {
        swap(nums[j], nums[n--]);
      }
    }
    return i;
  }

  int findKthLargest(vector<int> nums, int k) {
    int left = 0, right = nums.size() - 1;
    while (true) {
      int p = Partition(nums, left, right);
      if (p == k - 1) return nums[p];
      if (p < k - 1) {
        left = p + 1;
      } else {
        right = p - 1;
      }
    }
  }

};

int main(int argc, char** argv) {
  return 0;
}
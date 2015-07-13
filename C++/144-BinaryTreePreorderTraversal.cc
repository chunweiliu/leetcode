#include <iostream>
#include <vector>

#include "tree_node.h"

class Solution {
 public:
  std::vector<int> preorderTraversal(TreeNode* root) {
    std::vector<TreeNode*> stack;
    std::vector<int> result;
    TreeNode* current = root;
    while (stack.size() > 0 || current) {
      if (current) {
        result.push_back(current->val);
        stack.push_back(current);
        current = current->left;
      } else {
        current = stack.back();
        stack.pop_back();
        current = current->right;
      }
    }
    return result;
  }
};

int main(int argc, char** argv) {
  TreeNode tree_nodes[3] = {1, 2, 3};
  TreeNode* root;
  root = &tree_nodes[0];
  root->right = &tree_nodes[1];
  root->right->left = &tree_nodes[2];
  
  Solution solution = Solution();
  std::vector<int> result = solution.preorderTraversal(root);
  for (int i = 0; i < result.size(); ++i) {
    std::cout << result[i] << std::endl;
  }
}
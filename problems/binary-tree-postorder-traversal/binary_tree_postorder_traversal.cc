#include <iostream>
#include <vector>

#include "tree_node.h"

class Solution {
 public:
  std::vector<int> postorderTraversal(TreeNode* root) {    
    // Breath first search for the first stack
    std::vector<TreeNode*> first_stack;
    std::vector<TreeNode*> second_stack;
    TreeNode* current = root;
    if (current) {
      first_stack.push_back(current);
    }
    while (first_stack.size() > 0) {
      current = first_stack.back();
      first_stack.pop_back();
      second_stack.push_back(current);
      if (current->left) {
        first_stack.push_back(current->left);
      }
      if (current->right) {
        first_stack.push_back(current->right);
      }
    }

    std::vector<int> result;
    while(second_stack.size() > 0) {
      result.push_back(second_stack.back()->val);
      second_stack.pop_back();
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
  std::vector<int> result = solution.postorderTraversal(root);
  for (int i = 0; i < result.size(); ++i) {
    std::cout << result[i] << std::endl;
  }
}
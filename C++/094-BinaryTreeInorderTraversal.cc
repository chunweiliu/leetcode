#include <iostream>
#include <vector>

#include "tree_node.h"

class Solution {
public:
  std::vector<int> inorderTraversal(TreeNode* root) {
    std::vector<TreeNode*> stack;
    std::vector<int> result;
    TreeNode* current = root;
    while (stack.size() > 0 || current) {
      if (current) {
        stack.push_back(current);
        current = current->left;
      } else {
        current = stack.back();
        stack.pop_back();
        result.push_back(current->val);
        current = current->right;
      }
    }
    return result;
  }
  // std::vector<int> inorderTraversal(TreeNode* root) {
  //   std::vector<TreeNode*> stack;
  //   if (root) {
  //     stack.push_back(root);
  //   }

  //   std::vector<int> result;
  //   while (stack.size() > 0) {
  //     const auto& current = stack.back();
  //     stack.pop_back();  // Do not pop the stack unless no left node left.
      
  //     if (current->left) {
  //       stack.push_back(current->left);        
  //     }
  //     result.push_back(current->val);
  //     if (current->right) {
  //       stack.push_back(current->right);
  //     }
  //   }
  //   return result;
  // }
};

int main(int argc, char** argv) {
  TreeNode tree_nodes[3] = {1, 2, 3};
  TreeNode* root;
  root = &tree_nodes[0];
  root->right = &tree_nodes[1];
  root->right->left = &tree_nodes[2];
  
  Solution solution = Solution();
  std::vector<int> result = solution.inorderTraversal(root);
  for (int i = 0; i < result.size(); ++i) {
    std::cout << result[i] << std::endl;
  }
}
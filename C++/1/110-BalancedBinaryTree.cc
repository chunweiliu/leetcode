#include "leetcode.h"

using namespace std;


class Solution {
 public:
  bool isBalanced(TreeNode* root) {
    if (!root) return true;  // nullptr would be treated as false in C++ 11.
    return isBalanced(root->left) && isBalanced(root->right) &&
           (abs(Depth(root->left) - Depth(root->right)) <= 1);
  }

  int Height(const TreeNode* root) {
    if (!root) return 0;
    return max(Depth(root->left), Depth(root->right)) + 1;  // Actual height + 1
  }
};
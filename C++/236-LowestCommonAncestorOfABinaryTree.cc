// Unsolved. Need more practice.

#include <iostream>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {    
    // Return the lowest common ancestor of a binary tree.
    if (!root || root == p || root == q) {
      return root;
    }
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    // If both left and right have values, means the result is root.
    // return !left ? right : !right ? left : root;
    if (!left) {
      return right;
    }
    if (!right) {
      return left;
    }
    return root;
  }
  
  // A Contain function is unnecessary
  // bool Contain(TreeNode* root, TreeNode* p) {
  //   if (root->val == p->val) {
  //     return true;
  //   }
  //   if (root->left && Contain(root->left, p)) {
  //     return true;
  //   }
  //   if (root->right && Contain(root->right, p)) {
  //     return true;
  //   }
  //   return false;
  // }
};

int main(int argc, char** argv) {
  //        -1
  //      0     3
  //   -2    4
  // 8
  TreeNode nodes[6] = {-1, 0, 3, -2, 4, 8};
  TreeNode* root = &nodes[0];
  root->left = &nodes[1];
  root->right = &nodes[2];
  root->left->left = &nodes[3];
  root->left->right = &nodes[4];
  root->left->left->left = &nodes[5];
  
  Solution solution = Solution();
  
  TreeNode* node = solution.lowestCommonAncestor(root, root->left->left->left, root->left->right);
  std::cout << "Print the lowestCommonAncestor." << std::endl;
  std::cout << node->val << std::endl;
  
  return 0;
}
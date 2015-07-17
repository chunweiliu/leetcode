#include <iostream>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
  TreeNode* invertTree(TreeNode* root) {
    // Recursively switch the left and the right sub tree
    if (!root || (root->left == NULL && root->right == NULL)) {
      return root;
    }
    Switch(root);
    if (root->left) {
      root->left = invertTree(root->left);
    }
    if (root->right) {
      root->right = invertTree(root->right);
    }
    return root;
  }

  void Switch(TreeNode* root) {
    TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;
  }

  void Print(TreeNode* root) {
    if (root->left) {
      Print(root->left);
    }
    std::cout << root->val << std::endl;
    if (root->right) {
      Print(root->right);
    }
  }
};

int main(int argc, char** argv) {
  TreeNode nodes[7] = {1, 2, 3, 4, 7, 6, 9};
  TreeNode* root = &nodes[3];
  root->left = &nodes[1];
  root->left->left = &nodes[0];
  root->left->right = &nodes[2];
  root->right = &nodes[4];
  root->right->left = &nodes[5];
  root->right->right = &nodes[6];

  // TreeNode root(4, &TreeNode(7, &TreeNode(9), &TreeNode(6)), &TreeNode(2, &TreeNode(3), &TreeNode(1)));
  Solution* solution = new Solution();

  solution->Print(root);
  root = solution->invertTree(root);
  std::cout << "Print inverted tree." << std::endl;
  solution->Print(root);
  
  delete solution;
  
  return 0;
}
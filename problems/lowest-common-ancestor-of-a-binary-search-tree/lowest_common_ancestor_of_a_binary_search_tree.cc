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
    // Return the lowest common ancestor of a "binary search tree".
    // If p is on the left and q is on the right, then return the root.
    if ((p->val <= root->val && root->val <= q->val) ||
        (q->val <= root->val && root->val <= p->val)) {
      return root;
    }
    if (p->val < root->val && q->val < root->val) {
      return lowestCommonAncestor(root->left, p, q);
    }
    if (p->val > root->val && q->val > root->val) {
      return lowestCommonAncestor(root->right, p, q);
    }
    return root;
  }

  void Print(TreeNode* root) {
    if (root) {
      std::cout << root->val << std::endl;
      if (root->left) {
        Print(root->left);
      }
      if (root->right) {
        Print(root->right);
      }
    }
  }
};

int main(int argc, char** argv) {
  TreeNode nodes[9] = {6, 2, 8, 0, 4, 7, 9, 3, 5};
  TreeNode* root = &nodes[0];
  root->left = &nodes[1];
  root->right = &nodes[2];
  root->left->left = &nodes[3];
  root->left->right = &nodes[4];
  root->right->left = &nodes[5];
  root->right->right = &nodes[6];
  root->left->right->left = &nodes[7];
  root->left->right->right = &nodes[8];

  Solution solution = Solution();
  // solution.Print(root);

  TreeNode* node = solution.lowestCommonAncestor(root, root->right->right, root->left->left);
  std::cout << "Print the lowestCommonAncestor." << std::endl;
  std::cout << node->val << std::endl;
  
  return 0;
}
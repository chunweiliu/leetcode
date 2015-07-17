#ifndef TREE_NOED_H_
#define TREE_NOED_H_

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

#endif  // TREE_NOED_H_
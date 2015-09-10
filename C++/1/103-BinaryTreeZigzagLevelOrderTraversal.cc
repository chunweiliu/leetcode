#include "leetcode.h"
#include <algorithm>

class Solution {
 public:
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
};

int main(int argc, char** argv) {
  Solution solution;
  TreeNode nodes[5] = {3, 9, 20, 15, 7};
  TreeNode* root;
  root = &nodes[0];
  root->left = &nodes[1];
  root->right = &nodes[2];
  root->right->left = &nodes[3];
  root->right->right = &nodes[4];
  const auto& levels = solution.zigzagLevelOrder(root);
  for (int i = 0; i < levels.size(); ++i) {
    for (int j = 0; j < levels[i].size(); ++j) {
      std::cout << levels[i][j] << " ";
    }
    std::cout << std::endl;
  }
  return 0;
}
#include "leetcode.h"
#include <algorithm>

class Solution {
 public:
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
  const auto& ret = solution.rightSideView(root);
  for (int i = 0; i < ret.size(); ++i) {
      std::cout << ret[i] << " ";
  }
  return 0;
}
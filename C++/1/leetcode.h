// Helper funstions for the leetcode problems.
#ifndef LEETCODE_H_
#define LEETCODE_H_

#include <iostream>
#include <vector>

struct UndirectedGraphNode {
  int label;
  std::vector<UndirectedGraphNode*> neighbors;
  UndirectedGraphNode(int x) : label(x) {};
};

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void Print(ListNode*);
int Length(ListNode*);

// For the Sublime Text 3 ctrl + b compile option, putting the implementation in
// a seperated *.cc file will not work. Decision: Merge the *.cc and *.h files.
void Print(ListNode* root) {
  ListNode* current = root;
  while (current) {
    std::cout << current->val << "->";   
    current = current->next;   
  }
  std::cout << "." << std::endl;
}

int Length(ListNode* root) {
  ListNode* current = root;
  int length = 0;
  while (current) {
    length++;
    current = current->next;
  }
  return length;
}

#endif  // LEETCODE_H_
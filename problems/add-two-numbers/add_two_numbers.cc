// Definition for singly-linked list.
#include "leetcode.h"
// #include "linked-list.h"
 
class Solution {
 public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    if (l1 == NULL) {
      return l2;
    }
    if (l2 == NULL) {
      return l1;
    }
    ListNode* ret = l1;
    int carry = 0;
    while (true) {
      l1->val += l2->val + carry;
      if (l1->val > 9) {
        carry = 1;
        l1->val -= 10;
      } else {
        carry = 0;
      }
      if (l1->next == NULL) {
        l1->next = l2->next;  // L1 is finished. Move l2 to l1 to continue.
        break;
      } else if (l2->next == NULL) {
        break;
      }
      l1 = l1->next;
      l2 = l2->next;
    }
    while (l1->next != NULL && carry) {  // Need to check the last node.
      l1 = l1->next;  // Aware!
      l1->val += carry;
      if (l1->val > 9) {
        carry = 1;
        l1->val -= 10;
      } else {
        return ret;
      }
    }
    if (carry) {  // Add a new node by the head of l2.
      l2->val = carry;
      l2->next = nullptr;
      l1->next = l2;
    }
    return ret;
  }

  ListNode* addTwoNumbersLeak(ListNode* l1, ListNode* l2) {
    // Define a dummy node for linked list operation.
    ListNode header(-1), *current = &header;
    int carry = 0;
    while (l1 || l2 || carry) {
      int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
      current->next = new ListNode(sum % 10);  // Memory leaks!
      current = current->next;

      carry = sum / 10;
      l1 = l1 ? l1->next : nullptr;
      l2 = l2 ? l2->next : nullptr;
    }
    return header.next;
  }
};

int main(int argc, char** argv) {
  Solution solution;
  ListNode nodes[2] = {2, 0};

  ListNode* l1 = &nodes[0];
  // Print(l1);

  ListNode* l2 = &nodes[1];
  // l2->next = &nodes[2];
  // Print(l2);

  ListNode* root = solution.addTwoNumbers(l1, l2);
  Print(root);
  return 0;
}
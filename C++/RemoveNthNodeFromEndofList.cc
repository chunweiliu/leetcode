#include <iostream>


// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *_next) : val(x), next(_next) {}
  ~ListNode() {
    //std::cout << "ListNode" << " " << val << " " << "delete" << std::endl;
  }
};

class RemoveNthFromEndofList {
public:
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    ListNode dummy{-1};
    dummy.next = head;
    ListNode *front = &dummy, *back = &dummy;
    for (int i = 0; i < n; ++i) {
      front = front->next;
    }
    while (front->next) {
      front = front->next;
      back = back->next;
    }
    ListNode *tmp = back->next;
    back->next = back->next->next;
    delete tmp;
    return dummy.next;
  }

  void print_list(ListNode *head) {
    while (head) {
      std::cout << head->val << " ";
      head = head->next;
    }
  }
};

int main()
{
  ListNode *head = new ListNode(1, new ListNode(2, new ListNode(3)));
  RemoveNthFromEndofList remove_nth_from_end_of_list;

  remove_nth_from_end_of_list.print_list(head);
  head = remove_nth_from_end_of_list.removeNthFromEnd(head, 1);
  std::cout << std::endl;
  remove_nth_from_end_of_list.print_list(head);

  delete head->next->next;
  delete head->next;
  delete head;
  return 0;
}
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == [] or head is None:
            return

        node_list = []
        curr = head

        while curr:
            node_list.append(curr)
            curr = curr.next

        curr = node_list.pop(0)
        first_flag = -1
        while node_list:
            if first_flag == 1:
                curr.next = node_list.pop(0)
            else:
                curr.next = node_list.pop()
            curr = curr.next
            first_flag *= -1
        curr.next = None
        return head

if __name__ == "__main__":
    #head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    head = []
    head = Solution().reorderList(head)
    while head:
        print head.val
        head = head.next

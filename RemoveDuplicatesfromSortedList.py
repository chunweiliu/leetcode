# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == [] or head is None:
            return

        node_list = []
        curr = head
        # use a list for storing non-duplicates
        while curr.next:
            if curr.val != curr.next.val:
                node_list.append(curr)
            curr = curr.next
        if node_list:
            if curr.val != node_list[-1].val:
                node_list.append(curr)
        else:
            node_list.append(curr)

        head_none = ListNode(0)
        curr = head_none
        while node_list:
            curr.next = node_list.pop(0)  # should edit the next
            curr = curr.next
        return head_none.next

if __name__ == "__main__":
    head = ListNode(1)
    head = Solution().deleteDuplicates(head)
    while head:
        print head.val
        head = head.next

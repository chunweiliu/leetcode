# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        prev, curr = dummy, head
        while curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        prev.next = curr  # Corner case: [1, 1]
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(1, ListNode(2)))
    new_head = Solution().deleteDuplicates(head)
    while new_head:
        print new_head.val,
        new_head = new_head.next

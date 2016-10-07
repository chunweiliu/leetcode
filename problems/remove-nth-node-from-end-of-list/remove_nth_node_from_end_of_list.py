# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Use a pair of indices, one advancing another by n step.
        fast = slow = head  # Put head in slow, and put what in slow in fast
        while n > 0:
            fast = fast.next
            n -= 1

        if not fast:  # Remove the first element
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next  # Remove the node next to slow.
        return head

if __name__ == "__main__":
    head = Solution().removeNthFromEnd(
        ListNode(0, ListNode(1)), 2)
    while head:
        print head.val,
        head = head.next

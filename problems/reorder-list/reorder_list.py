# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Seperate the list in the midpoint. Midpoint is the last node of the
        # first half.
        fast_curr = curr = head
        while fast_curr.next and fast_curr.next.next:
            curr = curr.next
            fast_curr = fast_curr.next.next
        midpoint = curr

        # Reverse the list after the midpoint.
        new_head = self.reverse(curr.next)
        midpoint.next = None

        # Alternatively link two lists.
        curr = ListNode(0)
        alternative = False
        while head or new_head:
            if alternative:
                curr.next = new_head
                new_head = new_head.next
            else:
                curr.next = head
                head = head.next
            curr = curr.next
            alternative = not alternative

    def reverse(self, head):
        if not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev, last, curr = dummy, head, head.next
        while curr:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        return dummy.next

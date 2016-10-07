# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # Find the middle point.
        mid, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            mid = mid.next

        # In either odd or even list, just reverse the node after the
        # mid point and compare the right half.
        # E.g [1 2 3 2 1] -> mid = 3
        # E.g [1 2 2 1] -> mid = 2
        right = self.reverse(mid.next)

        while right:
            if right.val != head.val:
                return False
            right = right.next
            head = head.next
        return True

    def reverse(self, head):
        if not head or not head.next:
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

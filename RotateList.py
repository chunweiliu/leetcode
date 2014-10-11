# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        """Rotate
        Time: O(n)
        Space: O(1)
        Corner: only one node, rotate around, k = 0
        """
        def find_length(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length

        def find_kth_last(head, k):
            dummy = ListNode(0)
            dummy.next = head
            prev = dummy
            curr = ahead = head
            while k > 1:
                ahead = ahead.next
                k -= 1

            while ahead.next:
                prev = curr
                curr = curr.next
                ahead = ahead.next
            return (prev, curr, ahead)

        if not head or not head.next:
            return head

        k = k % find_length(head)  # avoid circle
        if k == 0:
            return head

        new_tail, new_head, new_body = find_kth_last(head, k)
        new_body.next = head
        new_tail.next = None
        return new_head

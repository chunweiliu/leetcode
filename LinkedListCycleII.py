# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# [1 -> 2 -> 1]
#   i  0 1 2 3
#slow  1 2 1 2
#fast  1 1 1 1
#slow2     1 2


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        """The length from head to the start of cycle is k
        The length from fast and slow meet to the start of cycle is k
                         +++++++++---
        Time: O(n)          k  |    |
        Space: O(1)             \__/
        """
        fast = slow = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            if fast is slow:
                break
        if fast is None:
            return None

        slow2 = head  # slow and slow2 will meet at cycle after k iterations
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow

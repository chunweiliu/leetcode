# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Example:
            1 -> 1 -> 1
        =>  1 -> None

        meta: clean code
        """
        curr = head

        while curr:
            next = curr.next
            while next and next.val == curr.val:
                next = next.next

            curr.next = next
            curr = curr.next

        return head
        
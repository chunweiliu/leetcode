# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        # Make sure change curr.next instead of curr
        # Time: O(n)
        # Space: O(1)
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = ListNode(0)
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1  # change curr.NEXT, not curr
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next  # curr advance

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return head.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(2)))
    l2 = ListNode(2)
    head = Solution().mergeTwoLists(l1, l2)
    while head:
        print head.val
        head = head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        """Find the next
        Time: O(n)
        Space: O(1)
        Corner: None pointer
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(2)))
    l2 = ListNode(2)
    head = Solution().mergeTwoLists(l1, l2)
    while head:
        print head.val
        head = head.next

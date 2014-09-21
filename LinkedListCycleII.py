# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        # The intersection is the start of the cycle iff fast and slow start at
        # the start of the cycle
        # Time: O(n)
        # Space: O(1)


if __name__ == "__main__":
    head = ListNode(1, ListNode(2))
    head.next = head
    a = Solution().detectCycle(head)
    print a.val

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        # Draw a figure to understand the connection rule
        # Time: O(n)
        # Space: O(1)
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        step = 0
        while step < m - 1:  # move to the begining
            prev = curr
            curr = curr.next
            step += 1

        last = prev.next  # add a dummy for this prev.next
        while step < n - 1:  # move to the end
            # reverse here
            curr = last.next
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            step += 1
        return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    m = 1
    n = 3
    head = Solution().reverseBetween(head, m, n)
    while head:
        print head.val
        head = head.next

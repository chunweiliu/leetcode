# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        # Reverse the second half and reorder the list in place
        # Time: O(N)
        # Space: O(1)
        if head == [] or head is None:
            return

        # Find the second half by two pointers trick
        half = self.findHalf(head)

        # Reverse the second half
        reversed_half = self.reverse(half)

        # Reorder the list
        curr = head
        curr_r = reversed_half
        while curr_r:
            next, next_r = curr.next, curr_r.next
            curr.next = curr_r
            curr_r.next = next
            curr, curr_r = next, next_r
        half.next = None

    def findHalf(self, head):
        fast = head
        slow = head
        while head:
            if fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
            else:
                break
            if slow.next:
                slow = slow.next
        return slow

    def reverse(self, head):
        prev, curr, next = None, head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = Solution().reorderList(head)
    while head:
        print head.val
        head = head.next

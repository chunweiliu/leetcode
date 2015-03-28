# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        # Use fast and slow pointers to find cycle
        # Time: O(n)
        # Space: O(1)
        fast = head
        slow = head
        while fast:
            if fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
                else:
                    break
            else:
                break
            if slow.next:
                slow = slow.next
            if fast is slow:
                return True
        return False


if __name__ == "__main__":
    head = ListNode(0, ListNode(1))
    print Solution().hasCycle(head)

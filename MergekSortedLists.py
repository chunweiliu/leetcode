# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        """Two solutions
        1. Use a data structure to maintain k candidates as heap
        Time: O(n log k)
        Space: O(k)
        2. Recursively Merge two lists
        Time: O(n log k)
        Space: O(n log k)
        Corner: length == 0 or 1
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]  # return a ListNode
        if len(lists) == 2:
            return self.merge_two_list(lists[0], lists[1])

        head1 = self.mergeKLists(lists[:len(lists)/2])
        head2 = self.mergeKLists(lists[len(lists)/2:])
        return self.mergeKLists([head1, head2])

    def merge_two_list(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        head = tail = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                current = head1
                head1 = head1.next
            else:
                current = head2
                head2 = head2.next
            tail.next = current
            tail = tail.next
        tail.next = head1 or head2
        return head.next

if __name__ == "__main__":
    lists = [ListNode(5, ListNode(6)), ListNode(4), ListNode(2, ListNode(3))]
    #lists = [[]]
    head = Solution().mergeKLists(lists)
    while head:
        print head.val
        head = head.next

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        """Split list into two parts, recursive found the median
        Time: O(n)
        Space: O(n)
        """
        def get_linked_list_length(head):
            count = 0
            while head:
                head = head.next
                count += 1
            return count

        def advance_linked_list(head, step):
            prev = None
            while step:
                prev = head
                head = head.next
                step -= 1
            return (prev, head)

        def split_linked_list(head):
            length = get_linked_list_length(head)
            left_tail, median = advance_linked_list(head, length/2)

            # deal with left
            left = None if median is head else head  # for n = 1
            if left_tail:
                left_tail.next = None

            # deal with right and median
            right = median.next
            median.next = None

            return (left, median, right)

        if not head:
            return None

        left, median, right = split_linked_list(head)
        root = TreeNode(median.val)

        if left:
            root.left = self.sortedListToBST(left)
        if right:
            root.right = self.sortedListToBST(right)
        return root



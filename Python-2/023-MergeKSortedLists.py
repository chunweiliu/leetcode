from heapq import heapify, heappop, heapreplace


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Depend on the size of k, we might want to use different DS.
        # If k is small, use indices, otherwise use heap.
        dummy = current_node = ListNode(-1)
        heap = [(node.val, node) for node in lists if node]  # Add value field
        heapify(heap)

        while heap:
            value, node = heap[0]
            current_node.next = node
            current_node = current_node.next
            if node.next:
                heapreplace(heap, (node.next.val, node.next))

                # The heappushpop push an element to the heap first, if the
                # element is not larger than the one in the heap, then the
                # heap[0] would always return the same node. Don't use pushpop.
                # heappushpop(heap, (node.next.val, node.next))
            else:
                heappop(heap)
        return dummy.next

if __name__ == '__main__':
    l0 = ListNode(0, ListNode(0, ListNode(0)))
    l1 = ListNode(1, ListNode(3, ListNode(4, ListNode(6))))
    lists = [l0, l1]
    l = Solution().mergeKLists(lists)
    while l:
        print l.val
        l = l.next

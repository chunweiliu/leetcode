import heapq
import unittest


class Bit:
    def find_next_large(self, n):
        """Find next larger integer with the same numbers of bits
        Time: O(b)
        Space: O(1)
        """
        # 10011...01100
        #         k <-
        # 10011...10100
        # 10011...10001
        def set_bit(n, k, b):
            if b:
                return (n | (1 << k))
            else:
                return (n & ~(1 << k))

        def find_bit(n, k):
            return (n & (1 << k)) > 0
            # return n >> k & 1

        # find monotonic increasing
        bit_index = 0
        zero_count = 0
        while find_bit(n, bit_index) == 0:
            bit_index += 1
            zero_count += 1
        while find_bit(n, bit_index) == 1:
            bit_index += 1

        # set swap the (0, 1) in not monotonic place
        n = set_bit(n, bit_index, 1)
        n = set_bit(n, bit_index-1, 0)

        # reverse the rest of bits
        bit_index -= 2
        while zero_count > 0:
            n = set_bit(n, bit_index, 0)
            bit_index -= 1
            zero_count -= 1
        while bit_index >= 0:
            n = set_bit(n, bit_index, 1)
            bit_index -= 1
        return n

    #Elements of programming interviews (C0)
    def parity(self, bits):
        """Check how many bits is one
        Time: O(b)
        Space: O(1)
        """
        solution = 0
        while bits:
            #solution ^= bits & 1  # why not? not shift
            solution ^= 1
            bits &= bits - 1  # drop the LSB, the rest of bits don't change
        return solution

    def swap_bit(self, n, i, j):
        """If two bits are different, XOR them with 1 (swap)
        Time: O(1)
        Space: O(1)
        """
        if (n >> i) & 1 != (n >> j) & 1:
            n ^= (1 << i | 1 << j)
        return n

    def addBinary(self, a, b):
        """Bit operation
        Time: O(n)
        Space: O(1)
        Corner: carry
        """
        if a is None:
            return b
        if b is None:
            return a

        # add as binary
        a, b = map(int, a), map(int, b)
        c = list()
        s = 0
        while a or b:
            s /= 2
            if a:
                s += a[-1]
                a.pop()
            if b:
                s += b[-1]
                b.pop()
            c.append(s % 2)
        if s/2 > 0:
            c.append(1)
        return ''.join(map(str, c[::-1]))


class Stack:
    def __init__(self, value=list(), max=list()):
        self.value = value
        self.max = max

    def push(self, value):
        self.value.append(value)
        if self.max:
            current_max = self.max[-1][0]
            if current_max < value:
                self.max.append([value, 1])
            elif current_max == value:
                current_max[1] += 1
        else:
            self.max.append([value, 1])

    def pop(self):
        drop = self.value.pop()
        if drop == self.max[-1][0]:
            if self.max[-1][1] == 1:
                self.max.pop(-1)
            else:
                self.max[-1][1] -= 1
        else:
            pass
        return drop

    def get_max(self):
        if self.max:
            return self.max[-1][0]
        else:
            return None

    def honai_move(self, n, towers, start, to, temp):
        """Recursively move as follow:
        1. Move n - 1 from current to temporal
        2. Move the last one from current to destination
        3. Move n - 1 from temporal to destination
        """
        if n > 0:
            self.honai(n - 1, towers, start, temp, to)
            towers[to].insert(0, towers[start].pop())
            self.honai(n - 1, towers, temp, to, start)


class String:
    def permute_string(self, s):
        """Permutate all orders of a string
        Time: O(n!)
        Space: O(n!)
        """
        if len(s) <= 1:
            return [s]
        ret = list()
        char = s[0]
        reminders = self.permute_string(s[1:])
        for reminder in reminders:
            for x in range(len(reminder) + 1):
                reminder_list = list(reminder)
                reminder_list.insert(x, char)
                ret.append(''.join(reminder_list))
        return ret

    # sort using key function, key is the value for comparison
    def sort_strings(self, strings):
        """Generate key function for sorting
        Time: O(n log n)
        Space: O(n)
        """
        def generate_keys(strings):
            key_length = [len(string) for string in strings]
            key_anagram = [sorted(string) for string in strings]
            key_alphabet = strings
            return zip(key_length, key_anagram, key_alphabet)

        tuples = self.generate_keys(strings)
        sorted_tuples = sorted(tuples)
        print sorted_tuples
        return [string[-1] for string in sorted_tuples]

     # Check anonymous letter
    def is_from_texts(self, letter, texts):
        """Look up dictionary (hash table)
        Time: O(m + n) for building dictionary
        Space: O(m + n)
        """
        def get_histogram(texts):
            histogram = dict()
            for text in texts:
                try:
                    histogram[text] += 1
                except KeyError:
                    histogram[text] = 1
            return histogram

        letter_histogram = get_histogram(letter)
        text_histogram = get_histogram(texts)

        for key, value in letter_histogram.iteritems():
            if key == ' ':
                continue
            try:
                if text_histogram[key] < value:
                    return False
            except KeyError:
                return False
        return True

    def minDistance(self, word1, word2):
        """DP
        cost(word1, word2) =
        if word1[-1] == word2[-1]:
            cost(word1[:m-1], word2[:n-1])
        else:
            1 + min of
            cost(word1[:m-1], word2[:n-1])  # substitute last w1 with last w2
            cost(word1[:m-1], word2)  # insert the last of w1
            cost(word1, word2[:n-1])  # delete the last of w2
        Time: O(mn)
        Space: O(n), n is the smaller one
        Corners: word2 is empty string
        """
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        columns = len(word2) + 1
        last_costs = range(columns)
        for i, w1 in enumerate(word1):
            this_costs = [i + 1] * columns
            for j, w2 in enumerate(word2):
                if w1 == w2:
                    this_costs[1 + j] = last_costs[j]
                else:
                    this_costs[1 + j] = 1 + min(this_costs[j], min(
                        last_costs[j], last_costs[1 + j]))
            last_costs = this_costs
        return last_costs[-1]

    def atoi_re(self, str):
        """Find a string of digits if any, then int the string
        """
        if len(str) == 0:
            return str
        import re
        try:
            signed_digits = int(re.search(r'-\d+', str).group())
        except AttributeError:
            signed_digits = None
            try:
                digits = int(re.search(r'\d+', str).group())
            except AttributeError:
                digits = None
        return signed_digits if signed_digits else digits

    def atoi(self, str):
        """Corner cases
        Valid:
        1. space in the front
        2. sign
        3. digits
        4. characters in the end
        5. range
        Not valid:
        1. empty string
        2. first element is character
        """
        if len(str) == 0:
            return 0

        # skip leading space
        p = 0
        while p < len(str) and str[p] == ' ':
            p += 1

        # sign check
        sign = 1
        if str[p] == '-':
            sign = -1
            p += 1
        elif str[p] == '+':
            p += 1

        digits = 0
        while p < len(str) and str[p].isdigit():
            digits = digits*10 + int(str[p])
            p += 1

        if p == 0:
            return 0
        else:
            # range check for integer
            ret = sign * digits
            if ret > 2147483647:
                return 2147483647
            if ret < -2147483648:
                return -2147483648
            return ret

    keyboard = dict()
    keyboard['1'] = ''
    keyboard['2'] = 'abc'
    keyboard['3'] = 'def'
    keyboard['4'] = 'ghi'
    keyboard['5'] = 'jkl'
    keyboard['6'] = 'mno'
    keyboard['7'] = 'pqrs'
    keyboard['8'] = 'tuv'
    keyboard['9'] = 'wxyz'
    keyboard['0'] = ' '

    def letterCombinations(self, digits):
        """Enumerate all results through recursive (ref: Permutations.py)
        Time: O(n)
        Space: O(1)
        Corner: len(digits) is 0 or 1
        """
        if len(digits) == 0:
            return ['']
        if len(digits) == 1:
            return list(self.keyboard[digits])

        prefix = self.keyboard[digits[0]]
        surfix = self.letterCombinations(digits[1:])
        new_words = list()
        for word in surfix:
            for character in prefix:
                new_words.append(''.join(character + word))
        return new_words

    def find_no_repeat(self, string):
        """
        Time: O(n)
        Space: O(k), k is # of different keys
        corner cases: no output?
        """
        # compute a frequency table
        table = dict()
        for s in string:
            try:
                table[s] += 1
            except KeyError:
                table[s] = 1

        # go through the table
        for s in string:
            if table[s] > 1:
                continue
            return s  # table[s] == 1
        return None  # corner


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class List:
    def reverse(self, head):
        """Reverse linked list
        Time: O(n)
        Space: O(1)
        """
        if head.next is None:
            return head
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

    def reverse_pair(self, head):
        """Reverse linked list in 2 pairs in place
        Time: O(n)
        Space: O(1)
        """
        if head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next:
            last = prev.next
            curr = last.next
            if curr is None:
                break
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            prev = last
        return dummy.next

    def reverse_kpair(self, head, k):
        """Reverse linked list in k pairs in place
        Time: O(n)
        Space: O(1)
        """
        # why k = 1 failed?
        prev, next = None, None
        curr = head
        step = 0
        while curr and step < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            step += 1
        if next:
            head.next = self.reverse_kpair(next, k)
        return prev

    def merge_two_lists(self, head1, head2):
        """Merge two linked lists in place
        Time: O(n) n is smaller than m
        Space: O(1)
        """
        # Corner cases:
        # 1. None headers, 2. run out of anyone
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

    def merge_k_lists(self, lists):
        """Use merge_two_lists with recursive
        Time: O(n log k)
        Space: O(k)
        Corner: return list node
        """
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            return self.merge_two_lists(lists[0], lists[1])

        head1 = self.merge_k_lists(lists[:len(lists)/2])
        head2 = self.merge_k_lists(lists[len(lists)/2:])
        return self.merge_k_lists([head1, head2])

    def removeNthFromEnd(self, head, n):
        """End advance front with n nodes
        Time: O(#node)
        Space: O(1)
        Corner cases: n = 0, 1
        """
        if n == 0:
            return head

        # Need dummy for special case
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        front = end = head

        # advance end
        while n > 0:
            end = end.next
            n -= 1

        # advance both
        while end:
            prev = front
            front = front.next
            end = end.next

        # remove front
        prev.next = front.next
        front.next = None

        return dummy.next

    def addTwoNumbers(self, l1, l2):
        """Advance l1 and l2 together, aware carry
        Time: O(n)
        Space: O(1)
        Corner: empty list, carry > 0
        """
        curr1, curr2 = l1, l2
        curr = dummy = ListNode(0)
        num = 0
        while curr1 or curr2:
            num /= 10  # as carry
            if curr1:
                num += curr1.val
                curr1 = curr1.next
            if curr2:
                num += curr2.val
                curr2 = curr2.next
            curr.next = ListNode(num % 10)
            curr = curr.next

        if num / 10 == 1:  # max
            curr.next = ListNode(1)
        return dummy.next

    def detectCycle(self, head):
        """The length from head to the start of cycle is k
        The length from fast and slow meet to the start of cycle is k
                         +++++++++---
        Time: O(n)          k  |    |
        Space: O(1)             \__/
        """
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            if fast is slow:  # cannot put in the first
                break

        if fast:  # cycle exist
            slow2 = head
            while slow is not slow2:
                slow = slow.next
                slow2 = slow2.next
            return slow
        return None

    def merge_even_old(self, head):
        """0 -> 1 -> 2 -> 3 -> 4 : 0 -> 2 -> 4 -> 1 -> 3
        Time: O(n)
        Space: O(1)
        Corner: 0 -> 1 -> 2
                e    o    ne
        """
        if not head or not head.next:
            return head

        even_tail = head  # start from zero
        odd_head = odd_tail = even_tail.next

        # advance each head by two
        next_even, next_odd = None, None
        while odd_tail.next:
            next_even = odd_head.next
            if next_even:
                next_odd = next_even.next
            else:
                next_odd = None

            even_tail.next = next_even
            even_tail = next_even

            odd_tail.next = next_odd
            odd_tail = next_odd

        even_tail.next = odd_head  # relink two parts
        return head

    def remove_kth_from_list(self, head, k):
        """Two pointers, curr and ahead
        Time: O(n)
        Space: O(1)
        Corner: 0, 1, 1 - 2
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = ahead = head

        while k > 1:
            ahead = ahead.next
            k -= 1

        while ahead.next:
            prev = curr
            curr = curr.next
            ahead = ahead.next

        prev.next = curr.next
        return dummy.next


class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Tree:
    def preorder_recursive(self, root):
        """Pre oreder traversal using recursive
        Time: O(n)        1
        Space: O(n)     2   3
        """
        if root is None:
            return
        else:
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder_recursive(self, root):
        """In order traversal using recursive
        Time: O(n)
        Space: O(n)
        """
        if root is None:
            return
        self.inorder(root.left)
        print root.val
        self.inorder(root.right)

    def postorder_recursive(self, root):
        """Post order traversal using recursive
        Time: O(n)       3
        Space: O(n)    1   2
        """
        if root is None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print root.val

    def preorder(self, root):
        """Go deep left and pop stack, if stack is empty than we are done
        Time: O(n)
        Space: O(h)
        """
        stack = list()
        curr = root
        done = False
        while not done:
            if curr:
                print curr.val
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0:
                    done = True
                else:
                    temp = stack.pop()
                    curr = temp.right

    def inorder(self, root):
        """Go deep left and pop stack, if stack is empty than we are done
        Time: O(n)
        Space: O(h)
        """
        stack = list()
        curr = root
        done = False
        while not done:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0:
                    done = True
                else:
                    temp = stack.pop()
                    print temp.val
                    curr = temp.right

    def inorder_with_parent(self, root):
        """Inorder traversal with parent nodes
        Time: O(n)
        Space: O(1)
        """
        prev, curr = None, root
        while curr:
            if prev is None or prev.left is curr or prev.right is curr:  # down
                if curr.left:
                    next = curr.left
                else:
                    print curr.val
                    next = curr.right if curr.right else curr.parent
            else:  # going up
                if prev is curr.left:
                    print curr.val
                    next = curr.right if curr.right else curr.parent
                else:  # subtree over
                    curr = curr.parent
            prev = curr
            curr = next

    def postorder(self, root):
        """Push nodes to instack and pop them to outstack
        Time: O(n)
        Space: O(n)
        """
        in_stack = list()
        out_stack = list()
        curr = root

        in_stack.append(curr)
        while len(in_stack) > 0:
            temp = in_stack.pop()
            if temp:
                if temp.left:
                    in_stack.append(temp.left)
                if temp.right:
                    in_stack.append(temp.right)
            out_stack.append(temp)
        while len(out_stack) > 0:
            temp = out_stack.pop()
            print temp.val

    def build_binary_search_tree(self, A):
        """Build binary tree recursivly given a sorted array
        Time: O(log n)
        Space: O(h)
        """
        #     3
        #   2   4
        # 1       5
        if len(A) == 0:
            return
        elif len(A) == 1:
            return TreeNode(A[0])
        else:
            m = len(A) / 2
            root = TreeNode(A[m])
            root.left = self.build_binary_search_tree(A[:m])
            root.right = self.build_binary_search_tree(A[m+1:])
            return root

    def common_ancestor(self, r, p, q):
        """Find the first root for two nodes split in left and right
        Time: O(n)
        Space: O(h)
        """
        def cover(root, node):
            if root is None:
                return False
            if root is node:
                return True
            return cover(root.left, node) or cover(root.right, node)

        if cover(r.left, p) and cover(r.left, q):
            ret = self.common_ancestor(r.left, p, q)
        if cover(r.right, p) and cover(r.right, q):
            ret = self.common_ancestor(r.right, p, q)
        return ret

    # Match trees
    def contain_tree(self, t1, t2):
        """Test if tree 2 (n) is in tree 1 (m)
        Time: O(mn)
        Space: O(1)
        """
        def subtree(t1, t2):

            def match_tree(t1, t2):
                if t1 is None and t2 is None:
                    return True
                if t1 is None or t2 is None:
                    return False
                return match_tree(t1.left, t2.left) and \
                    match_tree(t1.right, t2.right)

            if t1.val == t2.val:
                if match_tree(t1, t2):
                    return True
            else:
                return subtree(t1.left, t2) or subtree(t1.right, t2)

        if t2 is None:
            return True
        else:
            return subtree(t1, t2)

    # Valid binary search tree
    def is_valid_bst1(self, root):
        """Check each root is vaild or not
        Time: O(n)
        Space: O(h) for recursives
        """
        MAX_VALUE = 10 ** 10
        MIN_VALUE = -10 ** 10

        def is_valid_bst_recursive(self, root, lower, upper):
            if root is None:
                return True
            elif root.val <= lower or root.val >= upper:
                return False
            return is_valid_bst_recursive(root.left, lower, root.val)\
                and is_valid_bst_recursive(root.right, root.val, upper)

        return is_valid_bst_recursive(root, MIN_VALUE, MAX_VALUE)

    def is_valid_bst2(self, root):
        """Perform Morris traversal and check if all current > previous node
        Morris traversal: link the last left subtree node's right to the root
        Time: O(n)
        Space: O(1)
        """
        MIN_VALUE = -1000000
        if root is None:
            return True

        ret = True
        curr = root
        last_value = MIN_VALUE
        while curr:
            if curr.left:
                pred = curr.left
                # find the end node of the left subtree
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if pred.right:  # pred.right is curr
                    pred.right = None  # revert the next link
                    if last_value >= curr.val:
                        ret = False
                    last_value = curr.val
                    curr = curr.right
                else:
                    pred.right = curr
                    curr = curr.left
            else:
                if last_value >= curr.val:
                    ret = False
                last_value = curr.val
                curr = curr.right
        return ret

    def buildTree_preorder_inorder(self, preorder, inorder):
        """Recursively build tree
        Time: O(n log n) average
        Space: O(log n)
        """
        if not preorder:
            return None

        root = preorder[0]
        left_count = inorder.index(root)  # elements in left tree

        left_inorder = inorder[:left_count]
        left_preorder = preorder[1:1+left_count]

        right_inorder = inorder[1+left_count:]
        right_preorder = preorder[1+left_count:]

        ret = TreeNode(root)
        ret.left = self.buildTree_preorder_inorder(left_preorder, left_inorder)
        ret.right = self.buildTree_preorder_inorder(
            right_preorder, right_inorder)
        return ret

    def buildTree_inorder_postorder(self, inorder, postorder):
        """Recuresively build
        Time: O(n log n) in average
        Space: O(log n) in average
        """
        if not postorder:
            return None

        root_val = postorder[-1]
        left_count = inorder.index(root_val)

        left_inorder = inorder[:left_count]
        left_postorder = postorder[:left_count]

        right_inorder = inorder[1+left_count:]
        right_postorder = postorder[left_count:len(postorder)-1]  # end index!

        root = TreeNode(root_val)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root

    def hasPathSum(self, root, sum):
        """Traverse from root to leaves, if any return True
        Time: O(n)
        Space: O(n)
        Style: Using RETURN values
        """
        def preorder(root, sum):
            if not root.left and not root.right:  # leaves
                return True if sum == 0 else False

            found = False
            if root.left:
                found |= preorder(root.left, sum - root.left.val)
            if root.right:
                found |= preorder(root.right, sum - root.right.val)
            return found

        if not root:
            return False
        return preorder(root, sum - root.val)

    def pathSum(self, root, sum):
        """Find all paths from root to leaves had path sum equal to sum
        Time: O(n)
        Space: O(n)
        Style: Using a CONTAINER
        """
        def path_finder(root, sum, path, paths):
            if not root.left and not root.right:  # leaves
                if sum == 0:
                    paths.append(path)

            if root.left:  # copy of path, so they won't affect each
                path_finder(root.left, sum-root.left.val,
                            list(path+[root.left.val]), paths)
            if root.right:
                path_finder(root.right, sum-root.right.val,
                            list(path+[root.right.val]), paths)
        if not root:
            return list()

        paths = list()
        path_finder(root, sum-root.val, [root.val], paths)
        return paths

    def maxPathSum(self, root):
        """Record max path so far in a container
        Time: O(n)
        Space: O(n)
        Style: Using MEMBER
        """
        def maxPathSumRec(self, root):
            if not root:
                return 0

            left_sum = self.maxPathSumRec(root.left)
            right_sum = self.maxPathSumRec(root.right)

            if left_sum < 0 and right_sum < 0:
                self.max_value = max(self.max_value, root.val)
                level_max = root.val
            else:
                if left_sum > 0 and right_sum > 0:
                    self.max_value = max(self.max_value,
                                         left_sum + root.val + right_sum)

                level_max = max(left_sum, right_sum) + root.val
                self.max_value = max(self.max_value, level_max)
            return level_max

        self.max_value = float('-inf')
        self.maxPathSumRec(root)
        return self.max_value


class Array:
    def find_k_max(self, A, k):
        """Find top k elements in an array
        Time: O(k^2 n)
        Space: O(k)
        """
        top_k = list()
        for y in range(k):
            max_value = A[0]
            for x in range(1, len(A)):
                if A[x] not in top_k:
                    if A[x] > max_value:
                        max_value = A[x]
            top_k.append(max_value)
        return top_k.pop()

    # Find kth max
    def find_kth_max(self, numbers, k):
        """Applying find max kth Time
        Time: O(kn)
        Space: O(1)
        """
        def find_max(numbers):
            max_value = max(numbers)
            max_index = numbers.index(max_value)
            return (max_value, max_index)

        step = 0
        while step < k:
            max_value, max_index = find_max(numbers[step:])
            numbers[step], numbers[max_index + step] = \
                numbers[max_index + step], numbers[step]
            step += 1
        return max_value

    def dutch_flag(self, A, pivot, start, end):
        """Partition A into three group
        Time: O(n)
        Space: O(1)
        """
        smaller, equal, larger = start, start, end
        while equal <= larger:
            if A[equal] < pivot:
                A[equal], A[smaller] = A[smaller], A[equal]
                smaller += 1
                equal += 1
            elif A[equal] == pivot:
                equal += 1
            else:
                A[equal], A[larger] = A[larger], A[equal]
                larger -= 1
        return smaller  # small already exceed to the pivot position

    def find_kth_small(self, A, k):
        """Apply Dutch flag log n times
        Time: O(n) in average, where T(n) = O(n) + T(n/2), T(n) = O(n)
        Space: O(1)
        """
        start, end = 0, len(A) - 1
        while start <= end:
            pivot = A[(start + end) / 2]
            rank = self.dutch_flag(A, pivot, start, end)

            if rank == k - 1:  # k to the index
                return pivot
            elif rank > k - 1:
                end = rank - 1
            else:
                start = rank + 1

    def find_median(self, numbers):
        """Find median by binary search with dutch flag algorithm
        Time: O(n) in average! worse case O(n^2) (median of medians O(n))
        Space: O(1)
        """
        return self.find_kth_small(numbers, 1 + len(numbers)/2)

    def rearrange(self, numbers):
        """Rearrange numbers to N0 < N1 > N2 < N3 > N4 ...
        Finding median and partition the list into left and right
        Time: O(n)
        Space: O(n)
        Corner: zero or one instance, two numbers
        """
        median = self.find_median(numbers)
        greater = [x for x in numbers if x > median]
        smaller = [x for x in numbers if x < median]
        equalto = [x for x in numbers if x == median]

        while equalto:  # smaller always >= larger
            need = smaller if len(greater) >= len(smaller) else greater
            need += [equalto.pop()]

        for i, number in enumerate(numbers):
            if i % 2 != 0:
                numbers[i] = greater[i/2]
            else:
                numbers[i] = smaller[i/2]

        # final check:
        for i, number in enumerate(numbers):
            if i % 2 == 1 and i < len(numbers) - 1:
                if number <= numbers[i - 1] or \
                   number <= numbers[i + 1]:
                    return None
        return numbers

    def rearrange2(self, numbers):
        """Rearrange numbers to N0 < N1 > N2 < N3 > N4 ...
        *** THIS IS NOT A CORRECT ANSWER ***
        Time: O(n)
        Space: O(1)
        Corner: zero or one instance, two numbers
        """
        if not numbers or len(numbers) == 1:
            return numbers
        if len(numbers) == 2:
            if numbers[0] > numbers[1]:
                numbers[0], numbers[1] = numbers[1], numbers[0]
            return numbers

        for i, number in enumerate(numbers):
            if i % 2 != 0:
                continue
            print numbers
            sub = numbers[i:i+3]
            if len(sub) < 2:  # corner
                pass
            else:
                sub = sorted(sub)
                sub[-1], sub[-2] = sub[-2], sub[-1]
            # How to substitude without ruin
            numbers[i:i+3] = sub
        return numbers

    def find_mode(self, A):
        """Find mode using dictionary and list
        Time: O(n)
        Space: O(n)
        """
        hist = dict()
        for x in range(len(A)):
            try:
                hist[A[x]] += 1
            except KeyError:
                hist[A[x]] = 1

        k = hist.keys()
        v = hist.values()
        return k[v.index(max(v))]

    def find_target_or_less(self, numbers, target, candidate=None):
        """Find a target in a sorted list using binary search with candidate
        Time: O(log n)
        Space: O(1)
        * modified version of find_target, find_k_or_less
        """
        if not numbers:
            return None
        if len(numbers) == 1:
            if numbers[0] <= target:
                return numbers[0]
            else:
                return candidate

        # binary search
        index = len(numbers) / 2
        median = numbers[index]
        if median == target:
            return median
        if median < target:
            return self.find_target_or_less(
                numbers[index + 1:], target, median)
        if median > target:
            return self.find_target_or_less(
                numbers[:index], target, candidate)

    def find_less_than_target(self, numbers, target, candidate=None):
        """Binary search with conditions
        Time: O(log n)
        Space: O(log n)
        """
        if not numbers:
            return None
        if len(numbers) == 1:
            return numbers[0] if numbers[0] < target else candidate

        index = len(numbers) / 2
        median = numbers[index]
        if median >= target:
            return self.find_less_than_target(
                numbers[:index], target, candidate)
        if median < target:
            return self.find_less_than_target(
                numbers[index+1:], target, median)

    def find_index_less_than_target(self, numbers, target):
        """Find index using binary search
        Time: O(log n)
        Space: O(1)
        """
        if not numbers:
            return None

        if len(numbers) == 1:
            return numbers[0] if numbers[0] < target else None

        candidate = None
        start, end = 0, len(numbers) - 1
        while start < end:
            middle = (start+end) / 2
            median = numbers[middle]

            if median >= target:
                end = middle - 1
            else:
                candidate = middle
                start = middle + 1

        return middle if median < target else candidate

    def find_target_in_rotated_sorted_array(self, numbers, target):
        """Binary search with complicated conditions
        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = (left + right) / 2
            if numbers[mid] == target:
                return mid

            if numbers[mid] >= numbers[left]:  # order in the front
                if numbers[left] <= target and target < numbers[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # order in the end
                if numbers[mid] < target and target <= numbers[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return None

    def find_index_larger_than_k(self, numbers, k):
        """Binary search with a candidate variable
        Time: O(log n)
        Space: O(1)
        """
        if len(numbers) == 0:
            return -1
        if len(numbers) == 1:
            if numbers[0] > k:
                return 0
            else:
                return -1

        start, end = 0, len(numbers) - 1
        candidate = -1
        while start <= end:
            mid = (start + end) / 2
            if numbers[mid] <= k:
                start = mid + 1
            else:
                candidate = mid
                end = mid - 1
        return candidate

    def find_ai_equal_i(A):
        """BS A[i] - i: Assume A[i] is distinguish to others and A is sorted
        Time: O(log n)
        Space: O(1)
        Corner: empty array
        """
        if len(A) == 0:
            return -1
        p, q = 0, len(A)
        mid = p + q / 2
        while p <= q:
            if A[mid] == mid:
                return mid
            elif A[mid] > mid:
                q = mid - 1
            else:
                p = mid + 1
        return -1

    def make_changes(self, n, coin=25):
        """Recursive make changes for n amount using m coins
        Time: O(nm)
        Space: O(m)
        """
        # $100 -> n=100, coin=25
        # make_changes(100, 0)+make_changes(75, 0)+...+make_changes(25, 0)+1
        ways = 0
        if coin == 25:
            next_coin = 10
        elif coin == 10:
            next_coin = 5
        elif coin == 5:
            next_coin = 1
        elif coin == 1:
            return 1

        ways, coin_num = 0, 0
        while coin_num * coin <= n:
            ways += self.make_changes(n - coin_num * coin, next_coin)
            coin_num += 1
        return ways

    def twoSum(self, num, target):
        """Reduce range by two pointers
        Time: O(n log n)
        Space: O(1)
        Corner: return original index
        """
        if not num or len(num) < 2:
            return None

        # append original index in front
        sorted_num = sorted(enumerate(num), key=lambda num: num[1])

        p, q = 0, len(num) - 1
        while p < q:
            s = sorted_num[p][1] + sorted_num[q][1]
            if s == target:
                break
            if s > target:
                q -= 1
            else:
                p += 1

        # compute original index
        small, large = sorted_num[p][0]+1, sorted_num[q][0]+1
        if small > large:
            small, large = large, small
        return (small, large)

    def threeSum(self, num):
        """Find three sum using two pointers (in a sorted array)
        Time: O(n^2)
        Space: O(1)
        """
        num.sort()
        ans = list()
        for i, a in enumerate(num):
            if i > 0 and a == num[i - 1]:
                continue

            p, q = i + 1, len(num) - 1
            while p < q:
                # check duplicates
                if p > i + 1 and num[p] == num[p - 1]:
                    p += 1
                    continue

                if q < len(num) - 1 and num[q] == num[q + 1]:
                    q -= 1
                    continue

                b, c = num[p], num[q]
                if a + b + c == 0:
                    ans.append([a, b, c])
                    p += 1
                    q -= 1
                elif a + b + c < 0:
                    p += 1
                else:
                    q -= 1
        return ans

    def three_less_sum(self, num, d):
        """Find three sum last than d
        Time: O(n * n^2)
        Space: O(1)
        * modified version of threeSum
        """
        from itertools import combinations

        num.sort()
        ans = list()
        for a_index, a in enumerate(num):
            if a_index > 0 and a == num[a_index - 1]:
                continue

            b_index, c_index = a_index + 1, len(num) - 1
            while b_index < c_index:
                b, c = num[b_index], num[c_index]
                if a + b + c <= d:
                    # want all none duplicates in [b, c]
                    all_pairs = [(a, comb[0], comb[1])for comb in combinations(
                        set(num[b_index:c_index+1]), 2)]  # set prevents dups
                    ans += all_pairs  # += concatinate lists to one list
                    break
                else:
                    c_index -= 1
        return ans

    def get_products(self, numbers):
        """Find products of numbers using comulative products
        Time: O(n)
        Space: O(n)
        """
        if len(numbers) == 0:
            return numbers
        # what about len(numbers) == 1?
        if len(numbers) == 1:
            return None

        # products[0] =     3 * 4 * 5
        # products[1] = 1     * 4 * 5
        # products[2] = 1 * 3     * 5
        products_before = [0] * len(numbers)
        for i, number in enumerate(numbers):
            if i == 0:
                products_before[i] = number
            else:
                products_before[i] = number * products_before[i - 1]

        products_after = [0] * len(numbers)
        for i, number in enumerate(reversed(numbers)):
            if i == 0:
                products_after[-1 - i] = number
            else:
                products_after[-1 - i] = number * products_after[-i]

        products = [0] * len(numbers)
        for i, (product_before, product_after) in enumerate(
                zip(products_before, products_after)):
            if i == 0:
                products[i] = products_after[1]
            elif i == len(products_before) - 1:
                products[i] = products_before[-2]
            else:
                products[i] = products_before[i - 1] * products_after[i + 1]
        return products

    def merge_sort(self, lists):
        """Using a min heap built from the lists
        Time: O(n log k), k is the heap size
        Space: O(k)
        """
        min_heap = list()
        # initialize min heap
        for i, x in enumerate(lists):
            heapq.heappush(min_heap, (x.pop(0), i))

        sorted_list = list()
        while min_heap:
            value, index = heapq.heappop(min_heap)
            sorted_list.append(value)
            if lists[index]:
                heapq.heappush(min_heap, (lists[index].pop(0), index))

        return sorted_list

    # Common elements
    def common_elements1(self, A, B):
        """Common elements of two array. Based on A binary search B
        Time: O(m log n) for m << n.
        Space: O(log n)
        """
        def has_key_bs(self, items, key):
            if len(items) == 0:
                return False

            mid = len(items) / 2
            if items[mid] == key:
                ret = True
            elif items[mid] < key:
                ret = self.has_key_bs(items[mid+1:], key)
            else:
                ret = self.has_key_bs(items[:mid], key)
            return ret

        common = list()
        prev = None
        for a in A:
            if prev != a and has_key_bs(B, a):
                common.append(a)
            prev = a
        return common

    def common_elements2(self, A, B):
        """Advance small pivot from A or B
        Time: O(m + n), using the facts that A and B are sorted
        Space: O(1)
        """
        i, j = 0, 0
        common = list()
        while i < len(A) and j < len(B):
            if A[i] == B[j] and (i == 0 or A[i] != A[i - 1]):
                common.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return common

    def sort_within_k(self, A, k):
        """Sort locally with a slide window k (approximate sort)
        Time: O(n log k)
        Space: O(k)
        Corner: len(A) < k
        """
        if len(A) == 0:
            return None

        # recruiting
        min_heap = A[:min(len(A), k)]
        heapq.heapify(min_heap)

        # rank
        for i in range(len(A)):
            if i + k < len(A):
                A[i] = heapq.heappushpop(min_heap, A[i + k])
            else:
                A[i] = heapq.heappop(min_heap)

    def find_snakes(self, board, target):
        """Recursively find 4 directions
        Time: O(n^2)
        Space: O(1)
        """
        def search(board, target, visited, i, j):
            def is_valid(board, target, visited, i, j):
                if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
                   (i, j) in visited:
                    return False
                return True

            if target[0] != board[i][j]:
                return 0
            if len(target) == 1:  # only one charater left and match
                return 1

            visited.append((i, j))  # otherwise, need search the next
            found = 0
            if is_valid(board, target[1:], visited, i, j + 1):
                found += search(board, target[1:], visited, i, j + 1)
            if is_valid(board, target[1:], visited, i - 1, j):
                found += search(board, target[1:], visited, i - 1, j)
            if is_valid(board, target[1:], visited, i + 1, j):
                found += search(board, target[1:], visited, i + 1, j)
            if is_valid(board, target[1:], visited, i, j - 1):
                found += search(board, target[1:], visited, i, j - 1)
            return found

        found = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = list()
                found += search(board, target, visited, i, j)
        return found

    def minimum_cover_set(self, lowers, uppers):
        """Find a minimum set of points cover given interval
        Time: O(n log n)
        Space: O(1)
        """
        MIN = -100000

        sorted_intervals = sorted(zip(lowers, uppers),
                                  key=lambda interval: interval[1])

        def is_in_interval(point, interval):
            return point >= interval[0] and point <= interval[1]

        current_point = MIN
        points = list()
        for interval in sorted_intervals:
            if not is_in_interval(current_point, interval):
                current_point = interval[1]
                points.append(current_point)
        return points

    def print_power_set(self, iterable):
        """Get the power set using bit representation
        Time: O(2^n)
        Space: O(2^n)
        """
        import math
        for i in range(1 << len(iterable)):
            x = i
            while x:
                lsb = x & ~(x - 1)
                target = int(math.log(lsb, 2))  # pick lsb
                print iterable[target],
                x &= x - 1
            print

    def generate_random_not_from_set(self, n, m, black):
        """Generate N random numbers from 0 to M not in black list
        Time: O(n)
        Space: O(1)
        """
        from random import randint
        white = [x for x in range(m) if x not in black]
        while n:
            i = randint(0, len(white) - 1)
            yield white[i]
            n -= 1


class DynamicProgramming:
    def knapsack(self, items, capacity):
        """Solve pseudo-polynomial by DP
        Time: O(nw), n is number of items, w is the sum of the weights
        Space: O(w)
        """
        #sum(weight for i, (value, weight) in enumerate(items))
        values = [0] * (capacity + 1)
        for (value, weight) in items:
            print values, value, weight
            curr = capacity
            while curr - weight >= 0:
                values[curr] = max(values[curr],
                                   values[curr - weight] + value)
                curr -= 1
        return values[capacity]

    def longestConsecutive(self, num):
        """Hash table keep the longest.
        If the key is a lower interval, than the value is the upper.
        If the key is an upper interval, than the value is the lower.
        (two directions counts)
        Time: O(n)
        Space: O(k)
        Corner: len(num) == 0
        """
        if len(num) == 0:
            return None

        intervals = dict()
        for i in num:
            if i in intervals:
                continue

            lower = intervals[i - 1] if i - 1 in intervals else i
            upper = intervals[i + 1] if i + 1 in intervals else i

            intervals[i] = i  # so we don't want duplicates
            intervals[lower] = upper  # both directions count
            intervals[upper] = lower

        return max(abs(lower-upper) + 1
                   for (lower, upper) in intervals.iteritems())

    def minPathSum(self, grid):
        """DP find minimum from (i-1, j), (i, j-1)
        Time: O(mn)
        Space: O(n)
        Conner: grid is empty
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return grid

        total = 0
        path_sum = [0] * len(grid[0])
        for j, element in enumerate(grid[0]):
            total += element
            path_sum[j] = total

        for i, row in enumerate(grid):
            if i == 0:
                continue
            for j, element in enumerate(row):
                if j == 0:
                    path_sum[j] += element
                else:
                    path_sum[j] = min(path_sum[j-1] + element,
                                      path_sum[j] + element)
        return path_sum[len(grid[0]) - 1]

    def maxProduct(self, A):
        """Max continous product. DP: A[i], A[i]*pre_min, A[i]*pre_max
        Time: O(n)
        Space: O(1)
        Conner cases: len(A) == 0, 1
        """
        if len(A) == 0:
            return A

        max_so_far = A[0]
        pre_min = A[0]
        pre_max = A[0]

        for x in A[1:]:
            min_now = min(min(pre_min*x, pre_max*x), x)
            max_now = max(max(pre_min*x, pre_max*x), x)
            max_so_far = max(max_so_far, max_now)
            pre_min = min_now
            pre_max = max_now

        return max_so_far


class Recursive:
    # 8 Queens
    BOARD_SIZE = 8

    def under_attack(self, col, queens):
        left = right = col

        for r, c in reversed(queens):
            left, right = left - 1, right + 1

            if c in (left, col, right):
                return True
        return False

    def solve(self, n):
        if n == 0:
            return [[]]

        smaller_solutions = self.solve(n - 1)

        return [solution + [(n, i+1)]
                for i in xrange(self.BOARD_SIZE)
                for solution in smaller_solutions
                if not self.under_attack(i+1, solution)]
    # board = [0] * 8

    # def check_queens(self, row):
    #     for x in range(row):
    #         diff = abs(self.board[row] - self.board[x])
    #         if diff == 0 or diff == row - x:
    #             return False
    #     return True

    # def put_queen(self, row):
    #     if row == 8:
    #         #print self.board
    #         return 1

    #     total = 0
    #     for x in range(8):
    #         self.board[row] = x  # generate 8 branchs when row=0
    #         if self.check_queens(row):
    #             total += self.put_queen(row + 1)
    #     return total


class Test(unittest.TestCase):
    def setUp(self):
        self.args = ([['S', 'N', 'A'], ['S', 'E', 'K']], 'SNAKES')

    def tearDown(self):
        self.args = None

    def test_find_snake(self):
        expected = 1
        result = Array().find_snakes(*self.args)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    # Unit Test
    # suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # print Array().find_median([1, 1, 2, 3, 5])
    #print Array().find_median([2, 3, 5, 1, 1])
    # print Array().find_kth_small([2, 3, 5, 1, 1], 3)
    # print Array().find_median([2, 3, 5, 1, 1])
    print Array().rearrange([2, 1, 2])

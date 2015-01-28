import unittest


class Bit:
    def set_bit(self, n, k, b):
        if b:
            return (n | (1 << k))
        else:
            return (n & ~(1 << k))

    def get_bit(self, n, k):
        # return (n & (1 << k)) > 0
        return n >> k & 1

    def parity(self, n):
        """Check how many bits is one
        Time: O(b)

        """
        solution = 0
        while n:
            #solution ^= bits & 1  # why not? not shift
            solution ^= 1
            n &= n - 1  # drop the LSB, the rest of bits don't change
        return solution

    def swap_bit(self, n, i, j):
        """If two bits are different, XOR them with 1 (swap)
        Time: O(1)
        Space: O(1)
        """
        if self.get_bit(n, i) != self.get_bit(n, j):
            n ^= (1 << i | 1 << j)
        return n

    def addBinary(self, a, b):
        """Bit operation
        Time: O(n)
        Space: O(1)
        Corner: carry
        """
        if not a:
            return b
        if not b:
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

        # return str(bin(int(a, 2) + int(b, 2)))[2:]  # one-liner answer

    def find_next_large1(self, n):
        """Find next larger integer with the same numbers of bits
        Time: O(b)
        Space: O(1)
        """
        # 10011...01100
        #         k <-
        # 10011...10100
        # 10011...10001
        # find monotonic increasing

        bit_index = 0
        zero_count = 0
        while self.get_bit(n, bit_index) == 0:
            bit_index += 1
            zero_count += 1
        while self.get_bit(n, bit_index) == 1:
            bit_index += 1

        # set swap the (0, 1) in not monotonic place
        n = self.set_bit(n, bit_index, 1)
        n = self.set_bit(n, bit_index-1, 0)

        # reverse the rest of bits
        bit_index -= 2
        while zero_count > 0:
            n = self.set_bit(n, bit_index, 0)
            bit_index -= 1
            zero_count -= 1
        while bit_index >= 0:
            n = self.set_bit(n, bit_index, 1)
            bit_index -= 1
        return n

    def find_next_large2(self, n):
        """Find next larger integer with the same numbers of bits
        Time: O(b)
        Space: O(1)
        """
        bits = bin(n)[2:]  # represent as string
        reversed_bits = list(bits[::-1])

        # find position to swap
        for i, bit in enumerate(reversed_bits):
            if i > 0 and reversed_bits[i - 1] > bit:
                break

        # swap bits
        if i == len(reversed_bits) - 1 and reversed_bits[i - 1] <= bit:
            i += 1  # all increasing so we need to add 1
            reversed_bits[-1] = '0'
            reversed_bits.append('1')
        else:
            reversed_bits[i] = '1'
            reversed_bits[i-1] = '0'

        # reorder the reset
        reversed_bits[:i-1] = sorted(reversed_bits[:i-1], reverse=True)

        # format
        return int('0b'+''.join(reversed_bits[::-1]), 2)


class Stack:
    def __init__(self):
        self.values = list()
        self.maxs = list()  # [max_key, num_max_key]

    def push(self, value):
        self.values.append(value)

        if self.maxs:
            current_max = self.maxs[-1][0]
            if current_max < value:
                self.maxs.append([value, 1])
            elif current_max == value:
                current_max[1] += 1
        else:
            self.maxs.append([value, 1])

    def pop(self):
        drop = self.values.pop()
        if drop == self.maxs[-1][0]:
            if self.maxs[-1][1] == 1:
                self.maxs.pop(-1)
            else:
                self.maxs[-1][1] -= 1
        else:
            pass
        return drop

    def get_max(self):
        if self.max:
            return self.max[-1][0]
        else:
            return None

    def honai(self, n, towers, start, to, temp):
        """Recursively move as follow:
        1. Move n - 1 from current to temporal
        2. Move the last one from current to destination
        3. Move n - 1 from temporal to destination
        [[1, 2, 3], [], []] -> [[], [], [1, 2, 3]]
        """
        if n > 0:
            self.honai(n - 1, towers, start, temp, to)
            towers[to].insert(0, towers[start].pop(0))
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
        permuted_strings = self.permute_string(s[1:])
        for permuted_string in permuted_strings:
            for i in range(len(permuted_string) + 1):
                copy = list(permuted_string)
                copy.insert(i, char)
                ret.append(''.join(copy))
        return ret

    # sort using key function, key is the value for comparison
    def sort_strings(self, strings):
        """Generate key function for sorting (len, anagram, order)
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
            hist = dict()
            for text in texts:
                hist[text] = hist.get(text, 0) + 1
            return hist

        hist_letter = get_histogram(letter)
        hist_texts = get_histogram(texts)

        # compare two histograms
        for key, value in hist_letter.iteritems():
            if key == ' ':
                continue
            if key not in hist_texts or value > hist_texts[key]:
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
            word1, word2 = word2, word1  # |word1| > |word2|

        columns = len(word2) + 1  # why + 1?
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
        if not digits:
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
            table[s] = table.get(s, 0) + 1

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
        if not head or not head.next:
            return head

        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverse_pair(self, head):
        """Reverse linked list in 2 pairs in place
        Time: O(n)
        Space: O(1)
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next:
            last = prev.next
            curr = last.next
            if not curr:
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
        Corners: k == 0 or 1
        """
        if not head or k == 0:
            return head

        if k == 1:  # why k = 1 failed? Head.next relink to its origin next
            k = float('inf')

        prev, curr = None, head
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
        if not head1:
            return head2
        if not head2:
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
        Hint: return list node
        """
        if not lists:
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
        Time: O(#nodes)
        Space: O(1)
        Corner cases: n = 0, 1
        """
        if not head or not head.next:
            return head

        ahead = head
        while n:
            ahead = ahead.next
            n -= 1

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while ahead:
            prev = curr
            curr = curr.next
            ahead = ahead.next

        # remove curr
        prev.next = curr.next
        curr.next = None
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

        if num / 10 == 1:  # might be 10 to 19
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
            while slow is not slow2:  # prevent {1 -> 2 -> 1}
                slow = slow.next
                slow2 = slow2.next
            return slow
        return None

    def merge_even_odd(self, head):
        """0 -> 1 -> 2 -> 3 -> 4 to
           0 ------> 2
           c    s    n
           0    1-------> 3 ...
        Time: O(n)
        Space: O(1)
        Corner: 0 -> 1 -> 2
                e    o    ne
        """
        if not head or not head.next or not head.next.next:
            return head

        skip_even = False
        odd_head = head.next
        curr, skip, next = head, head.next, head.next.next
        while next:
            curr.next = next  # skip

            curr = skip  # relabel
            skip = next
            next = next.next

            skip_even ^= True
            curr.next = None  # if skip even, this would be the end of odds

        if skip_even:
            skip.next = odd_head
        else:
            curr.next = odd_head

        return head


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
        Space: O(h)     2   3
        """
        if not root:
            return

        print root.val
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder_recursive(self, root):
        """In order traversal using recursive
        Time: O(n)
        Space: O(h)
        """
        if not root:
            return

        self.inorder(root.left)
        print root.val
        self.inorder(root.right)

    def postorder_recursive(self, root):
        """Post order traversal using recursive
        Time: O(n)       3
        Space: O(h)    1   2
        """
        if not root:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print root.val

    def preorder(self, root):
        """Go deep left and pop stack, if stack is empty than we are done
        Time: O(n)
        Space: O(h)  -> stack is efficient even the complexity is the same
        """
        stack = list()
        curr = root
        done = False
        while not done:
            if curr:
                print curr.val
                stack.append(curr)
                curr = curr.left  # go deep left
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
            # going down
            if not prev or prev.left is curr or prev.right is curr:
                if curr.left:
                    next = curr.left
                else:
                    print curr.val
                    next = curr.right if curr.right else curr.parent
            # going up
            else:
                if prev is curr.left:  # came from left (like pop)
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

        in_stack.append(root)
        while in_stack:
            temp = in_stack.pop()
            if temp:
                if temp.left:
                    in_stack.append(temp.left)
                if temp.right:
                    in_stack.append(temp.right)
            out_stack.append(temp)

        while out_stack:
            temp = out_stack.pop()
            print temp.val

    def common_ancestor(self, r, p, q):
        """Find the first root split two nodes in left and right
        Time: O(n^2)
        Space: O(h)
        """
        def cover(root, node):  # if the tree contain the node
            if not root:
                return False
            if root is node:
                return True
            return cover(root.left, node) or cover(root.right, node)

        if cover(r.left, p) and cover(r.left, q):
            return self.common_ancestor(r.left, p, q)
        if cover(r.right, p) and cover(r.right, q):
            return self.common_ancestor(r.right, p, q)
        return r

    # Match trees
    def contain_tree(self, t1, t2):
        """Test if tree 2 (n) is in tree 1 (m)
        Time: O(mn)
        Space: O(1)
        """
        # match tree given root
        def match_tree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return match_tree(t1.left, t2.left) and \
                match_tree(t1.right, t2.right)

        # try to match on many subtree of t1
        def subtree(t1, t2):
            if match_tree(t1, t2):
                return True
            else:
                return subtree(t1.left, t2) or subtree(t1.right, t2)

        if not t2:
            return True
        else:
            return subtree(t1, t2)

    # Valid binary search tree
    def is_valid_bst1(self, root):
        """Check each root is vaild or not
        Time: O(n)
        Space: O(h) for recursives
        """
        def is_valid_bst_recursive(root, lower, upper):
            if not root:
                return True
            elif root.val <= lower or root.val >= upper:
                return False
            return is_valid_bst_recursive(root.left, lower, root.val)\
                and is_valid_bst_recursive(root.right, root.val, upper)

        MAX_VALUE = float('inf')
        MIN_VALUE = float('-inf')

        return is_valid_bst_recursive(root, MIN_VALUE, MAX_VALUE)

    def is_valid_bst2(self, root):
        """Perform Morris traversal and check if all current > previous node
        Morris traversal: link the last left subtree node's right to the root
        Time: O(n)
        Space: O(1)
        """
        MIN_VALUE = float('-inf')
        if not root:
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
                else:  # set end of left tree to the root
                    pred.right = curr
                    curr = curr.left
            else:
                if last_value >= curr.val:
                    ret = False
                last_value = curr.val
                curr = curr.right
        return ret

    def buildTree_preorder_inorder(self, preorder, inorder):
        """Recursively build tree         1
        preorder = [1 2 3 4 5]         2     4
        inorder = [3 2 1 4 5]       3           5
        Time: O(n log n) average
        Space: O(log n)
        """
        if not preorder:
            return None

        root_val = preorder[0]
        left_count = inorder.index(root_val)  # elements in left tree

        left_inorder = inorder[:left_count]
        left_preorder = preorder[1:1+left_count]  # 0: root

        right_inorder = inorder[1+left_count:]
        right_preorder = preorder[1+left_count:]

        root = TreeNode(root_val)
        root.left = self.buildTree_preorder_inorder(
            left_preorder, left_inorder)
        root.right = self.buildTree_preorder_inorder(
            right_preorder, right_inorder)
        return root

    def buildTree_inorder_postorder(self, inorder, postorder):
        """Recuresively build
        1. Find root
        2. Construct left and right
        Time: O(n log n) in average
        Space: O(log n) in average
        """
        if not postorder:
            return None

        root_val = postorder[-1]  # postorder root in the end
        left_count = inorder.index(root_val)

        left_inorder = inorder[:left_count]
        left_postorder = postorder[:left_count]

        right_inorder = inorder[1+left_count:]
        right_postorder = postorder[left_count:-1]  # not include index[-1]

        root = TreeNode(root_val)
        root.left = self.buildTree_inorder_postorder(
            left_inorder, left_postorder)
        root.right = self.buildTree_inorder_postorder(
            right_inorder, right_postorder)
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
                found |= preorder(root.left, sum-root.left.val)
            if root.right:
                found |= preorder(root.right, sum-root.right.val)
            return found

        if not root:
            return False
        return preorder(root, sum-root.val)

    def pathSum(self, root, sum):
        """Find all paths from root to leaves had path sum equal to sum
        Time: O(n)
        Space: O(n)
        Style: Using a CONTAINER
        """
        def path_finder(root, sum, path, paths):
            if not root.left and not root.right and sum == 0:  # leaves
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
        """Record max path (not only root to leaves) so far
        Compare 1. left 2. right 3. left + root + right 4. level
        Time: O(n)
        Space: O(n)
        Style: Using INSTANCE VARIABLE
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
            return level_max  # this is a vaild node to leaves path

        self.max_value = float('-inf')
        self.maxPathSumRec(root)
        return self.max_value

    def maxDepth(self, root):
        """Traverse a tree and record the max depth in instance variable
        Time: O(n)
        Space: O(n)
        """
        def max_depth(root, depth):
            if not root.left and root.right:
                self.max_depth = max(self.max_depth, depth)
            if root.left:
                max_depth(root.left, depth+1)
            if root.right:
                max_depth(root.right, depth+1)

        if not root:
            return 0

        self.max_depth = float('-inf')
        max_depth(root, 1)  # Leetcode define root has 1 depth
        return self.max_depth

    def minDepth(self, root):
        """Traverse a tree and record the min depth in instance variable
        Time: O(n)
        Space: O(n)
        """
        def min_depth(root, depth):
            if not root.left and not root.right:
                self.min_depth = min(self.min_depth, depth)
            if root.left:
                min_depth(root.left, depth+1)
            if root.right:
                min_depth(root.right, depth+1)

        if not root:
            return 0

        self.min_depth = float('inf')
        min_depth(root, 1)
        return self.min_depth

    def get_height(self, root):
        """Python has limit stack for local function
        Therefore, define a member function to get height
            0  -> depth = 0
        1      -> height = 0
        """
        if not root:
            return -1

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        # definition of unbalance only true if both sides are balance
        if left_height == self.UNBALANCE or \
           right_height == self.UNBALANCE or \
           abs(left_height - right_height) > 1:  # definition
            return self.UNBALANCE
        return 1 + max(left_height, right_height)

    def isBalanced(self, root):
        """Compare HEIGHT of left and right trees of a root
        Time: O(n)
        Space: O(n)
        """
        if not root:
            return True
        self.UNBALANCE = -2

        return self.get_height(root) != self.UNBALANCE

    def isBalanced2(self, root):
        """If a tree is blance, abs(max_height-min_height) <= 1
        Time: O(n)
        Space: O(n)
        """
        return abs(self.maxDepth(root)-self.minDepth(root)) <= 1

    def isSymmetric(self, root):
        """Recursive(left, right) and (right, left)
        Time: O(n)
        Space: O(n)
        """
        def is_symmetric(left, right):
            #Just a node comparison, but have careful order
            if not left and not right:
                return True
            if not left or not right:  # put or after and, avoid both None
                return False
            if left.val != right.val:
                return False
            return is_symmetric(left.left, right.right) and \
                is_symmetric(left.right, right.left)

        if not root:
            return True
        return is_symmetric(root.left, root.right)

    def sortedArrayToBST(self, num):
        """Set median as root, recursive for left and right
        Time: O(log n)
        Space: O(n)
        """
        if not num:
            return None
        if len(num) == 1:
            return TreeNode(num[0])

        middle = len(num) / 2
        root = TreeNode(num[middle])
        root.left = self.sortedArrayToBST(num[:middle])
        root.right = self.sortedArrayToBST(num[middle+1:])
        return root

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
            if left_tail:  # split the left part
                left_tail.next = None

            # deal with right and median
            right = median.next
            median.next = None

            return (left, median, right)

        if not head:
            return None

        left, median, right = split_linked_list(head)
        root = TreeNode(median.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root

    def find_tree_sum(self, root, target, numbers=[], depth=0):
        """Traverse from different nodes, ask if above have met the target
        Time: O(n log n)
        Space: O(n log n)
        """
        def print_path(numbers, start, end):  # print from root
            for number in numbers[start:end+1]:
                print number,
            print

        if not root:
            return
        numbers.append(root.val)

        # figure out if sum above this depth equal to target
        residual = target
        for i, number in enumerate(reversed(numbers)):  # from root
            residual -= number
            if residual == 0:
                print_path(numbers, depth-i, depth)

        # recursive find left and right
        self.find_tree_sum(root.left, target, list(numbers), depth+1)
        self.find_tree_sum(root.right, target, list(numbers), depth+1)


class Array:
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

            if rank == k - 1:  # kth small in k-1 position
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
        return self.find_kth_small(numbers, 1 + len(numbers)/2)  # 1th, 2nd,...

    def findMedianSortedArrays(self, A, B):
        # Using recursive to find the kth element
        # Time: O(log(m + n)), m = len(A), n = len(B)
        # Space: O(log(m + n)), recursive
        total = len(A) + len(B)
        if (total % 2) != 0:
            return self.findKthFromTwo(A, B, total/2 + 1)
        else:
            return .5 * (self.findKthFromTwo(A, B, total/2) +
                         self.findKthFromTwo(A, B, total/2 + 1))

    def findKthFromTwo(self, A, B, k):
        if k > len(A) + len(B):
            return None

        # assume |A| > |B|
        if len(A) < len(B):
            return self.findKthFromTwo(B, A, k)  # know which one we run out
        if not B:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        pb = min(k / 2, len(B))
        pa = k - pb
        if A[pa - 1] < B[pb - 1]:
            return self.findKthFromTwo(A[pa:], B, k - pa)
        else:
            return self.findKthFromTwo(A, B[pb:], k - pb)

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

        while equalto:  # balance the number, smaller always >= larger
            need = smaller if len(greater) >= len(smaller) else greater
            need.append(equalto.pop())

        for i, number in enumerate(numbers):
            numbers[i] = greater[i/2] if i % 2 != 0 else smaller[i/2]

        # final check:
        for i, number in enumerate(numbers):
            if i % 2 == 1 and i < len(numbers) - 1:
                if number <= numbers[i - 1] or \
                   number <= numbers[i + 1]:
                    return None
        return numbers

    def rearrange_wrong(self, numbers):
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
        Space: O(k)
        """
        hist = dict()
        for x in A:
            hist[x] = hist.get(x, 0) + 1

        keys = hist.keys()
        values = hist.values()
        return keys[values.index(max(values))]

    def find_target_or_less(self, numbers, target, candidate=None):
        """Find a target in a sorted list using binary search with candidate
        Time: O(log n)
        Space: O(1)
        * modified version of find_target, find_k_or_less
        """
        if not numbers:
            return None
        if len(numbers) == 1:
            return numbers[0] if numbers[0] <= target else candidate

        # binary search
        middle = len(numbers) / 2
        median = numbers[middle]
        if median == target:
            return median
        if median < target:
            return self.find_target_or_less(
                numbers[middle+1:], target, median)
        if median > target:
            return self.find_target_or_less(
                numbers[:middle], target, candidate)

    def find_less_than_target(self, numbers, target, candidate=None):
        """Binary search with conditions
        Time: O(log n)
        Space: O(log n)
        """
        if not numbers:
            return None
        if len(numbers) == 1:  # for stopping recursion
            return numbers[0] if numbers[0] < target else candidate

        middle = len(numbers) / 2
        median = numbers[middle]
        if median >= target:
            return self.find_less_than_target(
                numbers[:middle], target, candidate)
        if median < target:
            return self.find_less_than_target(
                numbers[middle+1:], target, median)

    def find_index_less_than_target(self, numbers, target):
        """Find index using binary search
        Time: O(log n)
        Space: O(1)
        """
        if not numbers:
            return None

        candidate = None
        start, end = 0, len(numbers) - 1
        while start <= end:  # why equal? one number can be handdle
            middle = (start+end) / 2
            median = numbers[middle]

            if median >= target:
                end = middle - 1
            else:
                candidate = middle
                start = middle + 1

        return candidate

    def find_index_larger_than_target(self, numbers, target):
        """Binary search with a candidate variable
        Time: O(log n)
        Space: O(1)
        """
        if not numbers:
            return None

        candidate = None
        start, end = 0, len(numbers) - 1
        while start <= end:
            middle = (start+end) / 2
            median = numbers[middle]

            if median <= target:
                start = middle + 1
            else:
                candidate = middle
                end = middle - 1

        return candidate

    def find_index_target_in_rotated_sorted_array(self, numbers, target):
        """Binary search with complicated conditions
        1 2 3   4   5 6 7  # order in the front
        5 6 7   1   2 3 4  # order in the end
        Time: O(log n)
        Space: O(1)
        """
        if not numbers:
            return None

        start, end = 0, len(numbers) - 1
        while start <= end:
            middle = (start + end) / 2
            if numbers[middle] == target:
                return middle

            if numbers[middle] >= numbers[start]:  # order in the front
                if numbers[start] <= target and target < numbers[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:  # order in the end
                if numbers[middle] < target and target <= numbers[end]:
                    start = middle + 1
                else:
                    end = middle - 1
        return None

    def find_ai_equal_i(numbers):
        """BS A[i] - i: Assume A[i] is distinguish to others and A is sorted
        Time: O(log n)
        Space: O(1)
        Corner: empty array
        """
        if not numbers:
            return None

        start, end = 0, len(numbers)
        while start <= end:
            middle = (start+end) / 2
            median = numbers[middle]
            if median == middle:
                return middle
            if median < middle:
                start = middle + 1
            else:
                end = middle - 1
        return None

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

        start, end = 0, len(num) - 1
        while start < end:
            num = sorted_num[start][1] + sorted_num[end][1]
            if num == target:
                break
            if num > target:
                end -= 1
            else:
                start += 1

        # compute original index
        small, large = sorted_num[start][0]+1, sorted_num[end][0]+1
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

            start, end = i + 1, len(num) - 1
            while start < end:
                # check duplicates
                if start > i + 1 and num[start] == num[start - 1]:
                    start += 1
                    continue

                if end < len(num) - 1 and num[end] == num[end + 1]:
                    end -= 1
                    continue

                b, c = num[start], num[end]
                if a + b + c == 0:
                    ans.append([a, b, c])
                    start += 1
                    end -= 1
                elif a + b + c < 0:
                    start += 1
                else:
                    end -= 1
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
                    # want all none duplicated combinations in [b, c]
                    all_pairs = [(a, comb[0], comb[1])for comb in combinations(
                        set(num[b_index:c_index+1]), 2)]  # set prevents dups
                    ans += all_pairs  # += concatinate lists to one list
                    break
                else:
                    c_index -= 1
        return ans

    def get_products(self, numbers):
        """Find products of numbers using comulative products
        products[0] =     3 * 4 * 5
        products[1] = 1     * 4 * 5
        products[2] = 1 * 3     * 5

        Time: O(n)
        Space: O(n)
        """
        if not numbers or len(numbers) == 1:  # ask for len == 1
            return None

        products_before = [0] * len(numbers)
        for i, number in enumerate(numbers):
            products_before[i] = number*products_before[i-1] \
                if i > 0 else number

        products_after = [0] * len(numbers)
        for i, number in enumerate(reversed(numbers)):
            products_after[-1-i] = numbers*products_after[-i] \
                if i > 0 else number

        products = [0] * len(numbers)
        for i, (product_before, product_after) in enumerate(
                zip(products_before, products_after)):
            if i == 0:
                products[i] = products_after[1]
            elif i == len(products_before) - 1:
                products[i] = products_before[-2]
            else:
                products[i] = products_before[i-1] * products_after[i+1]
        return products

    def merge_sort(self, lists):
        """Using a min heap built from the lists
        Time: O(n log k), k is the heap size
        Space: O(k)
        """
        from heapq import heappush
        from heapq import heappop

        min_heap = list()
        # initialize min heap with the first element of each list
        for i, x in enumerate(lists):
            heappush(min_heap, (x.pop(0), i))

        sorted_list = list()
        while min_heap:
            value, list_index = heappop(min_heap)
            sorted_list.append(value)
            if lists[list_index]:
                heappush(min_heap,
                         (lists[list_index].pop(0), list_index))

        return sorted_list

    # Common elements
    def common_elements1(self, A, B):
        """Common elements of two array. Based on A binary search B
        Time: O(m log n) for m << n.
        Space: O(1)
        """
        def has_key_bs(self, items, key):
            if not items:
                return False

            middle = len(items) / 2
            if items[middle] == key:
                ret = True
            elif items[middle] < key:
                ret = self.has_key_bs(items[middle+1:], key)
            else:
                ret = self.has_key_bs(items[:middle], key)
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
        from heapq import heapify
        from heapq import heappushpop
        from heapq import heappop

        if not A:
            return None

        # recruiting
        min_heap = A[:min(len(A), k)]
        heapify(min_heap)

        # rank
        for i in range(len(A)):
            A[i] = heappushpop(min_heap, A[i+k]) \
                if i+k < len(A) else heappop(min_heap)

    def snakes(self, board, target):
        """Recursively search 4 directions
        Time: O(n^2)
        Space: O(|target|)
        """
        def search(board, target, visited, i, j):
            def is_valid(board, target, visited, i, j):
                if i < 0 or i >= len(board) or \
                   j < 0 or j >= len(board[0]) or \
                   (i, j) in visited:
                    return False
                return True

            if target[0] != board[i][j]:
                return 0
            if len(target) == 1:  # only one charater left and match
                return 1

            visited.append((i, j))  # otherwise, need search the next
            found = 0
            if is_valid(board, target[1:], visited, i, j+1):
                found += search(board, target[1:], visited, i, j+1)
            if is_valid(board, target[1:], visited, i-1, j):
                found += search(board, target[1:], visited, i-1, j)
            if is_valid(board, target[1:], visited, i+1, j):
                found += search(board, target[1:], visited, i+1, j)
            if is_valid(board, target[1:], visited, i, j-1):
                found += search(board, target[1:], visited, i, j-1)
            return found

        found = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = list()  # each time needs a new copy
                found += search(board, target, visited, i, j)
        return found

    def minimum_cover_set(self, lowers, uppers):
        """Find a minimum set of points cover given interval
        Time: O(n log n)
        Space: O(1)
        """
        MIN = float('-inf')

        # sort based on the upper intervals
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

    def print_power_set1(self, iterable):
        """Get the power set using bit representation
        Time: O(2^n)
        Space: O(1)
        """
        from math import log

        for i in range(1 << len(iterable)):
            x = i  # bits representation of combination
            while x:
                lsb = x & ~(x - 1)  # as reprentation of integer
                target = int(log(lsb, 2))  # pick lsb index
                print iterable[target],
                x &= x - 1  # remove lsb
            print

    def print_power_set2(self, iterable):
        """Get the power set using bit representation
        Time: O(2^n)
        Space: O(1)
        """
        from itertools import combinations

        for i in range(len(iterable) + 1):  # include empty set
            print [comb for comb in combinations(iterable, i)]

    def generate_random_not_from_set(self, n, m, black):
        """Generate N random numbers from 0 to M not in black list
        Time: O(n)
        Space: O(1)
        """
        from random import randint

        white = [x for x in range(m) if x not in black]
        if white:
            while n:
                i = randint(0, len(white) - 1)
                yield white[i]
                n -= 1

    def maxPoints(self, points):
        """Compute all possible slopes for points
        Time: O(n^2)
        Space: O(k)
        Corner: 0 and 1 point, duplicated points
        """
        if len(points) < 2:
            return len(points) or 0  # no line

        max_points = 0
        for start in points:
            lines = dict()
            duplicates = 1
            for end in points:
                if start is end:
                    continue

                if start.x == end.x and start.y == end.y:
                    duplicates += 1  # no slope
                else:
                    if start.x == end.x:  # vertical
                        lines['vertical'] = lines.get('vertical', 0) + 1
                    elif start.y == end.y:
                        lines['horizontal'] = lines.get('horizontal', 0) + 1
                    else:
                        slope = 1.0*(end.y-start.y)/(end.x-start.x)
                        lines[slope] = lines.get(slope, 0) + 1

            if lines:
                max_points = max(max_points, max(lines.values())+duplicates)
            else:
                max_points = max(max_points, duplicates)
        return max_points

    def next_int(self, number):
        # reversed to processing order
        number = list(str(number))[::-1]  # each element is a string

        # find the positions for swap
        for i, n in enumerate(number):
            if i > 0 and number[i] < number[i - 1]:
                break
        swap_front = i

        for i, n in enumerate(number):
            if n > number[swap_front]:
                break
        if n <= number[swap_front]:
            return None
        swap_end = i

        # swap the positions
        number[swap_front], number[swap_end] = \
            number[swap_end], number[swap_front]

        # reorder the rest
        number[:swap_front-1] = sorted(number[:swap_front-1], reverse=True)

        # formating
        return ''.join(number[::-1])


class DynamicProgramming:
    def knapsack1(self, items, capacity):
        """Solve pseudo-polynomial by DP
        Time: O(nw), n is number of items, w is the sum of the weights
        Space: O(w)
        """
        #sum(weight for i, (value, weight) in enumerate(items))
        values = [0] * (capacity + 1)  # make indices clear
        for (value, weight) in items:
            curr = capacity
            while curr - weight >= 0:  # if you have choices
                values[curr] = max(values[curr],  # not take gain capacity
                                   values[curr - weight] + value)  # take
                curr -= 1  # eumerate all possible given this item
        return values[capacity]

    def knapsack2(self, items, capacity):
        # Return the value of the most valuable subsequence of the first i
        # elements in items whose weights sum to no more than j.
        #@memoized
        def best_value(i, j, items):
            if i == 0:
                return 0
            value, weight = items[i - 1]
            if weight > j:
                return best_value(i - 1, j, items)
            else:
                return max(best_value(i - 1, j, items),
                           best_value(i - 1, j - weight, items) + value)

        j = capacity
        result = list()
        for i in range(len(items), 0, -1):
            if best_value(i, j, items) != best_value(i - 1, j, items):
                result.append(items[i - 1])
                j -= items[i - 1][1]
        result.reverse()
        return best_value(len(items), capacity, items)

    def longestConsecutive(self, num):
        """Hash table keep the longest length.
        If the key is a lower interval, than the value is the upper.
        If the key is an upper interval, than the value is the lower.
        (two directions counts)
        Time: O(n)
        Space: O(k)
        Corner: len(num) == 0
        """
        if not num:
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
        if not grid or not grid[0]:
            return None

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

    # 8 Queens
    BOARD_SIZE = 8
    board = [0] * BOARD_SIZE

    def check_queens(self, row):
        for x in range(row):
            diff = abs(self.board[row] - self.board[x])
            if diff == 0 or diff == row - x:
                return False
        return True

    def put_queen(self, row):
        if row == 8:
            #print self.board
            return 1

        total = 0
        for x in range(8):
            self.board[row] = x  # generate 8 branchs when row=0
            if self.check_queens(row):
                total += self.put_queen(row + 1)
        return total

    def generateParenthesis(self, n):
        if n == 0:
            return []
        if n == 1:
            return ['()']

        ans = list()
        parenthesis = self.generateParenthesis(n - 1)

        # for each (), insert another () in it
        for each in parenthesis:
            each_list = list(each)  # inside in each
            for i, one_side in enumerate(each_list):
                if i < len(each_list) and \
                   one_side == '(' and each_list[i+1] == ')':
                    copy = list(each_list)
                    copy.insert(i+1, '()')
                    ans.append(''.join(copy))

        # insert a () aside the current solution
        ans.append('()'*n)
        ans.append('('+'()'*(n-1)+')')
        return ans


class Test(unittest.TestCase):
    def setUp(self):
        board = [['S', 'N', 'B', 'S', 'N'],
                 ['B', 'A', 'K', 'E', 'A'],
                 ['B', 'K', 'B', 'B', 'K'],
                 ['S', 'E', 'B', 'S', 'E']]
        self.args = (board, 'SNAKES')

    def tearDown(self):
        self.args = None

    def test_snake(self):
        expected = 3
        result = Array().snakes(*self.args)
        self.assertEqual(expected, result)


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


if __name__ == "__main__":
    # Unit Test
    # suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    print Recursive().generateParenthesis(3)

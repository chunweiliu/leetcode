class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        return self.evaluator(num, target, 0, 0, 0, '', [])

    def evaluator(self, num, target, position=0, evaluation=0, multed=0,
                  attemp='', ans=[]):

        if position == len(num) and evaluation == target:
            ans.append(attemp)
            return

        for i in range(position, len(num)):
            if i != position and num[position] == '0':
                # Get rid of 00.
                break

            current_num = int(num[position:i+1])
            if position == 0:
                self.evaluator(num, target, i + 1, current_num, current_num,
                               attemp + str(current_num), ans)
            else:
                self.evaluator(num, target, i + 1,
                               evaluation + current_num, current_num,
                               attemp + '+' + str(current_num), ans)

                self.evaluator(num, target, i + 1,
                               evaluation - current_num, -current_num,
                               attemp + '-' + str(current_num), ans)
                self.evaluator(num, target, i + 1,
                               evaluation - multed + multed * current_num,
                               multed * current_num,
                               attemp + '*' + str(current_num), ans)
        return ans

    def all_numbers(digits, attemp=[], results=[]):
        """DFS print all combinations:
                     123
                 /    |    \
                1    12   123
              /  \     \
             2   23     3
            /
           3
        """
        if not digits:
            results.append(attemp)
            
        for string_length in range(1, 1 + len(digits)):
            num = digits[:string_length]        
            all_numbers(digits[string_length:], attemp + [num], results)

        return results

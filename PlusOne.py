class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
    	# Preprocessing digits
        digits.reverse()
        digits.append(0)
        ndigits = len(digits)

        carries = [0] * ndigits
        carries[0] = 1

        # Calculate
        answer = [0] * ndigits
        for x in range(ndigits-1):
        	if digits[x] + carries[x] > 9:
        		answer[x] = digits[x] + carries[x] - 10
        		carries[x+1] += 1
        	else:
        		answer[x] = digits[x] + carries[x]

        # Bonudary condition check
        if carries[-1] == 0:
        	answer.pop(-1)
        if carries[-1] == 1:
        	answer[-1] += 1

        answer.reverse()
        return answer

if __name__ == '__main__':
	digits = [9, 9, 9]
	print Solution().plusOne(digits)
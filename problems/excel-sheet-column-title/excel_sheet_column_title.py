class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str

        Example:

        1 -> A
	    2 -> B
	    3 -> C
	    ...
	    26 -> Z
	    27 -> AA
	    28 -> AB 

	    Note: 26 base conversion
        """
        return self.convert(n, 26)

    def convert(self, n, base):
    	result = ''
    	while n:
			# Map each digit from 0 to base - 1.
	    	n -= 1  	    	
	    	
    		result += chr(n % base + ord('A'))
    		n /= base
    	return result[::-1]
        
if __name__ == "__main__":
	print Solution().convertToTitle(28)

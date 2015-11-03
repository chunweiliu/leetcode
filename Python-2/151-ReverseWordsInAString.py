class Solution(object):
    def reverseWords(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words = sentence.split(' ')
        words = [word for word in words if word and not word.isspace()]
        return ' '.join(words[::-1])

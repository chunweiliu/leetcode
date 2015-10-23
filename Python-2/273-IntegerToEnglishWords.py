class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 2 ^ 31 - 1 = 2,147,483,647
        less_than_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five',
                        'Six', 'Seven', 'Eight', 'Night', 'Ten',
                        'Eleven', 'Twelve', 'Thirteen', 'Fouteen', 'Fifteen',
                        'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Tewnty', 'Thirty', 'Forty', 'Fifty',
                'Sixty', 'Seventy', 'Eighty', 'Nighty']

        def num_to_words(num):
            if num == 0:
                return 'Zero'

            words = ''
            for unit in ['', 'Thousand', 'Million', 'Billion']:
                n = num % 1000
                if n > 0:
                    words = mapping(n) + unit + ' ' + words
                num /= 1000

            return words

        def mapping(num):
            # 0 - 999
            if num == 0:
                return ''
            if num < 20:
                return less_than_20[num] + ' '
            if num < 100:
                return tens[num / 10] + ' ' + mapping(num % 10)
            return less_than_20[num / 100] + ' Hundred ' + mapping(num % 100)

        return num_to_words(num)

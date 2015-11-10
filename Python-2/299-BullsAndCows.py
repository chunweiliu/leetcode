from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_hist = Counter(secret)
        guess_hist = Counter(guess)

        bulls = 0
        for s, g in zip(secret, guess):
            match = s == g
            secret_hist[s] -= match
            guess_hist[g] -= match
            bulls += match

        cows = 0
        for key, value in secret_hist.iteritems():
            cows += min(value, guess_hist[key])

        return str(bulls) + 'A' + str(cows) + 'B'

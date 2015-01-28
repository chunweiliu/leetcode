class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        # sorted so every anagrams are the same
        # O(mlog(m)), m is the mean string length
        # build a hash table for reference
        str_idx = dict()
        for x in range(len(strs)):
            key = ''.join(sorted(strs[x]))
            if key in str_idx:
                str_idx[key].append(x)
            else:
                str_idx[key] = [x]

        # find duplicated elements' index
        dups = []
        for k, v in str_idx.iteritems():
            if len(v) > 1:
                for x in v:
                    dups.append(strs[x])
        return dups

if __name__ == "__main__":
    strs = ['army', 'mary', 'abc', 'cba']
    print Solution().anagrams(strs)

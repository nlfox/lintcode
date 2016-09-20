class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        d = [False for i in xrange(len(s) + 1)]
        wl = list(set([len(i[0]) for i in dict.items()]))
        if 0 in wl:
            wl.remove(0)
        d[0] = True
        for i in xrange(1, len(s) + 1):
            if True in [(s[(i - j):i] in dict) and d[i - j] for j in wl]:
                d[i] = True
            else:
                d[i] = False
        return d[-1]

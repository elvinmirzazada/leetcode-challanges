class Solution:
    def appealSum(self, s):
        last = {}
        res = 0
        for i,c in enumerate(s):
            last[c] = i + 1
            res += sum(last.values())

        return res
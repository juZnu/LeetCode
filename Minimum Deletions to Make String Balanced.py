class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        res = 0
        for i in s:
            if i == 'b':
                b_count += 1
            else:
                res = min(res+1,b_count)
        return res
                
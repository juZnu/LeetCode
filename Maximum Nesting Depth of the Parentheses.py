class Solution:
    def maxDepth(self, s: str) -> int:
        openb =0
        result = 0
        for ele in s:
            if ele =="(":
                openb += 1
                result = max(result,openb)
            elif ele == ")":openb -= 1
        return result
        
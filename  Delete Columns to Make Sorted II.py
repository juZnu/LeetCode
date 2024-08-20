class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        str_carry = ['' for _ in range(len(strs))]

        for j in range(len(strs[0])):
            copy = str_carry.copy()
            sucess = True
            copy[0] += strs[0][j]
            for i in range(1,len(strs)):
                copy[i] += strs[i][j]
                if copy[i] < copy[i-1]:
                    sucess = False
                    break
            if sucess:
                str_carry = copy

        return len(strs[0]) - len(str_carry[0])
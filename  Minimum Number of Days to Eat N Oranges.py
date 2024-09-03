class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache()
        def path(i):
            if i <=1:return i
            return 1 + min(i%2 + path(i//2) , i%3 + path(i//3))   
        return path(n)
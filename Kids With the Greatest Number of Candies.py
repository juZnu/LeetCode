class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)
        return [ candy+extraCandies>=maxNum for candy in candies]

        
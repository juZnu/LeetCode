class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0

        while numBottles >= numExchange:
            div,mod = divmod(numBottles,numExchange)
            res += (numBottles - mod)
            numBottles = mod + div 
            
        res += numBottles

        return res
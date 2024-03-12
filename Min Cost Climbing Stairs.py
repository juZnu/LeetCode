class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-1,-1,-1):
            cost[i] += min(cost[i+1] if i+1 < len(cost) else 0,cost[i+2] if i+2 < len(cost) else 0)
        return min(cost[0],cost[1])
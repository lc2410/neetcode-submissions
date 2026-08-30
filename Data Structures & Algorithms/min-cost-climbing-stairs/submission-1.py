class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ways = [0] * (len(cost)+1)
        
        for i in range(2,len(cost)+1):
            ways[i] = min(ways[i-1]+cost[i-1], ways[i-2]+cost[i-2])
            
        return ways[len(cost)]
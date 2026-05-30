class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIndex = 0
        sellIndex = len(prices)-1
        maxProfit = 0
        while buyIndex < len(prices)-1:
            if prices[buyIndex] < prices[sellIndex]:
                maxProfit = max(maxProfit, prices[sellIndex]-prices[buyIndex])
            sellIndex -= 1
            if sellIndex == buyIndex:
                sellIndex = len(prices)-1
                buyIndex += 1

        
        return maxProfit
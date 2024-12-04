class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy=prices[0]
        profit=0

        for i in range (1,len(prices)):
            sell=prices[i]-buy
            profit=max(profit,sell)
            buy=min(buy,prices[i])

        return profit

        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of the max profit
        # Loop through i, j = i + 1 and calculate all possible buy and sell combos 
        # and return the highest value

        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range (i + 1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j] - prices[i])
        
        # return maxProfit

        # Keep track of the max profit earned
        # have 2 pointers i, j = i + 1. if i > j, advance j. Else update max profit to be
        # the max of itself versus prices[j] - prices[i]

        maxProfit = 0
        i = 0
        j = i + 1
        while i < len(prices) and j < len(prices):
            if prices[j] <= prices[i]:
                j += 1
            else:
                maxProfit = max(maxProfit, prices[j] - prices[i])
                j += 1
            
            if j >= len(prices):
                i += 1
                j = i + 1
        
        return maxProfit

            

        
        
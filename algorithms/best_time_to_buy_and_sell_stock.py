from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        maxprofit, minstock = float('-inf'), prices[0]
        for p in prices:
            maxprofit = max(maxprofit, p - minstock)
            minstock = min(minstock, p)
        return maxprofit

s = Solution().maxProfit(prices=[7,1,5,3,6,4])
print(s)

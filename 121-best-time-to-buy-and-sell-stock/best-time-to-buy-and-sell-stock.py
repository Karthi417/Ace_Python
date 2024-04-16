class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice= float(inf)
        maxprice=0
        for i in range(len(prices)):
            minprice=min(minprice,prices[i])
            maxprice=max(maxprice,prices[i]-minprice)
        return maxprice
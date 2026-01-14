class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy: best choice at each step. Two pointers
        l, r = 0,1
        max_profit = 0

        while r!= len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                max_profit = max(max_profit, prof)
            else:
                l = r
            r+=1
        return max_profit
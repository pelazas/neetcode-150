class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS
        # if amount == 0:
        #     return 0
        # # steps, curr_amount
        # queue = deque([(0,0)])
        # seen = set()

        # while queue:
        #     step, curr_count = queue.popleft()
            
        #     for coin in coins:
        #         next_amount = curr_count +coin

        #         if next_amount == amount:
        #             return step +1
                
        #         if next_amount < amount and next_amount not in seen:
        #             queue.append((step+1, next_amount))
        #             seen.add(next_amount)
        # return -1

        # DP
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
         
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

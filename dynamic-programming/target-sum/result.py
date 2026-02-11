class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # TIME COMPLEXITY: O(2^n)
        # res = []
        # def dfs(to_target, index, path):
        #     if index == len(nums):
        #         if to_target == 0:
        #             res.append(path)
        #         return
            
        #     dfs(to_target + nums[index], index+1, path+f"+{nums[index]}")
        #     dfs(to_target - nums[index], index+1, path+f"-{nums[index]}")

        # dfs(target,0,"")
        # return len(res)

        # TIME COMPLEXITY: O(N*S)
        dp = [defaultdict(int) for _ in range(len(nums)+1)]

        dp[0][0] = 1

        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                dp[i+1][curr_sum + nums[i]] +=count
                dp[i+1][curr_sum - nums[i]] +=count

        return dp[len(nums)][target]


        
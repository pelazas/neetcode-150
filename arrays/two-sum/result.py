class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time complexity of O(n2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        

        #time complexity of O(n)
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [seen[complement],i]

            seen[num] = i
        
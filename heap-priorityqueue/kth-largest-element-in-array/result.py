from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #O(nlogn) solution
        # nums.sort() 
        # return nums[-k]

        #O(n) solution
        nums = [-x for x in nums]
        heapify(nums) #O(n)

        for i in range(k-1):
            heappop(nums)
        return -nums[0]


        


        
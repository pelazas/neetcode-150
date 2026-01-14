class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] > 0:
            return [num ** 2 for num in nums]
        
        m = len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                m = i
                break
        
        negative_nums = [abs(num) for num in nums[:m]] #reversed
        positive_nums = nums[m:]

        output = []
        for i in range(len(nums)):
            if len(negative_nums) == 0:
                output.append(positive_nums.pop(0))
            elif len(positive_nums) == 0:
                output.append(negative_nums.pop(-1))
            elif negative_nums[-1] <= positive_nums[0]:
                output.append(negative_nums.pop(-1))
            elif positive_nums[0] < negative_nums[-1]:
                output.append(positive_nums.pop(0))
        
        return [num ** 2 for num in output]
            

        
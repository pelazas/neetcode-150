class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(stack, starting_index):
            res.append(list(stack)) # CRUCIAL: create a copy of stack

            for i in range(starting_index,len(nums)):
                if i > starting_index and nums[i] == nums[i-1]:
                    continue

                stack.append(nums[i])
                backtrack(stack,i+1)
                stack.pop()
        
        backtrack([], 0)
        return res
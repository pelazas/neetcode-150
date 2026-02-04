class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort() O(nlogn)
        # current_length = 1
        # best_length = 1
        # for i in range(len(nums) -1): O(n)
        #     if nums[i+1] == nums[i]:
        #         continue
        #     if nums[i+1] == nums[i]+1:
        #         current_length +=1
        #     else:
        #         best_length = max(current_length, best_length)
        #         current_length = 1

        # return max(best_length, current_length)

        nums_set = set(nums) #remove duplicates
        best_length = 0

        for n in nums_set:
            if (n-1) not in nums_set:
                current_length = 1
                current_num = n
                while (current_num+1) in nums_set:
                    current_num +=1
                    current_length +=1

                best_length = max(best_length, current_length)

        return best_length
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while r > l:
            op = numbers[l] + numbers[r]
            if op == target:
                return [l+1,r+1]
            if op < target:
                l +=1
            elif op > target:
                r-=1

        return []
            

        
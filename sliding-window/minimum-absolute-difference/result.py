class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort() #O(nlogn)
        min_diff = float('inf')
        result = []
        for i in range(len(arr)-1):
            op = arr[i+1] - arr[i]
            if op < min_diff:
                min_diff = arr[i+1] - arr[i]
                result = []
                result.append([arr[i], arr[i+1]])
            elif op == min_diff:
                result.append([arr[i], arr[i+1]])
        
        return result

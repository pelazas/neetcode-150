class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0
        
        for i in range(1, n - 1):
            if arr[i-1] < arr[i] > arr[i+1]:
                # Expand Left
                l = i
                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                
                # Expand Right
                r = i
                while r < n - 1 and arr[r] > arr[r+1]:
                    r += 1
                
                # Calculate Length
                current_len = r - l + 1
                max_len = max(max_len, current_len)
                
        return max_len
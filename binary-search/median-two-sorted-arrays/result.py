class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(log(n)) -> BINARY SEARCH

        A,B = nums1, nums2

        # make nums1 the smaller array
        if len(A) > len(B):
            A, B = B, A
            
        m, n = len(A), len(B)
        total = m+n
        half = (total + 1) // 2
        low, high = 0, m

        while low <= high:
            #1. find the cut
            # partition_A is the index where we cut A
            partition_A = (low + high) // 2
            
            # partition_B = half - partition_A -> index where we cut B
            #partition_B = (m + n + 1) // 2
            partition_B = half - partition_A

            #2. find the edges
            A_left = A[partition_A-1] if partition_A > 0 else float('-inf')
            A_right = A[partition_A] if (partition_A) < m else float('inf')
            B_left = B[partition_B - 1] if partition_B > 0 else float('-inf')
            B_right = B[partition_B] if (partition_B) < n else float('inf')

            #3. compare edges - correct partition
            if A_left <= B_right and A_right >= B_left:
                if total % 2 == 1: #odd
                    return max(A_left, B_left)
                else: #even
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            if A_left > B_right:
                high = partition_A -1
            elif A_right < B_left:
                low = partition_A +1 



            

        
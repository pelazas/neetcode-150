from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #time complexity: O(nlogn)
        heap: list[tuple[int, list[int]]] = []

        for p in points:
            heappush(heap, (p[0]**2 + p[1]**2,p)) # O(logn)
        
        result = []
        for i in range(k):
            distance, point = heappop(heap)
            result.append(point)
        
        return result
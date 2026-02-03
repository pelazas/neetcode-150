from heapq import heappush, heappop, heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [-x for x in count.values()]
        heapify(max_heap)

        n_of_intervals = 0

        while max_heap:
            temp_list = []
            for i in range(n+1):
                if max_heap:
                    curr_freq = heappop(max_heap)
                    if curr_freq +1 < 0:
                        temp_list.append(curr_freq+1)
                n_of_intervals +=1

                if not max_heap and not temp_list:
                    break

            for freq in temp_list:
                heappush(max_heap, freq)
        return n_of_intervals

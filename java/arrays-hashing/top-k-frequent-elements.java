class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> frequency_map = new HashMap();

        for (int num: nums){
            frequency_map.put(num, frequency_map.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Integer> minHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(frequency_map.get(a),frequency_map.get(b))
        );

        for (int num : frequency_map.keySet()) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        int[] result = new int[k];
        for (int i = 0; i< k; i++){
            result[i] = minHeap.poll();
        }

        return result;
    }
}
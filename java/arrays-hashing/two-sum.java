class Solution {
    public int[] twoSum(int[] nums, int target) {
        // key = target, value = index
        HashMap<Integer,Integer> map = new HashMap();

        for (int i = 0; i<nums.length; i++){
            int complement = target - nums[i];
            if (map.containsKey(nums[i])){
                return new int[]{map.get(nums[i]), i};
            }
            map.put(complement, i);
        }
        return new int[] {};
    }
}
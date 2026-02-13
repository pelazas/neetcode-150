class Solution {
    public int[] searchRange(int[] nums, int target) {

        int left = findBound(nums, target, true);  // Find first index
        int right = findBound(nums, target, false); // Find last index
        
        return new int[]{left, right};
    }

        private int findBound(int[] nums, int target, boolean isFirst) {
            int l = 0;
            int r = nums.length - 1;
            int index = -1;

            while (l <= r) {
                int mid = l + (r - l) / 2;

                if (nums[mid] == target) {
                    index = mid;
                    
                    if (isFirst) {
                        r = mid - 1;
                    } else {
                        l = mid + 1;
                    }
                } else if (nums[mid] < target) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            return index;
        }
}
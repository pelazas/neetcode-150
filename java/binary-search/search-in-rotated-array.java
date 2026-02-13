class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length -1;

        while (r >= l){
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[l] <= nums[mid]) { // left side is sorted
                if (nums[l] <= target && target < nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else { // right side is sorted
                if (nums[mid] < target && target <= nums[r]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
        return -1;
    }
}
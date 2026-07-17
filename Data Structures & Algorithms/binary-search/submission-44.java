class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        while (l < r) {
            int mid = l + ((r - l) / 2);
            int n = nums[mid];
            if (n == target) return mid;
            else if (n < target) l = mid + 1;
            else r = mid;
        }
        return (l < nums.length && nums[l] == target) ? l : -1;
    }
}

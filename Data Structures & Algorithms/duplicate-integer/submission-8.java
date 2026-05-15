class Solution {
    public boolean hasDuplicate(int[] nums) {
        if(nums.length == 0 || nums.length == 1) {
            return false;
        }
        HashSet<Integer> dup = new HashSet<Integer>();
        dup.add(nums[0]);
        for(int i = 1; i < nums.length; i++) {
            if(dup.contains(nums[i])) {
                return true;
            }
            dup.add(nums[i]);
        }
        return false;
    }
}

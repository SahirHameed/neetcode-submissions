class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevNums = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];

            if(prevNums.containsKey(diff)){
                return new int[] {prevNums.get(diff), i};
            }

            prevNums.put(nums[i], i);
        }

        return new int[] {};
    }
}

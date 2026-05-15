class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Design
        // Declare a HashMap where the key stores the
        // complement of the value at nums[i] and the 
        // value is the index

        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int compliment = target - nums[i];
            if(map.containsKey(compliment)){
                return new int[]{map.get(compliment), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}

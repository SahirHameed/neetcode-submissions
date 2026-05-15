class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Use a bucket sort where indices represent element
        // frequency and values are the list of #'s that meet
        // the required frequency
        // Declare a HashMap where the key is a # in nums and
        // the value is the frequency of that #
        // Declare a frequency list to store the list of all
        // #'s based on their frequency
        // Reverse loop through the frequency array and fill
        // a result array with the k most frequent elements

        HashMap<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freqs = new List[nums.length +1];

        for(int i = 0; i < freqs.length; i++) {
            freqs[i] = new ArrayList<>();
        }

        for(int num : nums) {
            count.put(num, count.getOrDefault(num,0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freqs[entry.getValue()].add(entry.getKey());
        }

        // Now we have the a list of frequencies
        int[] res = new int[k];
        int index = 0;
        for(int i = freqs.length - 1; i > 0 && index < k; i--) {
            for(int n : freqs[i]) {
                res[index++] = n;
                // index++;
                if(index == k) {
                    return res;
                }
            }
        }
        return res;

    }
}

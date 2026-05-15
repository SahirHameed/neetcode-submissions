class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // HashMap (Key; freq of a-z, val is array of words)
        // Loop through all strings in array
        // declare an array and loop through it to get the freq
        // of each letter in str
        // if a matching key exists, add to list
        // put the freq and string in array
        // loop through all values in the map and add to list and
        // return it

        HashMap<String, List<String>> groups = new HashMap<>();

        for(String str : strs) {
            int[] freq = new int[26];

            for(int i = 0; i < str.length(); i++) {
                freq[str.charAt(i) - 'a']++;
            }

            String freqKey = Arrays.toString(freq);

            if(!groups.containsKey(freqKey)) {
                groups.put(freqKey, new ArrayList<>());
            }
            groups.get(freqKey).add(str);
        }

         return new ArrayList<>(groups.values());
    }
}

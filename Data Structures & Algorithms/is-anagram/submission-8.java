class Solution {
    public boolean isAnagram(String s, String t) {
        // Pre-conditions
        // s.length == t.length
        // Design
        // Declare an int array of size 26 for a-z
        // Loop through string s (arbitrarily) 
        // Extract the character and convert to an int
        // Increment at s, decrement at t
        // Loop through the t array
        // Return false iff t[0-length] != 0

        if(s.length() != t.length()) {
            return false;
        }

        int[] letters = new int[26];
        
        for(int i = 0; i < s.length(); i ++) {
            letters[s.charAt(i) - 'a']++;
            letters[t.charAt(i) - 'a']--;
        }

        for(int letter : letters) {
            if(letter != 0) {
                return false;
            }
        }
        return true;
    }
}

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of s and t don't match return False
        # brute force solution is to sort the strings by ascii letters and return 
        # if the strings equal each other
        # Optomized
        # Create a frequency list for the 26 letters 
        # Loop through s and keep track of each character
        # Increment the frequency list at s[i] - 'a' and decrement at t[i] - 'a'
        # Loop through the freq list and if any values are not 0, return false, else true

        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for n in freq:
            if n != 0:
                return False
        
        return True
            
        
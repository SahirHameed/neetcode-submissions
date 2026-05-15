class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Naive: Sort the strings and return if s == t
        # Optimal: get the frequency of all letters in s,t in 2 lists and compare
        # the values
        # better: get the frequency of all letters in s,t in one list (inc for s dec for t)

        if len(s) != len(t):
            return False
        
        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for c in freq:
            if c != 0:
                return False
        
        return True
        
        
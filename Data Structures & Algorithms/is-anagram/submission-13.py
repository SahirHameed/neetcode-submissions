class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # constraints: length of s equals length of t
        # brute force: sort s and t and check for equality

        # return sorted(s) == sorted(t)
        # Time: O(mlogm + nlogn), Space: O(1)

        # Optomize: keep track of the frequencies of s and t using a list
        # of size 26 (a-z). Loop once to both increment at a char of s and decrement
        # at char of t. Then loop again to check if all slots of list is 0 to return
        # true, else false

        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for val in freq:
            if val != 0:
                return False
        
        return True

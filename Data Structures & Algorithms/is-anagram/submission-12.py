class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # constraints: length of s equals length of t
        # brute force: sort s and t and check for equality

        return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # constraints: length of s equals length of t
        # brute force: sort s and t and check for equality
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        return sorted_s == sorted_t

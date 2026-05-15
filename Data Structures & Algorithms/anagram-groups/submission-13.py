class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary where the key is the frequency of the string and the
        # values are the list of strings
        # Return a list of the values of the dictionary

        anagrams = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            anagrams[tuple(freq)].append(s)
        return list(anagrams.values())
        
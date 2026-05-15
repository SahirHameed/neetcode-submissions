class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary (K=freq of String,V=Strings that match frequency)
        # Double loop, one for strings, next for characters in the string
        # return a list of values of dictionary
    
        anagrams = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            anagrams[tuple(freq)].append(s)
        
        return list(anagrams.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dict mapping string freq to string
        # Loop through the list of strings
            # Create a freq list of size 26 (a-z)
            # Loop through the characters of each string
        # add dict[freq].append(word)
        #return a list of values from the dict

        anagrams = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] +=1
            anagrams[tuple(freq)].append(s)
        
        return list(anagrams.values())

        
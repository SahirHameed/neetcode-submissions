class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap where the key is a frequency list of the strings in strs
        # and the key is a list of strings that have the frequency
        # Loop through the strings in strs
            # Loop through the chars in each string a create a freq list for those strings
        # If the freq list is in the hashmap append the string to the values
        # Else add in key value pair
        # Return a list of values of the hashmap

        anagrams = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            anagrams[tuple(freq)].append(s)
        return list(anagrams.values())

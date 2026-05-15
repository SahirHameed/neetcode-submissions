class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # prob: group together strings that are anagrams of each other and return
        # in any order

        # soln
        # 1. Get the frequency of each string in the list
        # 2. Use a hashmap to map the frequency together with a list of strings
        # 3. Loop through the values in the hashmap and return a list of all grouped anagrams

        anagrams = defaultdict(list)
        for n in strs:
            freqs = [0] * 26
            for c in n:
                freqs[ord(c) - ord('a')] += 1
            anagrams[tuple(freqs)].append(n)
        return list(anagrams.values())

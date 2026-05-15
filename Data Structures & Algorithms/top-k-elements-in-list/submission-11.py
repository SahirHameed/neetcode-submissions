class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use the bucket sort algorithm where the index represents the frequency of the number
        # and the values are a list of numbers that match the frequency
        # Create a hashmap where the key is a number and the value is its firequency
        # Create a list of size len(nums + 1) 
        # Loop through the hashmap key,value pairs and update list[value].append(key)
        # Loop through the list in reverse and each of the sub lists
        # Append to res list until its length is = to k and return res

        freq = {}
        topK = [[] for i in range(len(nums) + 1)] # indices 1 to len(nums + 1)

        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        for key, value in freq.items():
            topK[value].append(key)
        
        res = []
        for i in range(len(topK) - 1, 0, -1):
            for n in topK[i]:
                if len(res) == k:
                    return res
                res.append(n)
        return res
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force solution:
        # Get the frequency of each value in the list. 
        # Create a hashmap whose key is the freq of each value amd key are those values
        # Return the values whose frequency is k

        count = [[] for i in range(len(nums) + 1)]
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            print(freq[n])
        
        for key, value in freq.items():
            count[value].append(key)
        

        res = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                if len(res) == k:
                    return res
                res.append(n)

        return res


        
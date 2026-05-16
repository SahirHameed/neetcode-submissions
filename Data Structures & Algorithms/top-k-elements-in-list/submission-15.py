class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimized: Use a Bucket Sort 
        # Use a dictionare where the key is the frequency and the values are list of ints that
        # match the frequency
        # Declare a hashmap and a list of lists of size len(nums) + 1
        cnt = [[] for i in range(len(nums) + 1)]
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n,0)
        
        for key, val in freq.items():
            cnt[val].append(key)
        
        res = []
        for i in range(len(cnt) - 1, 0, -1):
            for n in cnt[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res

        
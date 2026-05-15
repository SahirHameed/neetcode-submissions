class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)] # indices as counts of each #'s in nums
        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        for key,value in freq.items():
            count[value].append(key)
        
        res = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                if len(res) == k:
                    return res
                res.append(n)
        
        return res


        
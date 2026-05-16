class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive: Count the frequency of each element in the array and sort based on frequency
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n,0)
        
        arr = []
        for num, cnt in freq.items():
            arr.append([cnt, num])
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        
        for i,n in enumerate(nums):
            comp = target - n
            if comp in sums:
                return [sums[comp], i]
            sums[n] = i
        
        return []
            
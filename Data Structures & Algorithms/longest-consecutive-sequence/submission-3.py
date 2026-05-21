class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        res = 0
        for n in nums:
            streak, cur = 0, n
            while cur in nums_set:
                streak += 1
                cur += 1
            res = max(res, streak)
        return res

        
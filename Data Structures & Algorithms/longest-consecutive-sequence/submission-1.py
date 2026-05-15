class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set(nums)
        res = 0
        for n in nums:
            cur = 0
            if n - 1 not in consec:
                while n + cur in consec:
                    cur += 1
                res = max(res,cur)
        return res
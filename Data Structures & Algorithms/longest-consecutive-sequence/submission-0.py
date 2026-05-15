class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set(nums)
        res = 0
        for i in range(len(nums)):
            cur = 0
            j = 0
            while nums[i] + j in consec:
                cur += 1
                j += 1
            res = max(res,cur)

        return res
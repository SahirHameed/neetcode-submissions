class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Res = [1] * len(nums)
        # Nested for loop, i,j. If nums[i] != nums[j], res[i] *= nums[j]
        # Return res

        res = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res[i] *= nums[j]
        
        return res
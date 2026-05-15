class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Naive: use a nested for loop i, j = i + 1. if nums[i] + nums[j] == target and i != j
        # then return [i,j]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        return []
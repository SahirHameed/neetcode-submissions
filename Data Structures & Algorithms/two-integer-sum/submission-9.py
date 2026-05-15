class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: create a nested for loop and check to see if the values
        # at i,j=i+1 added sum to the target

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        
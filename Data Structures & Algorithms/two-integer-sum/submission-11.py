class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: create a nested for loop and check to see if the values
        # at i,j=i+1 added sum to the target

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        # optomized: create a hashmap that stores the complement for each number 
        # in the list that sums to target and store the index it was at

        pairs = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in pairs:
                return [pairs[comp], i]
            pairs[nums[i]] = i
        
        return pairs

        
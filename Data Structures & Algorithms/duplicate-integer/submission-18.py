class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Naive Solution: Use a double nested for loop, i, j = i + 1. if nums[i] == nums[j],
        # duplicate found, return true else return false 
        # Time: O(n^2) , Space: O(1)

        # Optimal: Use a set. Loop through all nums. if the number is not in the set, add it
        # else return true (dup found). After loop, return false

        dup_set = set()

        for n in nums:
            if n not in dup_set:
                dup_set.add(n)
            else:
                return True
        
        return False
        

        
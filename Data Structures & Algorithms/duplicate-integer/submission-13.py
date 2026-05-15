class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force: nested for loop (i,j= i + 1) and check to see if
        # the values match. If so return true, else false
        # Time: O(N^2), Space O(1)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

        # Optomized: Loop once through the lists and add the values to a set.
        # if the value exists in the set, return true. else false


        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Declaring a set
        # Loop through the values in nums
        # If a value in nums is already in the set, return true
        # Add the value to the set
        # Exit the loop and return false

        dups = set()
        for n in nums:
            if n in dups:
                return True
            dups.add(n)
        return False
            
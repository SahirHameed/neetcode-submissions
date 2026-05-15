class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()

        for a in nums:
            if a in dups:
                return True
            dups.add(a)
        
        return False
        
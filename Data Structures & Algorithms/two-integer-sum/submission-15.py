class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force: Loop through values at i, j = i + 1 and check if the values add to target
        # and return a list with i and j
        # Optomized: Use a hashmap where the key is the complement (target - nums[i]) and the value
        # is i
        # if the complement is in the hashmap, return a list of hashmap[complement] and i
        # Else hashmap[nums[i]] = i
        # return an empty list if nothing is found

        sums = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in sums:
                return [sums[comp], i]
            sums[n] = i
        return []
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Res = [1] * len(nums)
        # Nested for loop, i,j. If i != j, res[i] *= nums[j]
        # Return res

        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             res[i] *= nums[j]
        
        # return res

        zero_cnt = 0
        total = 1
        for n in nums:
            if n:
                total *= n
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zero_cnt == 1: 
                if c == 0:
                    res[i] = total
            else:
                res[i] = total // c

        return res        


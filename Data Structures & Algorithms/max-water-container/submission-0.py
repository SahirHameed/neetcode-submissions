class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1
        l = 0
        r = len(heights) - 1

        while l < r:
            length = min(heights[l], heights[r])
            width = r - l
            
            res = max(res, length * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
        
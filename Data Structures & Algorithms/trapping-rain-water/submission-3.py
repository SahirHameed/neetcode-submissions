class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force: calculate the max left and right height at index i
        # and update res as min(maxLeft, maxRight) - height[i]
        
        if not height:
            return 0
        
        res = 0
        length = len(height)

        for i in range(length):
            maxLeft = maxRight = height[i]

            for j in range(i):
                maxLeft = max(maxLeft, height[j])
            for j in range(i + 1, length):
                maxRight = max(maxRight, height[j])
            
            water_height = min(maxLeft, maxRight) - height[i]
            res += water_height if water_height > 0 else 0
        
        return res

        

        
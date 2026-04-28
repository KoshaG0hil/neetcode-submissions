class Solution:
    def trap(self, heights: List[int]) -> int:
    
        total_water=0

        for i in range(1,len(heights)-1):
            left=max(heights[0:i])
            right=max(heights[i+1:])
            water = min(left, right) - heights[i]
            total_water+=max(water,0)
        
        return total_water


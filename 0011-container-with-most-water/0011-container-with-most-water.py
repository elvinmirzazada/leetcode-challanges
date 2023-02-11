class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        
        while i < j:
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            max_area = max(area, max_area)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return max_area
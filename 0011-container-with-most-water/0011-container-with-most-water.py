class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_amount = 0
        while start < end:
            length = end - start
            amount = min(height[start], height[end]) * length
            if amount > max_amount:
                max_amount = amount
                
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
                
        return max_amount
            
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)
        
        for i, n in enumerate(boxes):
            
            for j in range(i+1, len(boxes)):
                
                if boxes[j] == '1':
                    
                    result[i] += abs(i-j)
                    
        
        for i in range(len(boxes)-1, -1, -1):
            
            for j in range(i-1, -1, -1):
                
                if boxes[j] == '1':
                    
                    result[i] += abs(i-j)
        
        
        return result
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for n in nums:
            result += [res + [n] for res in result]
            
            
        return result
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # visited = {}
        res = 0
        
        
        for i in range(len(nums)):
            min_el = nums[i]
            max_el = nums[i]
            for j in range(i, len(nums)):

                max_el = max(max_el, nums[j])
                min_el = min(min_el, nums[j])
                # if (i, j) not in visited:
                #     visited[(i, j)] = (max_el - min_el)
                    
                res += max_el-min_el
                    
        return res
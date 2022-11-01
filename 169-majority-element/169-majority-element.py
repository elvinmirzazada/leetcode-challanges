class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_el = nums[0]
        count = 0
        
        for num in nums:
            if num == maj_el:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    count += 1
                    maj_el = num
        
        return maj_el
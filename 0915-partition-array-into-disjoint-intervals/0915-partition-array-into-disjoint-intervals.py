class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
#         i = 0
#         left_max = 0
#         right_max = 0
        
#         while i < len(nums):
#             left_max = max(left_max, nums[i])
#             right_min = min(nums[i+1:])
            
#             if left_max > right_min:
#                 i += 1
#             else:
#                 return i+1
            
        curr_max = nums[0]
        possible_max = nums[0]
        length = 1

        for i in range(1, len(nums)):
            if nums[i] < curr_max:
                length = i + 1
                curr_max = possible_max
            else:
                possible_max = max(possible_max, nums[i])

        return length

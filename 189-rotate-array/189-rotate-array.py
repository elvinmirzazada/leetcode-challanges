
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         if k > len(nums):
#             k = k % len(nums)

#         first = nums[: -k]
#         second = nums[-k:]
#         while nums:
#             nums.pop()
#         nums.extend(second)
#         nums.extend(first)
        
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        while start < end: #
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

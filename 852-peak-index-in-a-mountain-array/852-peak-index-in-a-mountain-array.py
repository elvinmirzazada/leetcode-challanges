class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        i = 0
        j = len(arr)-1
        
        while i <= j:
            mid = (i+j) // 2
            if mid-1 >= 0 and arr[mid-1] > arr[mid]:
                j = mid - 1
            elif mid + 1 < len(arr) and arr[mid+1] > arr[mid]:
                i = mid + 1
            else:
                return mid
            
        return 1
            
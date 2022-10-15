class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        length = 0
        i = 1
        arr_len = len(arr)
        if arr_len < 3:
            return 0
        while i < len(arr)-1:
            count = 0
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                k = i - 1
                m = i + 1
                count += 1
                
                while k >= 0 and arr[k] < arr[k+1]:
                    count += 1
                    k -= 1
                    
                while m < len(arr) and arr[m-1] > arr[m]:
                    count += 1
                    m += 1
                    
                    
            if count > length:
                length = count
                
            i += 1
            
        return length
            
            
    
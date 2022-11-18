class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        i, j = 0, len(letters)-1
        
        while i <= j:
            mid = (i+j) // 2
            if letters[mid] > target:
                j = mid -1
            elif letters[mid] <= target:
                i = mid + 1
            
        if letters[i] <= target:
            return letters[i+1]
        else:
            return letters[i]
                
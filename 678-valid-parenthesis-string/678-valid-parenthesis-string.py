class Solution:
    def checkValidString(self, s: str) -> bool:
        left_balance = 0
        for ch in s:
            if ch == '(' or ch == '*':
                left_balance += 1
            else:
                left_balance -= 1
                
            if left_balance < 0:
                return False
            
        if left_balance == 0:
            return True
        
        right_balance = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')' or s[i] == '*':
                right_balance += 1
            else:
                right_balance -= 1
            
            if right_balance < 0:
                return False
        
        return True
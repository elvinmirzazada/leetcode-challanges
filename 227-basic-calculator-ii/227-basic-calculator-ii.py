class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        curr_num = 0
        last_op = "+"
        ops = {"*", "/", "-", "+"}
        nums = set(str(x) for x in range(10))
        
        for idx in range(len(s)):
            ch = s[idx]
            
            if ch in nums:
                curr_num = curr_num * 10 + int(ch)
                
            if ch in ops or idx == len(s)-1:
                if last_op == '+':
                    stack.append(curr_num)
                elif last_op == '-':
                    stack.append(-curr_num)
                elif last_op == '*':
                    stack[-1] *= curr_num
                elif last_op == '/':
                    stack[-1] = int(stack[-1] / curr_num)
                
                curr_num = 0
                last_op = ch

        return sum(stack)
                
    
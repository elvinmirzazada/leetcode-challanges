class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        self.add_par("(", result, 1, 0, n)
        return result
              
    
    
    def add_par(self, string, res, open_t, close_t, n):
        
        if close_t == n and open_t == n:
            res.append(string)
        
        elif open_t == n:
            string += ")"
            close_t += 1
            self.add_par(string, res, open_t, close_t, n)
            
        elif open_t <= n and close_t <= n:
            self.add_par(string+'(', res, open_t+1, close_t, n)
            if open_t > close_t:
                self.add_par(string+')', res, open_t, close_t+1, n)
        
        
        
        
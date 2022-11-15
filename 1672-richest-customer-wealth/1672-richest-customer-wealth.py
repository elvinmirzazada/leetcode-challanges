class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0 
        for row in accounts:
            wealth = 0
            for item in row:
                wealth += item
            max_wealth = max(max_wealth, wealth)
        
        return max_wealth
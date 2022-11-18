from collections import defaultdict

class Solution:
    WHITE, GRAY, BLACK = 1, 2, 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        for course, must_course in prerequisites:
            adj_map[must_course].append(course)
            
        sorted_order = []
        is_possible = True
        
        color = {k: Solution.WHITE for k in range(numCourses)}
        
        def dfs(node):
            nonlocal is_possible
            
            if not is_possible:
                return
            
            color[node] = Solution.GRAY
            
            if node in adj_map:
                for n in adj_map[node]:    
                    if color[n] == Solution.WHITE:
                        dfs(n)
                    elif color[n] == Solution.GRAY:
                        is_possible = False
                        
            color[node] = Solution.BLACK
            sorted_order.append(node)
            
        for v in range(numCourses):
            if color[v] == Solution.WHITE:
                dfs(v)
        
        return sorted_order[::-1] if is_possible else []
        
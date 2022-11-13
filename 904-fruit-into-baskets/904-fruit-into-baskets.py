class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        tree_map = {}
        max_num = 0
        start = 0
        
        for idx, tree in enumerate(fruits):
            if len(tree_map) < 2 and tree not in tree_map:
                tree_map[tree] = True
                max_num = max(max_num, idx - start + 1)
            elif tree in tree_map:
                max_num = max(max_num, idx - start + 1)
            else:
                tree_map = {}
                tree_map[fruits[idx-1]] = True
                tree_map[tree] = True
                start = idx-1
                
                while fruits[start] == fruits[start-1]:
                    start -= 1
                    
                    
                max_num = max(max_num, idx - start + 1)
                
        return max_num
#         max_fruit = 0
#         baskets = {}
        
#         for idx, i in enumerate(fruits):
#             num_fruit = 0
            
#             for j in range(idx, len(fruits)):
#                 if fruits[j] in baskets:
#                     num_fruit += 1
#                 elif len(baskets) < 2:
#                     num_fruit += 1
#                     baskets[fruits[j]] = True
#                 elif len(baskets) >= 2:
#                     del baskets[i]
#                     break
            
#             max_fruit = max(max_fruit, num_fruit)
            
#         return max_fruit

        
        
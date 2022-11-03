class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        for i in range(len(searchWord)):
            tmp = [x for x in products if x[:i+1] == searchWord[:i+1]]
            # tmp = sorted(tmp)
            result.append(tmp[:3])
            
        return result
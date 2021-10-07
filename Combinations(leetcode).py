from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1 
        # combine_list = list(combinations(list(range(1,n+1)),k))
        # return combine_list
        
        # 2
        result = []
        cur = []
        def backtrack(num):
            if len(cur) == k:
                result.append(list(cur))
            else:
                for i in range(num, n + 1):
                        cur.append(i)
                        backtrack(i + 1)
                        cur.pop()
        backtrack(1)
        
        return result

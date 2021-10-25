from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         for i in range(len(nums)+1):
#             for j in combinations(nums,i):
#                 # combinations의 리턴 타입은 tuple, list()로 감싸면 list로 바뀐다
#                 # temp = list(j)
#                 result.append(list(j))
                
#         return result
        result = [[]]
        for num in nums:
            result += [cur + [num] for cur in result]
            
        return result

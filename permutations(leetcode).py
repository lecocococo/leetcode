from itertools import permutations
# from itertools import combinations  => 순서 바뀐것을 같은 쌍으로 취습 1,2 = 2,1
# from itertools import product  => 2개 이상의 리스트에서 모든 조합 구하기
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums,len(nums)))

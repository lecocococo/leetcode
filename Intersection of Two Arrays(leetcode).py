class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1번 풀이
        # n1 = set(nums1)
        # n2 = set(nums2)
        # result = []
        # if len(n1) < len(n2):
        #     for i in n1:
        #         if i in n2:
        #             result.append(i)
        # else:
        #     for i in n2:
        #         if i in n1:
        #             result.append(i)
        # return result
        
        #2번 풀이 
        return set(nums1).intersection(set(nums2))

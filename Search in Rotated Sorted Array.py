class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<1:
            return -1
        
        def binary_search(start, end):
            
            if start>end:
                return -1
            
            middle = (start + end)//2
            middle_val = nums[middle]
            
            if target == middle_val:
                return middle
            
            start_val = nums[start]
            
            if start_val <= middle_val:
                if start_val<=target and target<middle_val:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if middle_val<target and target<=nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
            return binary_search(start, end)
        
        return binary_search(0,len(nums)-1)
    
#         시간 복잡도: O(n)
#         try:
#             return nums.index(target)
#         except:
#             return -1

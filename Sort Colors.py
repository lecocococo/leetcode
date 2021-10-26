class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         퀵정렬이용(이문제에 특화 x)
#         def quick_sort(nums, start, end):
#             if start>=end:
#                 return
#             pivot = start
#             left = start + 1
#             right = end
            
#             while left<=right:
#                 while left<=end and nums[left]<=nums[pivot]:
#                     left+=1
#                 while right>start and nums[right]>=nums[pivot]:
#                     right-=1
#                 # 교차한다는건 다훓어보았고 피벗의 위치를 바꿔줄때 라는것
#                 if left>right:
#                     nums[pivot],nums[right] = nums[right], nums[pivot]
#                 else:
#                     nums[pivot],nums[right] = nums[right], nums[pivot]
                    
#             quick_sort(nums, start, right-1)
#             quick_sort(nums, right+1, end)
            
#         quick_sort(nums, 0, len(nums)-1)
#         print(nums)

        left = 0
        curr = 0
        right = len(nums)-1
        
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1

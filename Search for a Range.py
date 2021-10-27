from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if len(nums) == 0:
        #     return [-1, -1]
        # s = bisect_left(nums,target)
        # e = bisect_right(nums,target)
        # print(s,e)
        # if nums[e-1]!=target or nums[s]!=target:
        #     return [-1, -1]
        # return [s, e-1]
        
        if not nums:
            return [-1, -1]
        
        l,r = 0, len(nums) - 1 
        while l < len(nums) and nums[l] < target:
            l += 1
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        while r >= 0 and nums[r] > target:
            r -= 1
        return [l, r]

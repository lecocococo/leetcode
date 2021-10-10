class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        i=0
        # print(nums)
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                return nums[i]
            
            i+=2
        return nums[len(nums)-1]

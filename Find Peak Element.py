class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        sub = []
        for i in range(len(nums)):
            temp = bisect_left(sub,nums[i])
            if temp<len(sub):
                return i-1
            else:
                sub.append(nums[i])
        return nums.index(sub[len(sub)-1])

        # 같은방법
        # l,r=0,len(nums)-1
        # while l<r:
        #     m=(l+r)//2
        #     if nums[m]<nums[m+1]:
        #         l=m+1
        #     else:
        #         r=m
        # return l

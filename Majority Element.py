from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # return Counter(nums).most_common(1)[0][0]
        
        nums.sort()
        return nums[len(nums)//2]

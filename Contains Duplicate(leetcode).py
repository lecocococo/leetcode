from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Counter 사용 (느림)
        # count = Counter(nums)
        # temp = count.most_common(n=1)
        # if temp[0][1] > 1:
        #     return True
        # return False
        
        # 정렬후 비교(빠름)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

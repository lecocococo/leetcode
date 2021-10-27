class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp=[1]
        # mx = 0
        # result = 1
        # tmp = 0
        # for i in range(1,len(nums)):
        #     mx = 0
        #     for j in range(i-1,-1,-1):
        #         if nums[i]>nums[j]:
        #             mx = max(mx,dp[j]);
        #     if mx!=0:
        #         dp.append(mx+1)
        #     else:
        #         dp.append(1)
        #     result = max(result,dp[i])
        #     # print(dp)
        # return result
        
        sub = []
        for num in nums:
            # bisect_left는 bisect 모듈의 이진검색 함수/ 정렬된 sub에 num를 삽입할 위치를 리턴해준다. num이 sub에 이미               있으면 기존 항목의 앞 (왼쪽)의 위치를 반환
            i = bisect_left(sub, num) 

            # num이 sub의 어떤값보다 클떄 
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        
        return len(sub)

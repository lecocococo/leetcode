class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # visited = 0
        # n = len(nums) - 1
        # for i in range(n):
        #     if visited < i + nums[i]:
        #         if visited < i:
        #             return False
        #         visited = i + nums[i]
        # return visited >= n
        
        # greedy(좀 더 빠름)
        n = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= n:
                n = i
        return n == 0

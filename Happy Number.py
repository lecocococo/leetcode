class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set() 
        while n!= 1:
            num = 0
            s = str(n)
            
            for i in s:
                num += int(i)**2
                
            if num in nums:
                return False
            
            nums.add(num)
            n = num
        return True

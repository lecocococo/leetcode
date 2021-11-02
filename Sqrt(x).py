class Solution:
    def mySqrt(self, x: int) -> int:
        # cnt = 0
        # su = 0
        # while x>su:
        #     su += (3+2*cnt)
        #     cnt += 1
        # return cnt
        
        num = 0
        while num * num < x:
            num += 10
        while num * num > x:
            num -= 1
        return num

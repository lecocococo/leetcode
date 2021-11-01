class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 르장드르 공식의 특별한 case
        # 5의 다중도로 결정이 됨
        # 쉽게 생각하면 n이 5의 배수일때마다 뒤에 0이 하나씩 붙는다
        
        # exp = 1
        # while 1:
        #     p = math.pow(5,exp)
        #     if p>n:
        #         break
        #     exp+=1
        # result = 0
        # for j in range(1,exp):
        #     result += (n//math.pow(5,j))
        # return int(result)
        
        result = 0
        while n > 0:
            result += n // 5
            n = n // 5
        return result

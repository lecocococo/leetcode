class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 무조건 첫번째 기호가 첫번째로 계산된다
        # 첫번째 기호 계산시 무조건 앞에 2개의 숫자는 존재한다
        
        # list 이용
        # rpn = tokens
        # op = ['+', '-', '*','/']
        # temp = 0
        # def check(a, b, oper):
        #     if oper == '+':
        #         return a + b
        #     elif oper == '-':
        #         return a - b
        #     elif oper == '*':
        #         return a * b
        #     elif oper == '/':
        #         return math.trunc(a / b)
        # # print(math.trunc(6/-132))
        # # print(rpn)
        # i = 0
        # while i < len(rpn):
        #     if len(rpn) == 1:
        #         return int(rpn[0])
        #     if rpn[i] in op:
        #         temp = check(int(rpn[i-2]), int(rpn[i-1]), rpn[i])
        #         print(temp)
        #         del rpn[i], rpn[i-1]
        #         rpn[i-2] = str(temp)
        #         i = -1
        #     i+=1 
        
        # stack 이용
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                num1, num2 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(num2+num1)
                elif token == "-":
                    stack.append(num2-num1)
                elif token == "*":
                    stack.append(num2*num1)
                else:
                    stack.append(math.trunc(num2 / num1))
        return stack.pop()

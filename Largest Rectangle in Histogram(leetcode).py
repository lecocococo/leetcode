class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0
        
        for index, height in enumerate(heights):
            if stack == []: 
                stack.append([index, height])
            else:
                temp_idx = index
                while stack != [] and stack[-1][1] > height: 
                    top = stack.pop()
                    temp_idx = top[0] 
                    size = top[1] * (index - top[0])
                    if result < size: 
                        result = size
                stack.append([temp_idx, height])#인덱스를 바꿔주는이유는 이전에 pop된 값들이 현재 push되는값 기준으론 
                                              #넓이 확장에 도움이된다. 그래서 인덱스를 마지막에 pop된 인덱스를 사용함
                                              #사용하게 된다면 넓이를 구하는데 사용이됨 ex)[2,1,5,6,2,3,2,2]
        for top in stack: 
            size = top[1] * (len(heights) - top[0]) 
            if result < size:
                result = size
        return result

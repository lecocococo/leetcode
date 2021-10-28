class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals, key = lambda x: (x[0],x[1]))
        # print(arr)
        result = []
        temp = [0, 0]
        start = 0
        end = 0
        for i in range(len(arr)):
            if i == 0:
                temp = arr[i]
                start = temp[0]
                end = temp[1]
                continue
            if arr[i][0] <= end:
                temp[1] = max(end,arr[i][1])
                end = temp[1]
            else:
                result.append(temp)
                temp = arr[i]
                start = temp[0]
                end = temp[1]
        result.append(temp)
        return result

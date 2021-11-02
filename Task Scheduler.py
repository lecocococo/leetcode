from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        # time = 0
        # heap = []
        # for key, val in Counter(tasks).items():
        #     heappush(heap, (-1*val, key)) # heapq가 minheap이기 때문에 maxheap처럼 사용하기위해 -1을 곱해줌
        # while heap:
        #     idx = 0
        #     temp = []
        #     while idx <= n:
        #         time += 1
        #         if heap:
        #             i,j = heappop(heap)
        #             if i != -1:
        #                 temp.append((i+1,j)) # 1개사용
        #         # 더이상 할 작업이 없다면 break
        #         if not heap and not temp:
        #             break
        #         else:
        #             idx += 1
        #     # 다시 heap에 넣기(-1보다 작은 숫자는 아직 남아있는 task가 있기 때문에)
        #     for item in temp:
        #         heappush(heap, item)
        # return time
        
        count = collections.Counter(tasks)
        values = sorted(count.values())
        max_item = values.pop()
        curr_idle = (max_item - 1) * n
        
        for v in values:
            curr_idle -= min(v, max_item - 1)
        return max(curr_idle, 0) + len(tasks)

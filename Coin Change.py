from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
#         # 기본값으로 최대값을 줌(최소값을 찾기 위해 )
#         dp = [0]+[sys.maxsize for _ in range(amount)]
        
#         for i in range(1,amount+1):
#             for coin in coins:
#                 if i - coin>=0:
#                     dp[i] = min(dp[i], dp[i - coin] + 1)
#             # print(dp)
            
#         if dp[amount] == sys.maxsize:
#             return -1
        
#         return dp[amount]
        # 훨씬 빠르다 앞의 풀이와 다르게 전부다 값을 만들어내지 않기때문에 비교할 값도 게산할 값도 현저히 줄어듬
        visited = set()
        # [] 한번더 친 이유는 iterable하게 만들어주기위해
        q = deque([[0, 0]])
        while q:
            current_amount, coin_used = q.popleft()
            
            if current_amount == amount:
                return coin_used
            # 아래에서 무조건 코인값을 다 더해서 큐에 넣어줌으로 amount를 넘어가게 되는 경우도 당연히 존재하기때문에
            elif current_amount > amount:
                continue
            for coin in coins:
                temp_amount = current_amount + coin
                if temp_amount not in visited:
                    q.append((temp_amount, coin_used+1))
                    visited.add(temp_amount)
        return -1

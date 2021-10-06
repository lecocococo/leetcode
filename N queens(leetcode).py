class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [0 for i in range(n)]
        def dfs(row):
            cnt = 0
            if row == n:
                return 1
            
            for col in range(n):
                #board[row]는 row에 위치한 퀸의 colum
                board[row] = col
                for i in range(row):
                    if board[i] == board[row]:
                        break
                    if abs(board[i] - board[row]) == row - i:
                        break
                else:
                    cnt += dfs(row+1)
            return cnt
        return dfs(0)

class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        cnt = 0
        def dfs(board, word, i, j, row, col, index):
            # global cnt
            if index == len(word):
                return True
            if row<0 or col<0 or row>=i or col>=j:
                return False
            if board[row][col] != word[index]:
                return False
            
            temp = board[row][col]
            # 갔던곳 값 바꿈
            board[row][col] = "1"
            
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if dfs(board, word, i, j, row + x, col + y, index + 1):
                    return True
            board[row][col] = temp
            return False
        
        # print(word[cnt])
        i = len(board)
        j = len(board[0])
        for row in range(i):
            for col in range(j):
                if board[row][col]==word[0]:
                    if dfs(board, word, i, j, row, col, 0) == True:
                        return True

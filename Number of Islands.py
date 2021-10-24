class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0;
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] is "0":
                return
            grid[i][j] = "0"
            # 위,아래,왼쪽, 오른쪽을 탐색
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j)
                    cnt+=1
                    
        return cnt

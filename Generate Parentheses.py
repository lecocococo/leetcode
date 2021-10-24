class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(s="", open=0, close=0):
            if open == n:
                result.append(s+")"*(n-close))  # "(" 개수 다채웠으면 나머진")"
            else:
                dfs(s+"(", open+1, close)  # "(" 개수 다 안채웠으면 "(" 추가
                if close < open:
                    dfs(s+")", open, close+1)  # "("개수가 ")" 보다 많으면 "(" 추가

        dfs()
        
        return result

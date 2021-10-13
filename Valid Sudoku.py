class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = {}
        for i in range(1,10):
            check[str(i)] = [set(), set(), set()]
        print(check)
        for i,r in enumerate(board):
            for j,c in enumerate(r):
                if c != ".":
                    sub_block = (i//3)*3+j//3
                    # 예를들어 1이 나오는 행,열,작은 박스의 위치를 저장해두고 확인하는것(같은 행, 열, 박스에 위치불가)
                    if i in check[c][0] or j in check[c][1] or sub_block in check[c][2]:
                        return False
                    check[c][0].add(i)
                    check[c][1].add(j)
                    check[c][2].add(sub_block)
        # print(check)
        return True

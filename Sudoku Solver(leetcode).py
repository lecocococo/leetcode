class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check_empty(arr,empty):
            for i in range(9):
                for j in range(9):
                    if arr[i][j]==".":
                        empty[0] = i
                        empty[1] = j
                        return True
            return False
        
        def check_row(arr,row,num):
            for i in range(9):
                if arr[row][i] == num:
                    return True
            return False
            
        def check_col(arr,col,num):
            for i in range(9):
                if arr[i][col] == num:
                    return True
            return False
        
        def check_box(arr, row, col,num):
            for i in range(3):
                for j in range(3):
                    if arr[row + i][col+j] == num:
                        return True
            return False
        
        def is_posible(arr,row,col,num):
            return not check_row(arr,row,num) and not check_col(arr,col,num) and not check_box(arr, row - row%3, col - col%3,num)
        
        
        def sudoku_solver(arr):
            empty = [0,0]
            if not check_empty(arr,empty):
                return True
            
            row = empty[0]
            col = empty[1]
            
            for num in range(1,10):
                if is_posible(arr,row,col,str(num)):
                    arr[row][col] = str(num)
                    
                    if sudoku_solver(arr):
                        return True
                    
                    arr[row][col] = "."
            return False
        
        sudoku_solver(board)
            
# 1 2 4  => 1
# 2 6    => 2
# 4 6 8   => 4
# 9  => 9
# x

class Solution {
    public void setZeroes(int[][] matrix) {
        boolean isFirstRowHaveZero = false;
        boolean isFirstColHaveZero = false;
        
        int r = matrix.length;
        int c = matrix[0].length;
        
        //첫번쨰 행 확인
        for (int i = 0;i<c;i++){
            if (matrix[0][i]==0){
                isFirstRowHaveZero = true;
                break;
            }
        }
        //첫번째 열 확인
        for (int j = 0;j<r;j++){
            if (matrix[j][0]==0){
                isFirstColHaveZero = true;
                break;
            }
        }
        //전체 확인
        for (int i = 1;i<r;i++){
            for (int j = 1;j<c;j++){
                if(matrix[i][j]==0){
                    matrix[i][0]=0;
                    matrix[0][j]=0;
                }
            }
        }
        //0으로 바꾸기
        for (int i = 1;i<r;i++){
            for (int j = 1;j<c;j++){
                if(matrix[i][0]==0||matrix[0][j]==0){
                    matrix[i][j]=0;
                }
            }
        }
        //행 0으로 바꾸기
        if(isFirstRowHaveZero){
            for(int i = 0;i<c;i++){
                matrix[0][i]=0;
            }
        }
        //열 0으로 바꾸기
        if(isFirstColHaveZero){
            for(int j = 0;j<r;j++){
                matrix[j][0]=0;
            }
        }
        
    }
}

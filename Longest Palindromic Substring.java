// class Solution {
//     public String longestPalindrome(String s) {
//         String result = "";
//         char[] arr = s.toCharArray();
//         int mx = 0;
//         boolean[][] dp = new boolean[arr.length][arr.length];
        
//         for(int i = arr.length - 1; i>=0;i--){
//             for(int j = i;j<arr.length;j++){
//                 //초반에 dp[i+1][j-1]여기서 배열범위를 안넘게 하기 위해서 가장 마지막에 배치(가장 마지막확인 )
//                 dp[i][j] = (arr[i]==arr[j]&&(j-i<=2||dp[i+1][j-1]));
//                 if(dp[i][j]&&j-i>=mx){
//                     mx = j-i;
//                     result = s.substring(i,j+1);
//                 }
//             }
//         }
//         return result;
        
//     }
// }
//2 더 빠름
// class Solution {
//     public String longestPalindrome(String s) {
//         int max = 0;
//         int i = 0 ;
//         int left = -1;
//         int right = -1 ;
//         while( i < s.length()){
//             int len1 = expandboth( s, i , i);
//             int len2  = expandboth( s, i , i+1);
//             if ( len1 > max ){
//                 max = len1; 
//                 left = i -len1/2;
//                 right = i+len1/2;
//             }
//             if( len2 > max){
//                 max = len2;
//                 left = i+1-len2/2;
//                 right = i+len2/2;
//             }
            
//             i++;
//         }
        
//         return s.substring( left , right+1);
//     }
    
//     private int expandboth( String s, int left , int right){
        
//         while( left >=0 && right < s.length() && s.charAt(left)== s.charAt(right) ){
//             left--;
//             right++;
//         }
        
//         return right-left-1;
//     }
// }

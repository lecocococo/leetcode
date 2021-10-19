class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if(s.length()<2)
            return s.length();
        // sliding window 알고리즘
        Set<Character> cset = new HashSet();
        char[] str = s.toCharArray();
        int left = 0;
        int right = 0;
        int result = 0;
        while (right<str.length){
            while (cset.contains(str[right])){
                cset.remove(str[left]);
                left++;
            }
                
            cset.add(str[right]);
            right++;
            
            result = Math.max(result, cset.size());
        }
            
        return result;
        
//         또다른 방식        
//         if(s.length() ==0 ){
//             return 0;
//         }
     
//         int res =0;
//         Map<Character, Integer> map = new HashMap();
        
//         for(int j=0, i=0; j < s.length() ; j++){
            
//             if(map.containsKey(s.charAt(j))){
//                 i = Math.max(i, map.get(s.charAt(j)));
//             }
            
            
//             res = Math.max(res, j-i+1);
//             map.put(s.charAt(j), j+1);
//         }
//         return res;
    }
}
// String.valueOf(char[]) 는 char[]를 string으로 변환해줌

class Solution {
    int cnt = 0;
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character,Integer> map = new HashMap();
        char[] jewel = jewels.toCharArray();
        char[] stone = stones.toCharArray();
        
        for(int i =0; i<jewel.length;i++)
            map.put(jewel[i],0);
        
        for(int i =0; i<stone.length;i++){
            if(map.containsKey(stone[i])){
                map.replace(stone[i],map.get(stone[i])+1);
                cnt++;
            }
        }
        
        // 굳이 돌면서 value 값을 더해줄 필요가 없었다 
        // map.forEach((key,value)->{
        //     if(value>0)
        //         cnt+=value;
        // });
        
        return cnt;
    }
}

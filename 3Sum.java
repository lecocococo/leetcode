class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // 중복제거 하려고 사용했지만 배열로 바꾸는 과정에서 오류발생
        // Set<Integer> set = new TreeSet<>();
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        //빠르게 잘라줄 곳은 잘라줌
        if(nums==null||nums.length<3){
            return result;
        }
        //값을 하나 선택해두고 그바로 뒤의 셀에 left, 배열의 끝에 right를 설정해둠
        //정렬이 되어있기때문에 0보다 크면 right를 줄이고 0보다 작으면 left를 올려줌
        //그리고 항상 중복은 제거해준다 
        for(int i=0;i<nums.length;i++){
            if(nums[i]>0)
                return result;
            if(i>0 && nums[i] == nums[i-1])
                continue;    
            
            int left = i+1;
            int right = nums.length - 1;
            
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                
                if(sum>0){
                    right--;
                }
                else if(sum<0){
                    left++;
                }
                else{
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    
                    while(left<right && nums[left] == nums[left-1]) {
                        left++;
                    }
                    while(left<right && nums[right] == nums[right+1]) {
                        right--;
                    }
                }
                
            }
        }
        return result;
    }
}

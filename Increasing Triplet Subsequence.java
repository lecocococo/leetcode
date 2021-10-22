class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first = nums[0];
        int second = Integer.MAX_VALUE;
        if(nums.length<3)
            return false;
        for(int i=1;i<nums.length;i++){
            // 2번째가 정해진 상황에서 새로운 값이 큰지본다
            if (nums[i]>second)
                return true;
            //3번쨰 값으로 2번쨰보다 큰갑이 안들어왔으니 지금 들어온값이 2번째값이된다
            if (nums[i]>first)
                second = nums[i];
            //2번째 값도 안되었으니 이젠 가장 첫번쨰 값으로 해준다
            if (nums[i]<first)
                first = nums[i];
        }
        return false;
    }
}

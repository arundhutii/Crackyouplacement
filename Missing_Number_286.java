class Solution {
    public int missingNumber(int[] nums) {
        int all_xor= 0;
        for (int i=0;i <=nums.length; i++) {
            all_xor= all_xor ^i;
        } 
        for(int num: nums){
            all_xor= all_xor^num;
        }
        return all_xor;
        
    }
}

class Solution {
    public int maxProfit(int[] prices) {
        int buyprice= prices[0];
        int prof=0;
        for(int i=1; i<prices.length;i++){
            if(prices[i]<buyprice){
                buyprice =prices[i];
            }
            else{
                int currentprof = prices[i] -buyprice;
                prof =Math.max(currentprof, prof);
            }
        }
        return prof;
    }
}

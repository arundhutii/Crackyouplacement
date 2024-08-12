class Solution {
    public static long[] productExceptSelf(int nums[]) {
     int n = nums.length;
        long[] result = new long[n];

 

        // Compute the prefix product
        long prefixProduct = 1;
        for (int i = 0; i < n; i++) {
            result[i] = prefixProduct;
            prefixProduct *= nums[i];
        }

 

        // Compute the suffix product and update the result array
        long suffixProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffixProduct;
            suffixProduct *= nums[i];
        }

 

        return result;   
    }
}

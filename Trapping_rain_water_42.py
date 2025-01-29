class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        n=len(height)
        right_max=[0]*n #fixed array size
        
        right_max[n-1]= height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i]= max(height[i],right_max[i+1])
        # print (right_max)

        left_max=0
        for i in range(n):
            left_max= max(left_max,height[i])
            res+= min(left_max, right_max[i])-height[i]
        return res

class Solution:
    def prefixesDivBy5(self, nums):
        ans=[]
        x=0
        for i in nums:
            x = (x * 2 + i) % 5
            # x = (x << 1 | i) % 5
            ans.append(x==0)
        return ans

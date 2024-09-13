class Solution:
    def averageValue(self, nums): 
        count= 0
        sums= 0
        for i in nums:
            if i % 6== 0:
                sums = sums+i
                count+=1
        if count==0:
            result=0
        else:
            result= sums//count
        return result





class Solution:
    def averageValue(self, nums):
        avg=0 
        count= 0
        sums= 0
        for i in nums:
            if i % 2 ==0 and i % 3 == 0:
                sums = sums+i
                count+=1
            if count==0:
                avg=0
            else:
               avg= sums/count
            result= int(avg)
        return result





import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count,l=0,[]    
        for i in nums :
            a=bisect.bisect_right  (l,i*2)#finding the index 
            count+=len (l)-a#finding the number of greater than equal to i*2
            idx=bisect.bisect(l,i)#finding the index where the i need to be inserted
            l[idx:idx]=[i]#trick for inserting at idx much faster than insert()
        return count

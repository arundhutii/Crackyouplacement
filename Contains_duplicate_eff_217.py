class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_s=set()
        for i in nums: 
            if i in nums_s:
                return True
            nums_s.add(i)
        return False
            

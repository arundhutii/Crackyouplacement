class Solution:
    def majorityElement(self, nums):
        maj = nums[0]
        votes = 1

        for i in range(1, len(nums)):
            if votes == 0:
                votes += 1
                maj = nums[i]
            elif maj == nums[i]:
                votes += 1
            else:
                votes -= 1
        
        return maj

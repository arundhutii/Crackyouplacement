class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [i, seen[rem]]
            
            seen[num] = i

        return False

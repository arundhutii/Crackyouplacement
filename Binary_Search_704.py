#method1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2  # Use integer division to ensure mid is an integer
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

#method2 
def search(self, nums, target):
    low=0
    high=len(nums)-1

    while low<=high:
        mid= (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            low= mid+1
        else:
            high= mid-1
    return -1

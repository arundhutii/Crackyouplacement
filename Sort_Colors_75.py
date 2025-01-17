class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, mid, end = 0, 0, len(nums) - 1 
        while mid <= end:
            if nums[mid] == 0:  # Case for 0
                self.swap(nums, start, mid)
                start += 1
                mid += 1
            elif nums[mid] == 1:  # Case for 1
                mid += 1
            else:  # Case for 2
                self.swap(nums, mid, end)
                end -= 1

    def swap(self, arr: list[int], i1: int, i2: int) -> None:
        arr[i1], arr[i2] = arr[i2], arr[i1]

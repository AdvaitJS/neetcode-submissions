class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    te = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = te
        return nums
        
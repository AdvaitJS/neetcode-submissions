class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            arr = nums[:i] + nums[i+1:]
            prod = 1
            for num in arr:
                prod = prod *num
            ans.append(prod)
        return ans
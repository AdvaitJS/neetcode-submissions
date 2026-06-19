class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:return 0
        nums = set(nums)
        ans = []
        for i in nums:
            if i-1 not in nums:
                count = 1
                while i+count in nums:
                    count +=1
                ans.append(count)
        return max(ans)
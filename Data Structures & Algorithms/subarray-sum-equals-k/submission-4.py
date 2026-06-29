class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        res = defaultdict(int)
        count = 0
        presum = 0
        res[0] = 1
        for i in nums:
            presum += i
            

            count += res[presum - k]
            res[presum] = res[presum] + 1
        return count

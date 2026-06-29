class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        answer = []
        freq = defaultdict(int)

        crit = len(nums)/3

        for element in nums:
            freq[element] = freq[element] + 1
        for i in freq:
            if freq[i] > crit:
                answer.append(i)
        return answer
            